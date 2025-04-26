# Plan: Code Improvements

This document outlines potential improvements for the Python API test scripts and the `runtest.sh` runner, ordered by estimated risk (least to most).

## Improvement Ideas (Ordered by Least Risk)


5.  **Centralize Pagination Logic:**
    *   **Problem:** The pagination logic (checking for `next_page_token`, looping, accumulating results) is repeated in `fetch_lpr_images_for_camera` and `fetch_lpoi_data`.
    *   **Idea:** Create a generic pagination helper function in `api_utils.py` (e.g., `_fetch_paginated_data(api_token, endpoint, params, list_key, page_size=...)`) that handles the looping and token management. The existing fetch functions (`fetch_lpr_images_for_camera`, `fetch_lpoi_data`) would then call this helper.
    *   **Risk:** Medium. This affects core data fetching logic and requires careful implementation to ensure it works correctly for different endpoints (which might have different keys for the list and the next token).

6.  **Move LPR Filtering Logic to `api_utils`:**
    *   **Problem:** The logic for filtering LPR detections based on the LPOI list is repeated in `test_lpr_lpoi_match_api.py` and `test_lpr_non_lpoi_report_api.py`.
    *   **Idea:** Create functions in `api_utils.py` (e.g., `filter_lpr_by_lpoi(detections, lpoi_set)`, `filter_lpr_by_non_lpoi(detections, lpoi_set)`) that take a list of detections and the LPOI set and return the filtered list. The LPR report scripts would then call these functions after fetching all detections.
    *   **Risk:** Medium. This involves moving business logic, requiring careful testing to ensure filtering is applied correctly in the consuming scripts.

7.  **Refactor `runtest.sh` User/Camera Selection:**
    *   **Problem:** The current method of running `test_users_list_api.py` or `test_cameras_api.py` with a special flag (`--list-for-selection`, `--list-for-menu`) and parsing their stdout output is fragile and couples the shell script tightly to the output format of the Python scripts.
    *   **Idea:** Create dedicated, minimal Python scripts or functions specifically for listing users/cameras in the required format for the shell script, separate from the main test logic. Or, potentially, refactor the main test scripts to have a dedicated "list" command mode that *only* outputs the list. The shell script would call this dedicated function/script and parse its output.
    *   **Risk:** Medium. This requires changes in both the shell script and potentially creating new or modifying existing Python scripts to support a dedicated listing mode, increasing the number of files or complexity of existing ones.

8.  **Consolidate API Key Reading:**
    *   **Problem:** The API key is read from the environment variable `os.environ.get('API_KEY')` in the `main` function of *every* Python script.
    *   **Idea:** Read the API key once in `runtest.sh` and pass it as a command-line argument to the Python script, or read it once in a central Python entry point (if a CLI is developed) and pass it to `get_api_token`.
    *   **Risk:** Medium. This changes the input mechanism for the API key in the Python scripts, requiring modification of argument parsing and function signatures.

9.  **Create a Central Configuration File:**
    *   **Problem:** Default values for parameters like `history_days`, `history_hours`, and `log_level` are hardcoded in both the Python scripts and `runtest.sh`.
    *   **Idea:** Introduce a configuration file (e.g., `config.yaml`) to store default values. The `runtest.sh` script or a central Python entry point would read this file. This would require adding a dependency for parsing the config file (e.g., `PyYAML`).
    *   **Risk:** High. Introduces a new dependency and requires modifying multiple scripts to read configuration instead of relying solely on defaults or command-line arguments.

10. **Develop a Unified Python CLI:**
    *   **Problem:** The `runtest.sh` script acts as a simple menu wrapper around individual Python scripts. Adding new tests requires modifying the shell script menu and argument handling logic.
    *   **Idea:** Replace `runtest.sh` with a single Python script that uses a library like `argparse` (more extensively) or `click` to define subcommands for each test. This would consolidate argument parsing, menu display, and script execution within Python, making it more portable and potentially easier to manage dependencies and shared logic.
    *   **Risk:** Highest. This is a significant architectural change, requiring rewriting the main entry point and potentially restructuring how tests are organized and run.
