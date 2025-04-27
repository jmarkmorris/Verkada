import json
import logging
import requests
import traceback
import sys
import os
import time
import datetime

# Define the logs directory path
LOGS_DIR = 'src_helix/logs'

# Ensure the logs directory exists
# This needs to happen before the file handler is potentially created
os.makedirs(LOGS_DIR, exist_ok=True)

def configure_logging(log_level_str: str = 'ERROR'):
    """
    Configures the root logger with a stream handler and a file handler.
    Removes existing handlers to prevent duplicates if called multiple times.

    Args:
        log_level_str: The desired logging level as a string (e.g., 'DEBUG', 'INFO').
                       Defaults to 'ERROR'.
    """
    # Get the root logger
    root_logger = logging.getLogger()

    # Remove existing handlers to prevent duplicates
    if root_logger.hasHandlers():
        # print("DEBUG: Root logger already has handlers. Removing them.", file=sys.stderr) # Diagnostic print
        root_logger.handlers.clear()
        # print("DEBUG: Root logger handlers cleared.", file=sys.stderr) # Diagnostic print


    # Set the root logger level to DEBUG so it processes all messages
    # Handlers will filter based on their own levels
    root_logger.setLevel(logging.DEBUG)
    # print(f"DEBUG: Root logger level set to DEBUG.", file=sys.stderr) # Diagnostic print


    # Create formatters
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # print("DEBUG: Formatter created.", file=sys.stderr) # Diagnostic print


    # Create handlers
    # Stream handler for stdout - level set by log_level_str argument
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    try:
        stream_handler.setLevel(getattr(logging, log_level_str.upper()))
        # print(f"DEBUG: Stream handler level set to {log_level_str.upper()}.", file=sys.stderr) # Diagnostic print
    except AttributeError:
        print(f"WARNING: Invalid log level string '{log_level_str}'. Defaulting stream handler to ERROR.", file=sys.stderr)
        stream_handler.setLevel(logging.ERROR)
        # print("DEBUG: Stream handler level defaulted to ERROR.", file=sys.stderr) # Diagnostic print


    # File handler for debug logs - always log DEBUG and above to file
    # Save log file in the src_helix/logs directory
    log_file_path = os.path.join(LOGS_DIR, 'debug.log') # Centralized debug log file

    # Create file handler, handling potential errors
    file_handler = None # Initialize file_handler to None
    try:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG) # File handler always logs DEBUG and above
        file_handler.setFormatter(formatter)
        # print(f"DEBUG: File handler created successfully for {log_file_path}.", file=sys.stderr) # Diagnostic print
    except Exception as e:
        # If file handler creation fails, log an error to the console (via stream_handler)
        # and continue without the file handler.
        # Use a temporary logger or print directly if root logger isn't fully set up yet
        print(f"ERROR: Failed to create file handler for {log_file_path}: {e}", file=sys.stderr)
        # print("DEBUG: File handler creation failed.", file=sys.stderr) # Diagnostic print


    # Add handlers to the root logger
    root_logger.addHandler(stream_handler)
    # print("DEBUG: Stream handler added to root logger.", file=sys.stderr) # Diagnostic print
    if file_handler: # Only add if file handler was successfully created
        root_logger.addHandler(file_handler)
        # print("DEBUG: File handler added to root logger.", file=sys.stderr) # Diagnostic print

    # print("DEBUG: Logging configuration complete.", file=sys.stderr) # Diagnostic print


# Get the logger for this module. It will inherit handlers from the root logger.
logger = logging.getLogger(__name__)

# Removed the old logging setup code from here.
# The configure_logging function will be called by the main scripts.


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


