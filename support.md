# Verkada API Support Request - 403 Forbidden for LPR Images Endpoint

**Date:** 2025-04-21

**Subject:** Experiencing 403 Forbidden error when accessing `/cameras/v1/analytics/lpr/imagesview` despite having Camera API Read permissions.

**Description of Problem:**

We are developing a script to retrieve License Plate Recognition (LPR) events for our configured License Plates of Interest (LPOIs) using the Verkada API.

Our script successfully performs the following steps:
1.  Uses a long-lived API Key to obtain a short-lived API Token from the `/token` endpoint.
2.  Uses the API Token to successfully fetch the list of License Plates of Interest from the `/cameras/v1/analytics/lpr/license_plate_of_interest` endpoint.
3.  Uses the API Token to successfully fetch the list of cameras from the `/cameras/v1/devices` endpoint.

However, when the script attempts to fetch LPR events using the `/cameras/v1/analytics/lpr/imagesview` endpoint (with `start_time`, `end_time`, and `page_size` parameters), the API consistently returns a `403 Client Error: Forbidden`.

**Troubleshooting Performed:**

We have taken the following steps to troubleshoot this issue:
1.  **Verified API Key Permissions:** We have logged into Verkada Command and confirmed that the API Key being used has "Read-only access" enabled for the "Camera API" product line. According to the API documentation, "Read-only access" should be sufficient for GET endpoints like `/cameras/v1/analytics/lpr/imagesview`.
2.  **Tested with Different Keys:** We have generated and tested with a new API Key that has "Read/Write access" enabled for the "Camera API". This key also receives the same `403 Forbidden` error for the `/cameras/v1/analytics/lpr/imagesview` endpoint.
3.  **Confirmed Other Endpoints Work:** As noted above, the same API Keys successfully access other Camera API GET endpoints (`/cameras/v1/analytics/lpr/license_plate_of_interest` and `/cameras/v1/devices`). This indicates the API Key and Token generation process is working correctly, and the key has general Camera API Read access.
4.  **Reviewed Documentation:** We have reviewed the API documentation for `/cameras/v1/analytics/lpr/imagesview` and the general API Security Overview, and we believe having Camera API Read access should grant permission to this endpoint.

**Request for Assistance:**

We are unable to determine why access to the `/cameras/v1/analytics/lpr/imagesview` endpoint is being forbidden despite the API Key having the required Camera API Read permissions.

Could you please investigate this issue and provide guidance on:
*   Whether there are any specific or additional permissions required for the `/cameras/v1/analytics/lpr/imagesview` endpoint beyond standard Camera API Read access?
*   Any known issues or configurations that might cause a 403 error for this endpoint under these circumstances?
*   How to ensure our API Key is correctly authorized to access this endpoint.

Thank you for your time and assistance.

**Relevant Information:**
*   Endpoint: `GET https://api.verkada.com/cameras/v1/analytics/lpr/imagesview`
*   HTTP Status Code Received: `403 Forbidden`
*   API Key Permissions: Verified as having at least "Read-only access" for "Camera API" in Verkada Command.
*   Other Camera API GET endpoints are accessible with the same key.
```
