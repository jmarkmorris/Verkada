import json
import logging
import requests
import traceback
import sys
import os
import time
import datetime

logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG)

# Define the logs directory path
LOGS_DIR = 'src_helix/logs'

# Ensure the logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create handlers for the api_utils logger
# Stream handler for stdout (optional, but useful for immediate feedback)
# Level will be set based on the calling script's configuration if propagation is enabled,
# or can be set here if needed. Let's set it to WARNING by default for this handler.
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter) # Set formatter for stream handler
stream_handler.setLevel(logging.WARNING) # Default stream level for api_utils

# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix/logs directory
log_file_path = os.path.join(LOGS_DIR, 'api_utils_debug.log')

# Create file handler, handling potential errors
try:
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG) # File handler always logs DEBUG and above
    file_handler.setFormatter(formatter) # Set formatter for file handler

    # Add handlers to the logger
    # Prevent duplicate handlers if the module is somehow imported multiple times
    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

except Exception as e:
    # If file handler creation fails, log an error to the console (via stream_handler)
    # and continue without the file handler.
    logger.error(f"Failed to create file handler for {log_file_path}: {e}")


VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
CAMERAS_ENDPOINT = "/cameras/v1/devices" # Added Cameras endpoint
LPR_IMAGES_ENDPOINT = "/cameras/v1/analytics/lpr/images" # Added LPR Images endpoint
LPOI_ENDPOINT = "/cameras/v1/analytics/lpr/license_plate_of_interest" # Added LPOI endpoint
USERS_LIST_ENDPOINT = "/access/v1/access_users" # Added Users List endpoint
USER_DETAILS_ENDPOINT = "/access/v1/access_users/user" # Added User Details endpoint
NOTIFICATIONS_ENDPOINT = "/cameras/v1/alerts" # Added Notifications endpoint
ACCESS_EVENTS_ENDPOINT = "/events/v1/access" # Added Access Events endpoint
LPR_TIMESTAMPS_ENDPOINT = "/cameras/v1/analytics/lpr/timestamps" # Added LPR Timestamps endpoint


def _fetch_data(api_token: str = None, endpoint: str = None, method: str = 'GET', params: dict = None, headers: dict = None, base_url: str = VERKADA_API_BASE_URL) -> dict:
    """
    Internal helper function to fetch data from a Verkada API endpoint.
    Handles request, status check, JSON parse, and basic logging.

    Args:
        api_token: The short-lived API token (used for x-verkada-auth). Optional if custom headers are provided.
        endpoint: The API endpoint path (e.g., "/cameras/v1/devices"). Required.
        method: The HTTP method ('GET' or 'POST'). Defaults to 'GET'.
        params: Dictionary of query parameters or request body data (depending on method and API).
        headers: Dictionary of request headers. If None, uses standard x-verkada-auth header with api_token.
        base_url: The base URL for the API. Defaults to VERKADA_API_BASE_URL.

    Returns:
        The parsed JSON response data as a dictionary.

    Raises:
        ValueError: If endpoint is None or method is unsupported.
        requests.exceptions.RequestException: For HTTP errors or other request issues.
        json.JSONDecodeError: If the response content is not valid JSON.
        Exception: For other unexpected errors.
    """
    if endpoint is None:
        raise ValueError("Endpoint must be provided.")

    url = f"{base_url}{endpoint}"
    request_headers = {
        "Accept": "application/json",
    }
    if headers:
        request_headers.update(headers)
    elif api_token: # Only add x-verkada-auth if token is provided and no custom headers
         request_headers["x-verkada-auth"] = api_token

    logger.debug(f"Fetching data from {url} using {method}")
    logger.debug(f"Request headers: {request_headers}")
    logger.debug(f"Request parameters: {params}")
    # Avoid logging the full token/key unless in DEBUG mode, and even then, maybe truncate
    if api_token and 'x-verkada-auth' in request_headers:
         logger.debug(f"Using API token: {api_token[:10]}...")
    elif headers and 'x-api-key' in headers:
         logger.debug(f"Using API key: {headers['x-api-key'][:10]}...")


    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=request_headers, params=params)
        elif method.upper() == 'POST':
            # Assuming POST requests might send params as query parameters or form data
            # If JSON body is needed, this function would need adjustment (json=params)
            response = requests.post(url, headers=request_headers, params=params)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        logger.debug(f"Response status code from {endpoint}: {response.status_code}")
        logger.debug(f"Response headers from {endpoint}: {dict(response.headers)}")

        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

        # Debug the raw response content length
        raw_content = response.content
        logger.debug(f"Raw response content length from {endpoint}: {len(raw_content)} bytes")

        data = response.json()
        logger.debug(f"Response JSON parsed successfully from {endpoint}")
        logger.debug(f"Response data type from {endpoint}: {type(data)}")
        # Log keys for dict responses
        if isinstance(data, dict):
            logger.debug(f"Response data keys from {endpoint}: {list(data.keys())}")

        return data

    except requests.exceptions.RequestException as e:
        # requests.exceptions.RequestException is the base class for all requests exceptions
        # including HTTPError, ConnectionError, Timeout, etc.
        # Specific HTTPError details are logged within the except block in the calling script
        # if needed, or can be extracted from the exception object here.
        # Let's log the basic error here and re-raise.
        logger.error(f"Request Exception fetching data from {endpoint}: {e}")
        # Re-raise the exception after logging
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON response from {endpoint}: {e}")
        # Attempt to log response content if available and not too large
        try:
            logger.error(f"Response content: {response.text[:500]}...") # Log first 500 chars
        except Exception:
            logger.error("Could not log response content.")
        # Re-raise the exception after logging
        raise
    except Exception as e:
        logger.error(f"Unexpected error fetching data from {endpoint}: {e}", exc_info=True)
        # Re-raise the exception after logging
        raise


