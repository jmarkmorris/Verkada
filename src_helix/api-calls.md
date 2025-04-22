# Verkada API Query Script (`src_helix/`)

**Goal:** Provide a command-line script to query various Verkada API endpoints, specifically focusing on retrieving License Plate Recognition (LPR) data.

**Functionality:**
*   Authenticates with the Verkada API using a two-step process (API Key to get API Token).
*   Supports querying different API endpoints via command-line flags.
*   Currently implements fetching License Plates of Interest (LPOIs) and LPR events.
*   Handles pagination for LPR events.
*   Allows specifying the history duration for LPR event queries.

**Technology Stack:**
*   Python 3.x
*   `requests` (for making HTTP requests)
*   `argparse` (for command-line arguments)
*   Standard libraries: `os`, `sys`, `logging`, `datetime`, `time`

---

## API Endpoints

This section lists Verkada API endpoints that return JSON text-based information, suitable for querying with scripts.

### Endpoints with Existing Test Scripts

The following endpoints have corresponding test scripts in the `src_helix/` directory:

1.  **`POST /token`**: Get API Token.
    *   *Script:* `test_token_api.py`
    *   *Purpose:* Exchanges API Key for a short-lived API Token.
    *   *Documentation:* [API Login](https://apidocs.verkada.com/reference/postloginapikeyviewv2)

2.  **`GET /cameras/v1/analytics/lpr/license_plate_of_interest`**: Get All License Plates of Interest.
    *   *Script:* `test_lpoi_api.py`
    *   *Purpose:* Retrieves the configured LPOI list.
    *   *Documentation:* [Get All License Plates of Interest](https://apidocs.verkada.com/reference/getlicenseplateofinterestviewv1)

3.  **`GET /cameras/v1/devices`**: Get Camera Data.
    *   *Script:* `test_cameras_api.py`
    *   *Purpose:* Retrieves a list of cameras in the organization.
    *   *Documentation:* Implicitly covered in Camera API section.

4.  **`GET /cameras/v1/analytics/lpr/imagesview`**: Get seen license plates.
    *   *Script:* `test_lpr_images_api.py`
    *   *Purpose:* Retrieves LPR detection events within a time range.
    *   *Documentation:* [Get seen license plates](https://apidocs.verkada.com/reference/getlprimagesview)
    *   *Note:* Requires specific Camera API Read permissions. Failed with 403 error in testing until permissions were granted.

5.  **`GET /cameras/v1/notifications`**: Get Alerts/Notifications.
    *   *Script:* `test_notifications_api.py`
    *   *Purpose:* Retrieves camera-related notifications within a time range.
    *   *Documentation:* [Get Alerts](https://apidocs.verkada.com/reference/getnotificationsviewv1)
    *   *Note:* Requires specific Camera API Read permissions. Failed with 403 error in testing until permissions were granted.

6.  **`GET /access/v1/events`**: Get Access Events.
    *   *Script:* `test_access_events_api.py`
    *   *Purpose:* Retrieves access control events (door unlocks, etc.) within a time range.
    *   *Documentation:* [Get Access Events](https://apidocs.verkada.com/reference/geteventsviewv1)
    *   *Note:* Requires specific Access API Read permissions. Failed with 403 error in testing until permissions were granted.

7.  **`GET /access/v1/access_users`**: Get All Access Users.
    *   *Script:* `test_users_list_api.py`
    *   *Purpose:* Retrieves a list of all users configured for access control.
    *   *Documentation:* [Get All Access Users](https://apidocs.verkada.com/reference/getaccessmembersviewv1)
    *   *Note:* API response key is `access_members`.

8.  **`GET /access/v1/access_users/user`**: Get Access Information Object.
    *   *Script:* `test_user_details_api.py`
    *   *Purpose:* Retrieves detailed information for a specific access user (requires `user_id` or `external_id`).
    *   *Documentation:* [Get Access Information Object](https://apidocs.verkada.com/reference/getaccessuserviewv1)

9.  **`GET /cameras/v1/analytics/lpr/timestamps`**: Get Timestamps for a specific License Plate.
    *   *Script:* `test_lpr_timestamps_api.py`
    *   *Purpose:* Retrieves timestamps when a specific license plate was seen (requires `license_plate` parameter).
    *   *Documentation:* [Get Timestamps for a specific License Plate](https://apidocs.verkada.com/reference/getlprtimestampsviewv1)

### Potential Future Endpoints for Testing

The following endpoints also return JSON data and could be implemented with test scripts:

**Access API:**
*   `GET /access/v1/access_groups`: Get All Access Groups.
*   `GET /access/v1/access_groups/{group_id}`: Get a specific Access Group.
*   `GET /access/v1/access_levels`: Get All Available Access Levels.
*   `GET /access/v1/access_levels/{level_id}`: Get a specific Access Level.
*   `GET /access/v1/doors`: Get Doors information.
*   `GET /access/v1/door_exception_calendars`: Get All Available Door Exception Calendars.
*   `GET /access/v1/door_exception_calendars/{calendar_id}`: Get a specific Door Exception Calendar.
*   `GET /access/v1/door_exception_calendars/{calendar_id}/exceptions/{exception_id}`: Get a specific Exception on a Door Exception Calendar.

**Camera API:**
*   `GET /cameras/v1/analytics/people/person_of_interest`: Get All Persons of Interest.
*   `GET /cameras/v1/analytics/lpr/timestamps`: Get Timestamps for a specific License Plate (requires `license_plate` parameter).
*   `GET /cameras/v1/audio`: Get Camera Audio Status (may require `camera_id`).
*   `GET /cameras/v1/cloud_backup`: Get cloud backup settings for a camera (requires `camera_id`).
*   `GET /cameras/v1/analytics/occupancy_trends/cameras`: Get Occupancy Trends Cameras.
*   `GET /cameras/v1/analytics/occupancy_trends`: Get Occupancy Trend Data (likely requires parameters).
*   `GET /cameras/v1/analytics/object_counts`: Get People/Vehicle Counts (likely requires parameters).
*   `GET /cameras/v1/analytics/max_object_counts`: Get Max People/Vehicle Counts (likely requires parameters).
*   `GET /cameras/v1/analytics/dashboard_occupancy_trends`: Get Dashboard Occupancy Trend Data (likely requires parameters).

**Core API:**
*   `GET /core/v1/audit_logs`: Get Audit Logs (likely requires time parameters).
*   `GET /core/v1/users/{user_id}`: Get User (Core user, requires core `user_id`).

**Sensor API:**
*   `GET /sensors/v1/alerts`: Get Sensor Alerts (likely requires time parameters).
*   `GET /sensors/v1/data`: Get Sensor Data (likely requires sensor IDs and time parameters).

**Guest API:**
*   `GET /guest/v1/sites`: Get Guest Sites.
*   `GET /guest/v1/visits`: Get Guest visits (likely requires time parameters).

**Alarms API:**
*   `GET /alarms/v1/devices`: Get Alarm Devices.
*   `GET /alarms/v1/sites`: Get Site Information (for Alarms).

**Viewing Station API:**
*   `GET /viewing_station/v1/devices`: Get Viewing Station Devices.

**Helix API:**
*   `GET /helix/v1/events/{event_id}`: Get a Helix Event.
*   `GET /helix/v1/event_types`: Get List of Helix Event Types.

*Note: Accessing many of these endpoints may require specific API Key permissions and parameters.*

---

## API Rate Limiting

When fetching large amounts of data, particularly when paginating through results from endpoints like `/cameras/v1/analytics/lpr/imagesview`, you may encounter API rate limits. If you receive `429 Too Many Requests` errors, consider adding a small delay (e.g., `time.sleep(0.1)`) between API calls, especially between fetching subsequent pages of results.

---

## Verkada API Authentication

The script follows the recommended two-factor authentication flow:

1.  A long-lived **API Key** (stored securely as an environment variable `API_KEY`) is used to request a short-lived **API Token** from the `/token` endpoint.
2.  The **API Token** is then used in the `x-verkada-auth` header for subsequent calls to other API endpoints (like fetching LPOIs or LPR events).

Ensure your `API_KEY` environment variable is set correctly and that the corresponding API Key in Verkada Command has the necessary permissions for the endpoints being queried (at least "Read-only access" for the Camera API for the current functionality).

---

## Script Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    # Replace <your-repo-url> with the actual repository URL
    cd Verkada # Assuming project root is Verkada
    ```

2.  **Create and activate a virtual environment:**
    *   It's recommended to create a separate environment for the script:
        ```bash
        python3 -m venv venv_helix
        ```
    *   Activate it:
        ```bash
        # On macOS/Linux:
        source venv_helix/bin/activate
        # On Windows:
        # venv_helix\Scripts\activate
        ```
    *   Your terminal prompt should now be prefixed (e.g., `(venv_helix)`).

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.md # Assuming requirements.md lists 'requests'
    ```
    *   *Note:* The `requirements.md` file should contain the necessary dependencies, including `requests`. If not, you might need to manually install `requests` (`pip install requests`).

4.  **Set Environment Variable (`API_KEY`):**
    *   Obtain your Verkada API Key from Verkada Command (**Admin** -> **Integrations** -> **API**).
    *   Set the `API_KEY` environment variable in your terminal session:
        ```bash
        export API_KEY="YOUR_VERKADA_API_KEY"
        ```
    *   *Note:* For persistent environment variables, consult your operating system's documentation (e.g., add to `.bashrc`, `.zshrc`, or system environment variables).

---

## Script Usage

The script is run from the command line, specifying the API to query and other options.

1.  **Activate Virtual Environment:** Ensure your `venv_helix` virtual environment is activated.
2.  **Run the Script:**
    *   Navigate to the project's root directory (`Verkada`) in your terminal.
    *   Execute the script using the `src_helix` module, specifying the API:
        ```bash
        # Example: Fetch LPR events for LPOIs with 7 days of history
        python -m src_helix.lpoi --api lpr_events --history_days 7 --log_level INFO
        ```
    *   Replace `lpr_events` with the desired API name if more handlers are added to `src_helix/lpoi.py`.
    *   Adjust `--history_days` to specify the time range for LPR event queries.
    *   Adjust `--log_level` (DEBUG, INFO, WARNING, ERROR, CRITICAL) for desired logging verbosity. Use `DEBUG` to see detailed request/response information.

