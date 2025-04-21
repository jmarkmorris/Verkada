"""
Script to retrieve and print License Plates of Interest and their timestamps from a Verkada organization.
"""
import os
import sys
import logging
import requests
import argparse
import datetime
import time
from typing import List, Dict, Any

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Hardcoded list of LPR camera IDs for debugging
HARDCODED_LPR_CAMERA_IDS = [
    "8c219867-9e7a-40e1-b19d-020f7458558c",
    "ab34699a-038b-41b4-98b4-9d83055489b6",
    "f9cd473f-3794-4bee-825c-d1ae60d8e791",
    "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
    "d1e37446-ca48-4398-9243-49a99ea4bc80",
]

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
LPOI_ENDPOINT = "/cameras/v1/analytics/lpr/license_plate_of_interest"
CAMERAS_ENDPOINT = "/cameras/v1/devices"
LPR_TIMESTAMPS_ENDPOINT = "/cameras/v1/analytics/lpr/timestamps"

# Dictionary to map API names to their endpoints and handler functions
API_ENDPOINTS = {
    "lpr_timestamps": {
        "handler": "handle_lpr_timestamps", # Name of the function to call
        "description": "Fetch timestamps for License Plates of Interest across specified cameras"
    }
    # Add other APIs here as needed
    # "cameras": {
    #     "endpoint": CAMERAS_ENDPOINT,
    #     "handler": "handle_cameras_api",
    #     "description": "Fetch Camera List"
    # }
}

def get_api_token(api_key: str) -> str:
    """
    Fetches a short-lived API token using the long-lived API key.

    Args:
        api_key: The long-lived Verkada API Key.

    Returns:
        The short-lived API token string.

    Raises:
        requests.exceptions.RequestException: For network or API errors during token generation.
        ValueError: If the API response format for the token is unexpected.
        KeyError: If the 'token' key is missing in the response.
    """
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    logger.info(f"Fetching API token from {url}")

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        data = response.json()

        if 'token' not in data or not isinstance(data['token'], str):
            raise ValueError("Unexpected API response format for token: missing or invalid 'token' key.")

        logger.info("Successfully fetched API token.")
        return data['token']

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            logger.error("API token request failed: 401 Unauthorized. Please check your API_KEY environment variable.")
        else:
            logger.error(f"API token request failed with HTTP error {e.response.status_code}: {e}")
        raise # Re-raise the exception after logging
    except requests.exceptions.RequestException as e:
        logger.error(f"API token request failed: {e}")
        raise # Re-raise the exception after logging
    except ValueError as e:
        logger.error(f"Failed to parse API token response: {e}")
        raise # Re-raise the exception after logging


