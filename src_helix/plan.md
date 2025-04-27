# Plan: Code Improvements

This document outlines potential improvements for the Python API test scripts and the `runtest.sh` runner, ordered by estimated risk (least to most).

## Implemented Improvements

1.  **Centralized Logging Configuration:**
    *   **Problem:** Repetitive logging setup across scripts.
    *   **Implementation:** Created `configure_logging` function in `api_utils.py` and called it from each test script's `main` function.
    *   **Benefit:** Consistent logging configuration across the project, reduced repetitive code.
    *   **Estimated Lines Eliminated:** Approximately 100 lines across test scripts.
    *   **Risk:** Low.

2.  **Centralized JSON Template Saving:**
    *   **Problem:** Repeated logic for generating and saving JSON templates.
    *   **Implementation:** Created `save_json_template` function in `api_utils.py` and called it from relevant test scripts (`test_cameras_api.py`, `test_token_api.py`, `test_user_details_api.py`, `test_access_events_api.py`, `test_lpoi_api.py`, `test_users_list_api.py`, `test_notifications_api.py`, `test_lpr_timestamps_api.py`).
    *   **Benefit:** Consolidated template saving logic, reduced repetitive code.
    *   **Estimated Lines Eliminated:** Approximately 90 lines across test scripts.
    *   **Risk:** Low.

3.  **Improved `runtest.sh` Argument Handling:**
    *   **Problem:** Repeated logic in `runtest.sh` for prompting for `history_days` and `history_hours`.
    *   **Implementation:** Consolidated time-based argument prompting into the `get_time_args` function in `runtest.sh`.
    *   **Benefit:** Reduced repetition and improved structure in `runtest.sh`.
    *   **Risk:** Low.

4.  **Refined `runtest.sh` Menu Parsing:**
    *   **Problem:** Fragile parsing of `menu_items` array in `runtest.sh` using comma delimiter, which could break if fields contained commas.
    *   **Implementation:** Changed the delimiter for `menu_items` array in `runtest.sh` to pipe `|`.
    *   **Benefit:** More robust parsing of menu items.
    *   **Risk:** Low.

5.  **Created Automated Test Runner (`testit.sh`):**
    *   **Problem:** No automated way to run all tests and check for pass/fail status.
    *   **Implementation:** Created `testit.sh` script to iterate through most tests, handle parameters programmatically for `test_user_details_api.py` (by selecting the first user from the list), skip `test_lpr_timestamps_api.py` (due to requiring specific, non-automatable input), check script exit codes, and report a summary.
    *   **Benefit:** Enables automated testing, provides a quick overview of API endpoint status, and clearly identifies tests that require manual interaction.
    *   **Risk:** Low (for the script itself; relies on the stability and exit codes of the underlying Python tests).

## Remaining Improvement Ideas (Ordered by Least Risk)

1.  **Centralize Pagination Logic:**
    *   **Problem:** The pagination logic (checking for `next_page_token`, looping, accumulating results) is repeated in `fetch_lpr_images_for_camera` and `fetch_lpoi_data`.
    *   **Idea:** Create a generic pagination helper function in `api_utils.py` (e.g., `_fetch_paginated_data(api_token, endpoint, params, list_key, page_size=...)`) that handles the looping and token management. The existing fetch functions (`fetch_lpr_images_for_camera`, `fetch_lpoi_data`) would then call this helper.
    *   **Risk:** Medium. This affects core data fetching logic and requires careful implementation to ensure it works correctly for different endpoints (which might have different keys for the list and the next token).

2.  **Move LPR Filtering Logic to `api_utils`:**
    *   **Problem:** The logic for filtering LPR detections based on the LPOI list is repeated in `test_lpr_lpoi_match_api.py` and `test_lpr_non_lpoi_report_api.py`.
    *   **Idea:** Create functions in `api_utils.py` (e.g., `filter_lpr_by_lpoi(detections, lpoi_set)`, `filter_lpr_by_non_lpoi(detections, lpoi_set)`) that take a list of detections and the LPOI set and return the filtered list. The LPR report scripts would then call these functions after fetching all detections.
    *   **Risk:** Medium. This involves moving business logic, requiring careful testing to ensure filtering is applied correctly in the consuming scripts.

3.  **Refactor User/Camera Selection (Eliminate stdout Parsing):**
    *   **Problem:** The `runtest.sh` and `testit.sh` scripts rely on running Python scripts with special flags (`--list-for-selection`, `--list-for-menu`) and parsing their stdout output, which is fragile and couples the shell scripts tightly to the output format of the Python scripts.
    *   **Idea:** Create dedicated, minimal Python functions (perhaps within `api_utils.py` or a new `listing_utils.py`) specifically for fetching and returning lists of users/cameras in a structured format (e.g., a list of dictionaries). The shell scripts would call these functions directly (or via a minimal wrapper script) and process the structured data, rather than parsing formatted strings from stdout.
    *   **Risk:** Medium. This requires changes in both the shell scripts and modifying/creating Python code to provide structured list data instead of formatted strings.

4.  **Consolidate API Key Reading:**
    *   **Problem:** The API key is read from the environment variable `os.environ.get('API_KEY')` in the `main` function of *every* Python script.
    *   **Idea:** Read the API key once in the main entry point (currently `runtest.sh` or `testit.sh`) and pass it as a command-line argument to the Python script, or read it once in a central Python entry point (if a CLI is developed) and pass it to `get_api_token`.
    *   **Risk:** Medium. This changes the input mechanism for the API key in the Python scripts, requiring modification of argument parsing and function signatures.

5.  **Create a Central Configuration File:**
    *   **Problem:** Default values for parameters like `history_days`, `history_hours`, and `log_level` are hardcoded in both the Python scripts and `runtest.sh`.
    *   **Idea:** Introduce a configuration file (e.g., `config.yaml`) to store default values. The `runtest.sh` script or a central Python entry point would read this file. This would require adding a dependency for parsing the config file (e.g., `PyYAML`).
    *   **Risk:** High. Introduces a new dependency and requires modifying multiple scripts to read configuration instead of relying solely on defaults or command-line arguments.

6.  **Develop a Unified Python CLI:**
    *   **Problem:** The `runtest.sh` script acts as a simple menu wrapper around individual Python scripts. Adding new tests requires modifying the shell script menu and argument handling logic.
    *   **Idea:** Replace `runtest.sh` with a single Python script that uses a library like `argparse` (more extensively) or `click` to define subcommands for each test. This would consolidate argument parsing, menu display, and script execution within Python, making it more portable and potentially easier to manage dependencies and shared logic.
    *   **Risk:** Highest. This is a significant architectural change, requiring rewriting the main entry point and potentially restructuring how tests are organized and run.