def fetch_all_paginated_data(api_token: str, endpoint: str, list_key: str, params: dict = None) -> list:
    """
    Fetches all data from a paginated API endpoint.
    Handles pagination using 'next_page_token'.

    Args:
        api_token: The short-lived API token.
        endpoint: The API endpoint path.
        list_key: The key in the response dictionary that contains the list of items (e.g., 'cameras', 'access_members').
        params: Optional dictionary of initial query parameters.

    Returns:
        A list containing all items from all pages.
    """
    all_items = []
    page_token = None
    page_count = 0
    initial_params = params.copy() if params else {} # Copy initial params

    logger.debug(f"Fetching all data from {endpoint} with list key '{list_key}'")

    while True:
        current_params = initial_params.copy()
        # Only add page_size if the endpoint is NOT the cameras endpoint
        if endpoint != CAMERAS_ENDPOINT:
            current_params["page_size"] = 250 # Use smaller page size for non-camera endpoints
            logger.debug(f"Using page_size=250 for endpoint {endpoint}")
        else:
            logger.debug(f"Not using page_size parameter for endpoint {endpoint}")


        if page_token:
            current_params["page_token"] = page_token
            logger.debug(f"Fetching page {page_count + 1} with page_token: {page_token}")
        else:
             logger.debug(f"Fetching initial page {page_count + 1}")

        try:
            data = _fetch_data(api_token, endpoint, method='GET', params=current_params)

            if isinstance(data, dict):
                current_page_items = data.get(list_key, [])
                if not isinstance(current_page_items, list):
                     logger.warning(f"Expected '{list_key}' list in response for page {page_count + 1}, but got {type(current_page_items)}. Stopping pagination.")
                     break # Stop if the key is not a list

                logger.debug(f"Found '{list_key}' key with {len(current_page_items)} items on page {page_count + 1}")
                all_items.extend(current_page_items)
                logger.debug(f"Added {len(current_page_items)} items from page {page_count + 1}. Total items fetched so far: {len(all_items)}")

                page_token = data.get('next_page_token') # Get next page token from the dictionary
            else:
                logger.warning(f"Response data for page {page_count + 1} is not a dictionary: {type(data)}. Stopping pagination.")
                break # Stop if the response is not a dictionary

            page_count += 1

            if page_token:
                logger.debug(f"Next page token found: {page_token}. Continuing pagination.")
                # Optional: Add a small delay to avoid hitting rate limits
                # time.sleep(0.1)
            else:
                logger.debug(f"No next page token found. Ending pagination.")
                break # No more pages

        except Exception as e:
            # _fetch_data already logged the specific error (HTTP, JSON, etc.)
            # Log a higher-level error here and stop pagination
            logger.error(f"Failed to fetch data from {endpoint}, page {page_count + 1}: {e}")
            break # Stop pagination on any error

    logger.info(f"Finished fetching all data from {endpoint}. Total items fetched: {len(all_items)}")
    return all_items


def fetch_all_access_users(api_token: str) -> list:
    """
    Fetches all access users from the /access/v1/access_users endpoint.
    Handles pagination.
    """
    logger.info("Fetching all access users...")
    return fetch_all_paginated_data(api_token, USERS_LIST_ENDPOINT, 'access_members')


def fetch_all_cameras(api_token: str) -> list:
    """
    Fetches all cameras from the /cameras/v1/devices endpoint.
    Handles pagination.
    """
    logger.info("Fetching all cameras...")
    # This will now call fetch_all_paginated_data without adding page_size
    return fetch_all_paginated_data(api_token, CAMERAS_ENDPOINT, 'cameras')


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
            # and the first item is a dictionary. Otherwise, template the first item directly.
            if value and isinstance(value[0], dict):
                 template[key] = [create_template(value[0])]
            elif value:
                 # Template the first item if it's a primitive type
                 template[key] = [type(value[0])()] if isinstance(value[0], (int, float, str, bool)) else [None]
            else:
                 template[key] = [] # Empty list remains empty
        elif isinstance(value, str):
            template[key] = ""
        elif isinstance(value, bool):
            template[key] = False # Or None, depending on desired empty state for boolean
        elif isinstance(value, (int, float)):
            template[key] = 0
        else:
            template[key] = None # Handles None and other types

    return template

def save_json_template(data_to_template, output_filename: str, wrap_key: str = None):
    """
    Generates a JSON template from provided data and saves it to a file.

    Args:
        data_to_template: The dictionary or list item to template.
        output_filename: The full path including filename to save the template.
        wrap_key: Optional. If provided, the template will be wrapped in a dictionary
                  like {wrap_key: [template_data]} if data_to_template was a list item,
                  or {wrap_key: template_data} if data_to_template was a dictionary.
                  If None, the template_data is saved directly.
    """
    if data_to_template is None:
        logger.warning(f"No data provided to generate template for {output_filename}.")
        return

    try:
        logger.debug(f"Generating JSON template from data type: {type(data_to_template)}")
        template_data = create_template(data_to_template)
        logger.debug(f"Template data created: {template_data}")

        final_output = template_data
        if wrap_key:
            # If wrap_key is provided, wrap the template.
            # Assume if wrap_key is used, the original data was likely a list item
            # that should be represented as a list in the template file.
            final_output = {wrap_key: [template_data]}
            logger.debug(f"Wrapped template data with key '{wrap_key}'")


        # Ensure the output directory exists
        output_dir = os.path.dirname(output_filename)
        os.makedirs(output_dir, exist_ok=True)
        logger.debug(f"Ensured directory exists: {output_dir}")


        logger.debug(f"Writing JSON template to {output_filename}")
        with open(output_filename, 'w') as f:
            json.dump(final_output, f, indent=4, ensure_ascii=False)
        logger.info(f"Generated JSON template: {output_filename}")

    except Exception as e:
        logger.error(f"Failed to generate or write JSON template to {output_filename}: {e}", exc_info=True)