def get_api_token(api_key: str) -> dict:
    """
    Fetch short-lived API token from Verkada API.
    Returns the full response dictionary containing the 'token'.
    """
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        # Use the internal fetch function, providing custom headers
        data = _fetch_data(endpoint=TOKEN_ENDPOINT, method='POST', headers=headers)
        logger.debug(f"Token response data keys: {list(data.keys())}")
        # Return the full data dictionary, not just the token string
        return data
    except Exception as e:
        # _fetch_data already logs the specific error
        logger.error(f"API token retrieval failed: {e}")
        raise # Re-raise the exception


def create_template(data: dict) -> dict:
    """Recursively create a template dictionary with empty values."""
    template = {}
    for key, value in data.items():
        if isinstance(value, dict):
            template[key] = create_template(value)
        elif isinstance(value, list):
            # For lists, create a list containing one template item if the list is not empty
            template[key] = [create_template(value[0])] if value else []
        elif isinstance(value, str):
            template[key] = ""
        elif isinstance(value, (int, float)):
            template[key] = 0
        elif isinstance(value, bool):
            template[key] = False # Or None, depending on desired empty state for boolean
        else:
            template[key] = None # Handles None and other types

    return template

# Moved shared functions from test_lpr_images_api_all_cameras.py
def fetch_lpr_enabled_cameras(api_token: str) -> list:
    """
    Fetches all cameras and filters for those with 'License' in their name.
    Returns a list of camera dictionaries.
    """
    try:
        # Use the new _fetch_data function
        data = _fetch_data(api_token, CAMERAS_ENDPOINT, method='GET')

        logger.debug(f"Raw camera response data in fetch_lpr_enabled_cameras: {data}")
        logger.debug(f"Type of data received in fetch_lpr_enabled_cameras: {type(data)}")

        # Extract the list of cameras, defaulting to empty list if not found or not a list
        all_cameras = data.get('cameras')
        if not isinstance(all_cameras, list):
             logger.warning(f"Expected 'cameras' list in response, but got {type(all_cameras)}. Returning empty list.")
             return []

        # Filter for cameras with 'name' and 'camera_id' that contain 'License' (case-insensitive)
        lpr_cameras = [
            cam for cam in all_cameras
            if isinstance(cam, dict) and 'name' in cam and 'camera_id' in cam and 'license' in cam['name'].lower()
        ]

        logger.info(f"Found {len(lpr_cameras)} LPR-enabled cameras (filtered by 'License' in name).")
        logger.debug(f"LPR-enabled cameras found: {[c.get('name', 'Unnamed') for c in lpr_cameras]}")

        return lpr_cameras
    except Exception as e:
        # _fetch_data already logs the specific error, just re-raise or log a higher-level error
        logger.error(f"Failed to fetch LPR-enabled cameras: {e}")
        raise # Re-raise the exception


def fetch_lpr_images_for_camera(api_token: str, camera_id: str, start_time: int, end_time: int) -> list:
    """
    Fetches LPR images (detections) for a single camera within a time range,
    handling pagination. Returns a list of detection dictionaries.
    """
    all_detections = []
    page_token = None
    page_count = 0

    logger.debug(f"Fetching LPR images for camera ID: {camera_id} from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)}")

    while True:
        params = {
            "camera_id": camera_id,
            "start_time": start_time,
            "end_time": end_time,
            "page_size": 200 # Max page size
        }
        if page_token:
            params["page_token"] = page_token
            logger.debug(f"Fetching page {page_count + 1} with page_token: {page_token}")
        else:
             logger.debug(f"Fetching initial page for camera ID: {camera_id}")

        try:
            # Use the new _fetch_data function
            data = _fetch_data(api_token, LPR_IMAGES_ENDPOINT, method='GET', params=params)

            # The API response structure for /images is a dictionary with 'camera_id', 'detections', 'next_page_token'
            detections = data.get('detections', []) if isinstance(data, dict) else []
            if not isinstance(detections, list):
                 logger.warning(f"Expected 'detections' list in response for camera {camera_id}, page {page_count + 1}, but got {type(detections)}. Stopping pagination for this camera.")
                 break # Stop if detections is not a list

            all_detections.extend(detections)
            logger.debug(f"Added {len(detections)} detections from page {page_count + 1}. Total detections so far: {len(all_detections)}")

            page_token = data.get('next_page_token') if isinstance(data, dict) else None
            page_count += 1

            if page_token:
                logger.debug(f"Next page token found: {page_token}. Continuing pagination for camera {camera_id}.")
                # Optional: Add a small delay to avoid hitting rate limits
                # time.sleep(0.1)
            else:
                logger.debug(f"No next page token found. Ending pagination for camera {camera_id}.")
                break # No more pages

        except Exception as e:
            # _fetch_data already logs the specific error (HTTP, JSON, etc.)
            # Log a higher-level error here and stop pagination for this camera
            logger.error(f"Failed to fetch LPR images for camera {camera_id}, page {page_count + 1}: {e}")
            break # Stop pagination for this camera on any error

    logger.info(f"Finished fetching LPR images for camera {camera_id}. Total detections: {len(all_detections)}")
    return all_detections


def format_timestamp(unix_timestamp: int) -> str:
    """Converts a Unix timestamp (seconds) to a human-readable string."""
    try:
        dt_object = datetime.datetime.fromtimestamp(unix_timestamp)
        return dt_object.strftime('%Y-%m-%d %H:%M:%S')
    except (TypeError, ValueError) as e:
        logger.warning(f"Could not format timestamp {unix_timestamp}: {e}")
        return str(unix_timestamp) # Return original value or error indicator
