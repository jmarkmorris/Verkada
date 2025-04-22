# Code Cleanup Plan for src_helix Scripts

This document outlines the remaining steps to clean up the Python and shell scripts in the `src_helix` directory, focusing on removing duplication, standardizing logging, and improving readability, based on the principles in `../my-globals/README-prompts.md`.

**Overall Goals:**

1.  Eliminate duplicated `get_api_token` and `create_template` functions by using the shared `src_helix.api_utils` module.
2.  Remove duplicated `VERKADA_API_BASE_URL` and `TOKEN_ENDPOINT` constants by importing them from `src_helix.api_utils`.
3.  Standardize logging configuration across all Python scripts using explicit handlers.
4.  Remove unused imports.
5.  Address any other identified code duplication or minor issues.

---

## Cleanup Steps per File:

### `src_helix/test_users_list_api.py`

This file still contains duplicated functions and constants, and uses `basicConfig` for logging instead of explicit handlers.

**Steps:**

1.  Remove the duplicated `get_api_token` function.
2.  Remove the duplicated `create_template` function.
3.  Remove the duplicated `VERKADA_API_BASE_URL` and `TOKEN_ENDPOINT` constants.
4.  Update the imports to include `get_api_token`, `create_template`, `VERKADA_API_BASE_URL`, and `TOKEN_ENDPOINT` from `src_helix.api_utils`.
5.  Replace the `logging.basicConfig` call with the standardized logging handler configuration (similar to `test_token_api.py`).
6.  Ensure error logging includes `exc_info=True` for tracebacks.
7.  Review for any unused imports after changes.

### `src_helix/test_cameras_api.py`

This file has standardized logging but still contains duplicated functions and constants.

**Steps:**

1.  Remove the duplicated `get_api_token` function.
2.  Remove the duplicated `create_template` function.
3.  Remove the duplicated `VERKADA_API_BASE_URL` and `TOKEN_ENDPOINT` constants.
4.  Update the imports to include `get_api_token`, `create_template`, `VERKADA_API_BASE_URL`, and `TOKEN_ENDPOINT` from `src_helix.api_utils`.
5.  Review for any unused imports after changes.

### `src_helix/test_lpr_images_api.py`

This file has standardized logging but still contains duplicated functions and constants, and a duplicated code block within `fetch_lpr_images_data`.

**Steps:**

1.  Remove the duplicated `get_api_token` function.
2.  Remove the duplicated `create_template` function.
3.  Remove the duplicated `VERKADA_API_BASE_URL` and `TOKEN_ENDPOINT` constants.
4.  Update the imports to include `get_api_token`, `create_template`, `VERKADA_API_BASE_URL`, and `TOKEN_ENDPOINT` from `src_helix.api_utils`.
5.  Remove the duplicated block of code within the `fetch_lpr_images_data` function that sets `url`, `headers`, and `params` a second time.
6.  Review for any unused imports after changes.

### `src_helix/test_lpoi_api.py`

This file has standardized logging but still contains duplicated functions and constants, and unused imports.

**Steps:**

1.  Remove the duplicated `get_api_token` function.
2.  Remove the duplicated `create_template` function.
3.  Remove the duplicated `VERKADA_API_BASE_URL` and `TOKEN_ENDPOINT` constants.
4.  Update the imports to include `get_api_token`, `create_template`, `VERKADA_API_BASE_URL`, and `TOKEN_ENDPOINT` from `src_helix.api_utils`.
5.  Remove the unused `io` and `contextlib` imports.
6.  Review for any other unused imports after changes.

### `src_helix/test_notifications_api.py`
### `src_helix/test_token_api.py`
### `src_helix/test_access_events_api.py`
### `src_helix/test_lpr_timestamps_api.py`

These files appear to have the major cleanup steps completed based on the provided content (duplicated functions/constants removed, imports updated, logging standardized). A final review for minor issues is always recommended.

### `src_helix/runtest.sh`

This script has been updated to use module paths (`python -m src_helix.script_name`), which resolved the import issues. It appears generally clean and functional for its purpose. No further major cleanup steps are immediately identified, but a review for minor improvements (e.g., clearer variable names, more robust input validation) could be considered if desired.

---

**Next Steps:**

Proceed with applying the cleanup steps outlined for each file, starting with `test_users_list_api.py`.
```