# Moved shared functions from test_lpr_images_api_all_cameras.py
def fetch_lpr_enabled_cameras(api_token: str) -> list:
    """
    Fetches all cameras and filters for those with 'License' in their name.
    Returns a list of camera dictionaries.
    """
    try:
        # Use the new fetch_all_cameras function to get all cameras
        all_cameras = fetch_all_cameras(api_token)

        logger.debug(f"Total cameras fetched in fetch_lpr_enabled_cameras: {len(all_cameras)}")

        # Filter for cameras with 'name' and 'camera_id' that contain 'License' (case-insensitive)
        lpr_cameras = [
            cam for cam in all_cameras
            if isinstance(cam, dict) and 'name' in cam and 'camera_id' in cam and 'license' in cam['name'].lower()
        ]

        logger.info(f"Found {len(lpr_cameras)} LPR-enabled cameras (filtered by 'License' in name).")
        logger.debug(f"LPR-enabled cameras found: {[c.get('name', 'Unnamed') for c in lpr_cameras]}")

        return lpr_cameras
    except Exception as e:
        # fetch_all_cameras already logs the specific error, just re-raise or log a higher-level error
        logger.error(f"Failed to fetch and filter LPR-enabled cameras: {e}")
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

def filter_lpr_by_lpoi(detections: list, lpoi_set: set) -> list:
    """
    Filters a list of LPR detections to include only those whose license plate
    is present in the provided set of License Plates of Interest (LPOI).

    Args:
        detections: A list of LPR detection dictionaries.
        lpoi_set: A set of license plate strings considered LPOI.

    Returns:
        A new list containing only the detections that match an LPOI plate.
    """
    if not isinstance(detections, list):
        logger.warning(f"Invalid input: detections must be a list, got {type(detections)}. Returning empty list.")
        return []
    if not isinstance(lpoi_set, set):
        logger.warning(f"Invalid input: lpoi_set must be a set, got {type(lpoi_set)}. Returning empty list.")
        return []

    logger.debug(f"Filtering {len(detections)} detections against {len(lpoi_set)} LPOI plates.")

    matched_detections = []
    for det in detections:
        # Ensure detection is a dictionary and has 'license_plate'
        if isinstance(det, dict) and 'license_plate' in det:
            if det['license_plate'] in lpoi_set:
                matched_detections.append(det)
        else:
            logger.debug(f"Skipping malformed detection entry during LPOI filtering: {det}")

    logger.debug(f"Found {len(matched_detections)} detections matching LPOI.")
    return matched_detections

def filter_lpr_by_non_lpoi(detections: list, lpoi_set: set) -> list:
    """
    Filters a list of LPR detections to include only those whose license plate
    is *not* present in the provided set of License Plates of Interest (LPOI).

    Args:
        detections: A list of LPR detection dictionaries.
        lpoi_set: A set of license plate strings considered LPOI.

    Returns:
        A new list containing only the detections that do *not* match an LPOI plate.
    """
    if not isinstance(detections, list):
        logger.warning(f"Invalid input: detections must be a list, got {type(detections)}. Returning empty list.")
        return []
    if not isinstance(lpoi_set, set):
        logger.warning(f"Invalid input: lpoi_set must be a set, got {type(lpoi_set)}. Returning empty list.")
        return []

    logger.debug(f"Filtering {len(detections)} detections against {len(lpoi_set)} LPOI plates (Non-LPOI).")

    non_lpoi_detections = []
    for det in detections:
        # Ensure detection is a dictionary and has 'license_plate'
        if isinstance(det, dict) and 'license_plate' in det:
            if det['license_plate'] not in lpoi_set:
                non_lpoi_detections.append(det)
        else:
            logger.debug(f"Skipping malformed detection entry during Non-LPOI filtering: {det}")

    logger.debug(f"Found {len(non_lpoi_detections)} detections not matching LPOI.")
    return non_lpoi_detections


# Example usage if api_utils were run directly (not intended for this project structure)
# if __name__ == '__main__':
#     configure_logging('DEBUG')
#     logger.info("api_utils module started directly.")
#     # Example API call (requires API_KEY env var)
#     # api_key = os.environ.get('API_KEY')
#     # if api_key:
#     #     try:
#     #         token_data = get_api_token(api_key)
#     #         logger.info(f"Successfully got token: {token_data.get('token', 'N/A')[:10]}...")
#     #     except Exception as e:
#     #         logger.error(f"Failed to get token: {e}")
#     # else:
#     #     logger.warning("API_KEY not set, cannot test get_api_token.")

