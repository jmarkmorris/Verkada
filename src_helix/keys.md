# Potential Foreign Key Relationships in Verkada API Test Data

This document analyzes the structure of the provided JSON sample files to identify potential relationships between different API endpoints, based on common field names that might serve as foreign keys.

**Note:** This analysis is based solely on the structure and naming conventions observed in the sample JSON data. The actual relationships and constraints are defined by the Verkada API itself.

---

## Identified Potential Relationships:

Based on the sample data, the following potential foreign key relationships are observed:

1.  **`test_users_list_api.json` (`access_members`) to `test_user_details_api.json` (Root Object)**
    *   **Relationship:** One-to-One or One-to-Many (a user listed in the list endpoint corresponds to their details in the details endpoint).
    *   **Potential Key:** `user_id`
    *   **Description:** The `user_id` field in each object within the `access_members` list in `test_users_list_api.json` appears to uniquely identify a user. This same `user_id` field is present at the root level of the `test_user_details_api.json` structure, suggesting it's the key to retrieve details for a specific user.
    *   **Relationship:** `test_users_list_api.json`.`access_members[*].user_id` = `test_user_details_api.json`.`user_id`

2.  **`test_cameras_api.json` (`cameras`) to `test_lpr_timestamps_api.json` (Request Parameter)**
    *   **Relationship:** One-to-Many (one camera can have many LPR timestamps).
    *   **Potential Key:** `camera_id`
    *   **Description:** The `camera_id` field in each object within the `cameras` list in `test_cameras_api.json` uniquely identifies a camera. The `test_lpr_timestamps_api.py` script requires a `camera_id` as a parameter to fetch timestamps, implying that timestamps are associated with a specific camera.
    *   **Relationship:** `test_cameras_api.json`.`cameras[*].camera_id` -> `test_lpr_timestamps_api` (via `camera_id` request parameter)

3.  **`test_cameras_api.json` (`cameras`) to `test_notifications_api.json` (Implicit/Contextual)**
    *   **Relationship:** One-to-Many (one camera can generate many notifications).
    *   **Potential Key:** `camera_id` (likely present within notification details, though not explicitly shown in the top-level `test_notifications_api.json` sample which is just a list of notifications).
    *   **Description:** Notifications are typically associated with a specific device like a camera. While the sample `test_notifications_api.json` doesn't show the camera ID at the top level, it's highly probable that a `camera_id` field exists within each notification object, linking it back to a camera from the `test_cameras_api.json` list.
    *   **Potential Relationship:** `test_cameras_api.json`.`cameras[*].camera_id` = `test_notifications_api.json`.`notifications[*].camera_id` (assuming `camera_id` exists within notification objects)

4.  **`test_cameras_api.json` (`cameras`) to `test_lpr_images_api.json` (Implicit/Contextual)**
    *   **Relationship:** One-to-Many (one camera can capture many LPR images/events).
    *   **Potential Key:** `camera_id` (likely present within LPR image/event details).
    *   **Description:** Similar to notifications, LPR images/events are tied to the camera that captured them. A `camera_id` field is expected within each LPR event object in the `test_lpr_images_api.json` response.
    *   **Potential Relationship:** `test_cameras_api.json`.`cameras[*].camera_id` = `test_lpr_images_api.json`.[*].`camera_id` (assuming `camera_id` exists within LPR image/event objects)

5.  **`test_users_list_api.json` (`access_members`) or `test_user_details_api.json` to `test_access_events_api.json` (Implicit/Contextual)**
    *   **Relationship:** One-to-Many (one user can generate many access events).
    *   **Potential Key:** `user_id` (likely present within access event details).
    *   **Description:** Access events (like door unlocks) are performed by users. An `user_id` field is expected within each event object in the `test_access_events_api.json` response, linking it back to a user from the user list or details.
    *   **Potential Relationship:** (`test_users_list_api.json`.`access_members[*].user_id` OR `test_user_details_api.json`.`user_id`) = `test_access_events_api.json`.`events[*].user_id` (assuming `user_id` exists within event objects)

---

## Summary of Potential Keys:

*   `user_id`: Appears to link user list/details to access events.
*   `camera_id`: Appears to link camera list to LPR timestamps, notifications, and LPR images/events.
*   `license_plate`: Appears in `test_lpr_timestamps_api.py` (as a parameter) and `test_lpoi_api.json`. This could link specific LPR events/timestamps to the list of license plates of interest.

This analysis provides a starting point for understanding how data from different Verkada API endpoints might be related.
```
