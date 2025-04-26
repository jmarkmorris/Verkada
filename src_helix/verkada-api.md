# Verkada API Endpoints and Test Scripts (`src_helix/`)

This document lists Verkada API endpoints relevant to this project, particularly those with corresponding test scripts in the `src_helix/` directory.

---

## API Endpoints

This section lists Verkada API endpoints that return JSON text-based information, suitable for querying with scripts.

### Endpoints with Existing Test Scripts

The following endpoints have corresponding test scripts in the `src_helix/` directory, runnable via `runtest.sh`:

1.  **`POST /token`**: Get API Token.
    *   *Script:* `test_token_api.py`
    *   *Purpose:* Exchanges API Key for a short-lived API Token.
    *   *Documentation:* [API Login](https://apidocs.verkada.com/reference/postloginapikeyviewv2)

2.  **`GET /cameras/v1/analytics/lpr/license_plate_of_interest`**: Get All License Plates of Interest.
    *   *Script:* `test_lpoi_api.py`
    *   *Purpose:* Retrieves the configured LPOI list.
    *   *Documentation:* [Get All License Plates of Interest](https://apidocs.verkada.com/reference/getlicenseplateofinterestviewv1)
    *   *Note:* API response key is `license_plate_of_interest`.

3.  **`GET /cameras/v1/devices`**: Get Camera Data.
    *   *Script:* `test_cameras_api.py`
    *   *Purpose:* Retrieves a list of cameras in the organization.
    *   *Documentation:* Implicitly covered in Camera API section.
    *   *Note:* API response key is `cameras`.

4.  **`GET /notifications/v1/cameras`**: Get Alerts/Notifications.
    *   *Script:* `test_notifications_api.py`
    *   *Purpose:* Retrieves camera-related notifications within a time range.
    *   *Documentation:* [Get Alerts](https://apidocs.verkada.com/reference/getnotificationsviewv1)
    *   *Note:* API response key is `notifications`. **Corrected endpoint path.**

5.  **`GET /events/v1/access`**: Get Access Events.
    *   *Script:* `test_access_events_api.py`
    *   *Purpose:* Retrieves access control events (door unlocks, etc.) within a time range.
    *   *Documentation:* [Get Access Events](https://apidocs.verkada.com/reference/geteventsviewv1)
    *   *Note:* API response key is `events`.

6.  **`GET /access/v1/access_users`**: Get All Access Users.
    *   *Script:* `test_users_list_api.py`
    *   *Purpose:* Retrieves a list of all users configured for access control.
    *   *Documentation:* [Get All Access Users](https://apidocs.verkada.com/reference/getaccessmembersviewv1)
    *   *Note:* API response key is `access_members`.

7.  **`GET /access/v1/access_users/user`**: Get Access Information Object.
    *   *Script:* `test_user_details_api.py`
    *   *Purpose:* Retrieves detailed information for a specific access user (requires `user_id` or `external_id`).
    *   *Documentation:* [Get Access Information Object](https://apidocs.verkada.com/reference/getaccessuserviewv1)

8.  **`GET /cameras/v1/analytics/lpr/timestamps`**: Get Timestamps for a specific License Plate.
    *   *Script:* `test_lpr_timestamps_api.py`
    *   *Purpose:* Retrieves timestamps when a specific license plate was seen (requires `license_plate` and `camera_id` parameters).
    *   *Documentation:* [Get Timestamps for a specific License Plate](https://apidocs.verkada.com/reference/getlprtimestampsviewv1)
    *   *Note:* API response is a dictionary containing a `detections` key, which holds the list of timestamp/detection events.

9.  **`GET /cameras/v1/analytics/lpr/images`**: Get seen license plates (All LPR Cameras).
    *   *Script:* `test_lpr_images_api_all_cameras.py`
    *   *Purpose:* Fetches LPR detection events for *all* LPR-enabled cameras within a time range and displays them in a table.
    *   *Documentation:* [Get seen license plates](https://apidocs.verkada.com/reference/getlprimagesview)
    *   *Note:* This script iterates through LPR-enabled cameras found via `/cameras/v1/devices`.

10. **`GET /cameras/v1/analytics/lpr/images`**: Get seen license plates (LPOI Match Report).
    *   *Script:* `test_lpr_lpoi_match_api.py`
    *   *Purpose:* Fetches LPR detection events for all LPR-enabled cameras within a time range and filters for matches against the LPOI list.
    *   *Documentation:* [Get seen license plates](https://apidocs.verkada.com/reference/getlprimagesview)
    *   *Note:* This script combines data from `/cameras/v1/analytics/lpr/license_plate_of_interest` and `/cameras/v1/analytics/lpr/images`.

11. **`GET /cameras/v1/analytics/lpr/images`**: Get seen license plates (Non-LPOI Report).
    *   *Script:* `test_lpr_non_lpoi_report_api.py`
    *   *Purpose:* Fetches LPR detection events for all LPR-enabled cameras within a time range and filters for detections that *do not* match any plate in the LPOI list.
    *   *Documentation:* [Get seen license plates](https://apidocs.verkada.com/reference/getlprimagesview)
    *   *Note:* This script combines data from `/cameras/v1/analytics/lpr/license_plate_of_interest` and `/cameras/v1/analytics/lpr/images`.

12. **`GET /cameras/v1/analytics/lpr/images`**: Get seen license plates (Hourly Report).
    *   *Script:* `test_lpr_hourly_report_api.py`
    *   *Purpose:* Fetches LPR detection events for all LPR-enabled cameras within a time range, categorizes them as LPOI or Non-LPOI, and provides an hourly count breakdown.
    *   *Documentation:* [Get seen license plates](https://apidocs.verkada.com/reference/getlprimagesview)
    *   *Note:* This script combines data from `/cameras/v1/analytics/lpr/license_plate_of_interest` and `/cameras/v1/analytics/lpr/images`.

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

When fetching large amounts of data, particularly when paginating through results from endpoints like `/notifications/v1/cameras`, you may encounter API rate limits. If you receive `429 Too Many Requests` errors, consider adding a small delay (e.g., `time.sleep(0.1)`) between API calls, especially between fetching subsequent pages of results.

---

## Verkada API Authentication

The test scripts follow the recommended two-factor authentication flow:

1.  A long-lived **API Key** (stored securely as an environment variable `API_KEY`) is used to request a short-lived **API Token** from the `/token` endpoint.
2.  The **API Token** is then used in the `x-verkada-auth` header for subsequent calls to other API endpoints.

Ensure your `API_KEY` environment variable is set correctly and that the corresponding API Key in Verkada Command has the necessary permissions for the endpoints being queried.
