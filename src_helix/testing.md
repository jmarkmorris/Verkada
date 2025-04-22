**Note:** Before running any tests, ensure your Verkada API key is set as an environment variable:
```bash
export API_KEY="your_verkada_api_key"
```

---

Here are the command lines to test each of the API endpoints using the provided scripts:

### `/token`

*   **Script:** `src_helix/test_token_api.py`
*   **Command:**
    ```bash
    python src_helix/test_token_api.py --log_level INFO
    ```

### `/cameras/v1/analytics/lpr/license_plate_of_interest`

*   **Script:** `src_helix/test_lpoi_api.py`
*   **Command:**
    ```bash
    python src_helix/test_lpoi_api.py --log_level INFO
    ```

### `/cameras/v1/devices`

*   **Script:** `src_helix/test_cameras_api.py`
*   **Command:**
    ```bash
    python src_helix/test_cameras_api.py --log_level INFO
    ```

### `/cameras/v1/analytics/lpr/imagesview`

*   **Script:** `src_helix/test_lpr_images_api.py`
*   **Commands:**
    a.  Test with default 7 days of history:
        ```bash
        python src_helix/test_lpr_images_api.py --log_level INFO
        ```
    b.  Test with a custom history period (e.g., 3 days):
        ```bash
        python src_helix/test_lpr_images_api.py --history_days 3 --log_level INFO
        ```

### `/cameras/v1/notifications`

*   **Script:** `src_helix/test_notifications_api.py`
*   **Commands:**
    a.  Test with default 7 days of history:
        ```bash
        python src_helix/test_notifications_api.py --log_level INFO
        ```
    b.  Test with a custom history period (e.g., 14 days):
        ```bash
        python src_helix/test_notifications_api.py --history_days 14 --log_level INFO
        ```

### `/access/v1/events`

*   **Script:** `src_helix/test_access_events_api.py`
*   **Commands:**
    a.  Test with default 7 days of history:
        ```bash
        python src_helix/test_access_events_api.py --log_level INFO
        ```
    b.  Test with a custom history period (e.g., 14 days):
        ```bash
        python src_helix/test_access_events_api.py --history_days 14 --log_level INFO
        ```

### `/access/v1/access_users`

*   **Script:** `src_helix/test_users_list_api.py`
*   **Command:**
    ```bash
    python src_helix/test_users_list_api.py --log_level INFO
    ```

### `/access/v1/access_users/user`

*   **Script:** `src_helix/test_user_details_api.py`
*   **Commands:**
    a.  Test fetching details for the first user (index 0):
        ```bash
        python src_helix/test_user_details_api.py --log_level INFO
        ```
    b.  Test fetching details for a specific user index (e.g., the third user, index 2):
        ```bash
        python src_helix/test_user_details_api.py --user_index 2 --log_level INFO
        ```

---

For more detailed logging, you can change `--log_level INFO` to `--log_level DEBUG` in any of these commands.
