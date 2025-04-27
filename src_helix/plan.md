# Plan: Code Improvements

This document outlines potential improvements for the Python API test scripts and the `runtest.sh` runner, ordered by estimated risk (least to most).

## Remaining Improvement Ideas (Ordered by Least Risk)



3.  **Refactor User/Camera Selection (Eliminate stdout Parsing):**
    *   **Problem:** The `runtest.sh` and `testit.sh` scripts rely on running Python scripts with special flags (`--list-for-selection`, `--list-for-menu`) and parsing their stdout output, which is fragile and couples the shell scripts tightly to the output format of the Python scripts.
    *   **Idea:** Create dedicated, minimal Python functions within `api_utils.py` specifically for fetching and returning lists of users/cameras in a structured format (e.g., a list of dictionaries). The shell scripts would call these functions directly (or via a minimal wrapper script) and process the structured data, rather than parsing formatted strings from stdout.
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