def fetch_api_data(api_token: str, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Fetches data from a specified Verkada API endpoint using an API token.

    Args:
        api_token: The short-lived Verkada API Token.
        endpoint: The API endpoint path (e.g., "/cameras/v1/analytics/lpr/license_plate_of_interest").
        params: Optional dictionary of query parameters.

    Returns:
        The JSON response data as a dictionary.
    Raises:
        requests.exceptions.RequestException: For network or API errors.
        ValueError: If the API response is not valid JSON.
    """
    url = f"{VERKADA_API_BASE_URL}{endpoint}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    logger.info(f"Fetching data from {url} with params: {params}")

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

        data = response.json()
        logger.info(f"Successfully fetched data from {url}")
        return data

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            logger.error(f"API request failed: 401 Unauthorized for {url}. The API token may be invalid or expired, or the API Key used to generate it lacks necessary permissions for this endpoint.")
        else:
            logger.error(f"API request failed with HTTP error {e.response.status_code}: {e}")
        raise # Re-raise the exception after logging
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise # Re-raise the exception after logging
    except ValueError as e:
        logger.error(f"Failed to parse API response from {url}: {e}")
        raise # Re-raise the exception after logging


def handle_lpr_timestamps(api_token: str, history_days: int, use_hardcoded_cameras: bool) -> None:
    """
    Fetches License Plates of Interest, then fetches camera list (or uses hardcoded list),
    and finally fetches and prints timestamps for each LPOI on each camera
    within the specified history days.

    Args:
        api_token: The short-lived Verkada API Token.
        history_days: The number of days of history to query for timestamps.
        use_hardcoded_cameras: Boolean flag to use the hardcoded camera list instead of fetching from API.
    """
    try:
        # Calculate start and end time based on history_days
        end_time = int(time.time())
        start_time = end_time - (history_days * 24 * 60 * 60)
        logger.info(f"Querying LPR timestamps for the last {history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")


        # 1. Fetch License Plates of Interest
        lpoi_data = fetch_api_data(api_token, LPOI_ENDPOINT)

        if 'license_plate_of_interest' not in lpoi_data or not isinstance(lpoi_data['license_plate_of_interest'], list):
            raise ValueError("Unexpected API response format for LPOI: missing or invalid 'license_plate_of_interest' list.")

        lpois = lpoi_data['license_plate_of_interest']

        if not lpois:
            logger.info("No License Plates of Interest found in the organization.")
            return

        unique_license_plates = list(set(lpoi.get('license_plate') for lpoi in lpois if lpoi.get('license_plate')))
        logger.info(f"Found {len(unique_license_plates)} unique License Plates of Interest.")

        # 2. Get Camera List (from API or hardcoded)
        if use_hardcoded_cameras:
            camera_ids = HARDCODED_LPR_CAMERA_IDS
            logger.info(f"Using hardcoded list of {len(camera_ids)} LPR camera IDs.")
            if not camera_ids:
                 logger.warning("Hardcoded camera list is empty. Cannot fetch LPR timestamps.")
                 return
        else:
            # Note: This fetches ALL cameras. The LPR timestamps endpoint only works for LPR-enabled cameras.
            # A more robust solution would filter cameras based on LPR capability if the camera endpoint provided that info.
            camera_data = fetch_api_data(api_token, CAMERAS_ENDPOINT)

            if 'cameras' not in camera_data or not isinstance(camera_data['cameras'], list):
                 raise ValueError("Unexpected API response format for Cameras: missing or invalid 'cameras' list.")

            cameras = camera_data.get('cameras', []) # Use .get with default to handle missing key gracefully

            if not cameras:
                logger.warning("No cameras found in the organization using the /cameras/v1/devices endpoint. Please ensure your API Key has 'Read' permissions for the Camera API.")
                # Log the full response even if the cameras list is empty, for debugging
                logger.debug(f"Full response from /cameras/v1/devices: {camera_data}")
                return

            camera_ids = [camera.get('id') for camera in cameras if camera.get('id')]
            logger.info(f"Found {len(camera_ids)} cameras from API.")


        # 3. Fetch and print timestamps for each LPOI on each camera
        logger.info("Fetching timestamps for each LPOI on each camera...")
        any_detections_found_overall = False

        for license_plate in unique_license_plates:
            detections_found_for_plate = False
            plate_timestamps = [] # Collect timestamps for the current plate across all cameras

            for camera_id in camera_ids:
                try:
                    logger.info(f"Querying timestamps for {license_plate} on camera {camera_id}")
                    timestamp_params = {
                        "license_plate": license_plate,
                        "camera_id": camera_id,
                        "page_size": 200, # Max page size for this endpoint
                        "start_time": start_time,
                        "end_time": end_time
                    }

                    timestamp_data = fetch_api_data(api_token, LPR_TIMESTAMPS_ENDPOINT, params=timestamp_params)

                    # Log the raw response data for debugging if no detections are found
                    if 'detections' not in timestamp_data or not isinstance(timestamp_data['detections'], list):
                         logger.warning(f"Unexpected API response format for timestamps for {license_plate} on camera {camera_id}: {timestamp_data}. Skipping.")
                         continue

                    detections = timestamp_data['detections']

                    if detections:
                        detections_found_for_plate = True
                        any_detections_found_overall = True
                        plate_timestamps.extend([(camera_id, timestamp) for timestamp in detections])

                        if 'next_page_token' in timestamp_data and timestamp_data['next_page_token']:
                            logger.warning(f"Pagination detected for timestamps for {license_plate} on camera {camera_id}. Only the first page of results is being returned.")
                            # TODO: Implement full pagination for timestamps if needed
                    else:
                        logger.info(f"  No detections found for {license_plate} on camera {camera_id} in the specified time range.")
                        # Log the full response even if detections list is empty, for debugging
                        logger.debug(f"Full response for {license_plate} on camera {camera_id} with no detections: {timestamp_data}")

                except (requests.exceptions.RequestException, ValueError) as e:
                    logger.error(f"Failed to fetch timestamps for {license_plate} on camera {camera_id}: {e}", exc_info=True)
                    # Continue to the next camera/plate even if one fails

            # Print timestamps for the current plate if any were found across all cameras
            if detections_found_for_plate:
                print(f"\n--- Timestamps for License Plate: {license_plate} ---")
                for cam_id, timestamp in plate_timestamps:
                     print(f"  Camera ID: {cam_id}, Timestamp: {timestamp} ({datetime.datetime.fromtimestamp(timestamp)})")
                print("-" * 20)


        if not any_detections_found_overall:
            logger.info(f"No LPR detections found for any of the License Plates of Interest in the last {history_days} days across the specified cameras.")


    except (requests.exceptions.RequestException, ValueError) as e:
        logger.error(f"Failed during LPR timestamps processing: {e}", exc_info=True)
        raise # Re-raise to be caught by the main error handler


# Add other API handler functions here as needed
# def handle_cameras_api(api_token: str) -> None:
#     """
#     Fetches and prints camera list.
#     """
#     try:
#         data = fetch_api_data(api_token, CAMERAS_ENDPOINT)
#         # Process and print camera data
#         print("Camera data (first page):", data)
#         if 'next_page_token' in data and data['next_page_token']:
#             logger.warning("Pagination detected for Cameras. Only the first page of results is being returned.")
#             # TODO: Implement full pagination if needed
#     except (requests.exceptions.RequestException, ValueError) as e:
#         logger.error(f"Failed to handle Cameras API: {e}", exc_info=True)
#         raise # Re-raise to be caught by the main error handler


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query various Verkada API endpoints.")
    parser.add_argument(
        "--api",
        choices=API_ENDPOINTS.keys(),
        required=True,
        help="Specify which Verkada API to query."
    )
    parser.add_argument(
        "--history_days",
        type=int,
        default=1, # Default to 1 day of history
        help="Number of days of history to query for LPR timestamps (default: 1)."
    )
    parser.add_argument(
        "--use_hardcoded_cameras",
        action="store_true", # This flag doesn't need a value, just its presence matters
        help="Use a hardcoded list of LPR camera IDs instead of fetching from the API."
    )

    args = parser.parse_args()

    try:
        api_key = os.environ.get("API_KEY")
        if not api_key:
            raise KeyError("API_KEY environment variable not set.")

        # First, get the API token
        api_token = get_api_token(api_key)

        # Get the handler function based on the chosen API
        api_info = API_ENDPOINTS.get(args.api)
        if not api_info:
             # This should not happen due to argparse choices, but as a safeguard
            logger.error(f"Unknown API specified: {args.api}")
            sys.exit(1)

        handler_function_name = api_info["handler"]
        handler_function = globals().get(handler_function_name)

        if handler_function and callable(handler_function):
            # Pass the appropriate arguments based on the handler function's signature
            if args.api == "lpr_timestamps":
                 handler_function(api_token, args.history_days, args.use_hardcoded_cameras)
            # Add conditions here for other APIs if they require different arguments
            # elif args.api == "cameras":
            #      handler_function(api_token)
            else:
                 # Default case for handlers that only need the api_token
                 handler_function(api_token)
        else:
            logger.error(f"Handler function not found or not callable for API: {args.api} ({handler_function_name})")
            sys.exit(1)


    except KeyError as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1) # Exit with a non-zero status code to indicate an error
    except (requests.exceptions.RequestException, ValueError) as e:
        # Specific API or data errors are already logged in the handler functions
        # This catches any exceptions re-raised from handlers or other unexpected errors
        logger.error(f"Operation failed: {e}", exc_info=True)
        sys.exit(1) # Exit with a non-zero status code to indicate an error
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True) # Log exception details
        sys.exit(1) # Exit with a non-zero status code to indicate an error
