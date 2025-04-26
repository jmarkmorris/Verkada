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


def get_api_token(api_key: str) -> str:
    """Fetch short-lived API token from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        logger.debug(f"Requesting token from {url} with API key: {api_key[:5]}...{api_key[-4:]}")
        response = requests.post(url, headers=headers)
        logger.debug(f"Token response status code: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        logger.debug(f"Token response data keys: {list(data.keys())}")
        return data['token']
    except Exception as e:
        # This error is now logged to src_helix/logs/api_utils_debug.log
        logger.error(f"API token retrieval failed: {e}")
        logger.error(f"Full exception traceback: {traceback.format_exc()}")
        raise

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
    url = f"{VERKADA_API_BASE_URL}{CAMERAS_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching all camera data from {url}")
        response = requests.get(url, headers=headers)
        logger.debug(f"Cameras response status code: {response.status_code}")
        response.raise_for_status()
        data = response.json()

        logger.debug(f"Raw camera response data: {data}")

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
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error fetching camera list: {e}")
        logger.error(f"Response status code: {e.response.status_code}")
        logger.error(f"Response content: {e.response.content}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error fetching camera list: {e}", exc_info=True)
        raise


def fetch_lpr_images_for_camera(api_token: str, camera_id: str, start_time: int, end_time: int) -> list:
    """
    Fetches LPR images (detections) for a single camera within a time range,
    handling pagination. Returns a list of detection dictionaries.
    """
    url = f"{VERKADA_API_BASE_URL}{LPR_IMAGES_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }
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
            response = requests.get(url, headers=headers, params=params)
            logger.debug(f"LPR images response status code for camera {camera_id}, page {page_count + 1}: {response.status_code}")
            response.raise_for_status()

            # Debug the raw response content length, but not the content itself
            raw_content = response.content
            logger.debug(f"Raw response content length for camera {camera_id}, page {page_count + 1}: {len(raw_content)} bytes")
            # Removed logging of raw_content preview to avoid dumping potential binary data

            try:
                data = response.json()
                logger.debug(f"Response JSON parsed successfully for camera {camera_id}, page {page_count + 1}")
                logger.debug(f"Response data type: {type(data)}")
                if isinstance(data, dict):
                    logger.debug(f"Response data keys: {list(data.keys())}")
                    if 'detections' in data:
                        logger.debug(f"Found 'detections' key with {len(data['detections'])} items for camera {camera_id}, page {page_count + 1}")
                    else:
                        logger.debug(f"'detections' key not found in response for camera {camera_id}, page {page_count + 1}")
                else:
                    logger.debug(f"Response data for camera {camera_id}, page {page_count + 1} is not a dictionary: {type(data)}")
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response for camera {camera_id}, page {page_count + 1}: {e}")
                logger.error(f"Response content: {response.content}")
                # Stop pagination for this camera on JSON error
                break


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

        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error fetching LPR images for camera {camera_id}, page {page_count + 1}: {e}")
            logger.error(f"Response status code: {e.response.status_code}")
            logger.error(f"Response content: {e.response.content}")
            # Decide whether to stop or continue with the next camera on error
            # For now, we'll log and stop fetching for this camera
            break
        except Exception as e:
            logger.error(f"Unexpected error fetching LPR images for camera {camera_id}, page {page_count + 1}: {e}", exc_info=True)
            # Log and stop fetching for this camera
            break

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
