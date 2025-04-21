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

# Configure basic logging (level will be set by argparse later)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
LPOI_ENDPOINT = "/cameras/v1/analytics/lpr/license_plate_of_interest"
LPR_IMAGES_ENDPOINT = "/cameras/v1/analytics/lpr/imagesview" # Endpoint to get seen license plates

# Dictionary to map API names to their endpoints and handler functions
API_ENDPOINTS = {
    "lpr_events": {
        "handler": "handle_lpr_events", # Name of the function to call
        "description": "Fetch LPR events for License Plates of Interest"
    }
    # Add other APIs here as needed
    # "cameras": {
    #     "endpoint": "/cameras/v1/devices", # Keep endpoint definition if needed for other handlers
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
        elif e.response.status_code == 403:
             logger.error(f"API request failed: 403 Forbidden for {url}. The API Key used to generate the token likely lacks the necessary permissions for this endpoint.")
        else:
            logger.error(f"API request failed with HTTP error {e.response.status_code}: {e}")
        raise # Re-raise the exception after logging
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise # Re-raise the exception after logging
    except ValueError as e:
        logger.error(f"Failed to parse API response from {url}: {e}")
        raise # Re-raise the exception after logging


def handle_lpr_events(api_token: str, history_days: int) -> None:
    """
    Fetches License Plates of Interest, then fetches LPR events using the
    /cameras/v1/analytics/lpr/imagesview endpoint within the specified history days,
    filters for LPOI events, and prints their details.

    Args:
        api_token: The short-lived Verkada API Token.
        history_days: The number of days of history to query for events.
    """
    try:
        # Calculate start and end time based on history_days
        end_time = int(time.time())
        start_time = end_time - (history_days * 24 * 60 * 60)
        logger.info(f"Querying LPR events for the last {history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")

        # 1. Fetch License Plates of Interest
        lpoi_data = fetch_api_data(api_token, LPOI_ENDPOINT)

        if 'license_plate_of_interest' not in lpoi_data or not isinstance(lpoi_data['license_plate_of_interest'], list):
            raise ValueError("Unexpected API response format for LPOI: missing or invalid 'license_plate_of_interest' list.")

        lpois = lpoi_data['license_plate_of_interest']

        if not lpois:
            logger.info("No License Plates of Interest found in the organization.")
            return

        unique_lpoi_plates = {lpoi.get('license_plate') for lpoi in lpois if lpoi.get('license_plate')}
        logger.info(f"Found {len(unique_lpoi_plates)} unique License Plates of Interest.")

        # 2. Fetch LPR Events using /cameras/v1/analytics/lpr/imagesview with pagination
        all_lpr_events = []
        page_token = None
        lpr_events_endpoint = LPR_IMAGES_ENDPOINT

        logger.info(f"Fetching LPR events from {lpr_events_endpoint}...")

        while True:
            lpr_params = {
                "start_time": start_time,
                "end_time": end_time,
                "page_size": 200 # Max page size for this endpoint
            }
            if page_token:
                lpr_params["page_token"] = page_token

            lpr_data = fetch_api_data(api_token, lpr_events_endpoint, params=lpr_params)

            if 'license_plates' not in lpr_data or not isinstance(lpr_data['license_plates'], list):
                 logger.warning(f"Unexpected API response format for LPR events from {lpr_events_endpoint}: missing or invalid 'license_plates' list. Raw data: {lpr_data}. Stopping pagination.")
                 break # Stop fetching if the format is unexpected

            lpr_events_page = lpr_data['license_plates']
            all_lpr_events.extend(lpr_events_page)

            page_token = lpr_data.get('next_page_token')
            if not page_token:
                break # Stop if there are no more pages

            logger.info(f"Fetched {len(lpr_events_page)} events, fetching next page with token: {page_token}")
            # Consider adding a small delay here to avoid hitting rate limits, especially with many pages
            # time.sleep(0.1)


        logger.info(f"Fetched a total of {len(all_lpr_events)} LPR events within the specified time range.")

        # 3. Filter LPR events for those matching LPOIs
        lpoi_lpr_events = [
            event for event in all_lpr_events
            if event.get('license_plate') in unique_lpoi_plates
        ]

        if not lpoi_lpr_events:
            logger.info(f"No LPR events found for any of the License Plates of Interest in the last {history_days} days.")
            return

        logger.info(f"Found {len(lpoi_lpr_events)} LPR events matching License Plates of Interest.")

        # 4. Print details of matching events
        print("\n--- LPR Events for License Plates of Interest ---")
        for event in lpoi_lpr_events:
            license_plate = event.get('license_plate', 'N/A')
            camera_id = event.get('camera_id', 'N/A')
            timestamp = event.get('timestamp', 'N/A')
            image_url = event.get('image_url', 'N/A') # The imagesview endpoint includes image_url

            print(f"  License Plate: {license_plate}")
            print(f"    Camera ID: {camera_id}")
            if isinstance(timestamp, int):
                 print(f"    Timestamp: {timestamp} ({datetime.datetime.fromtimestamp(timestamp)})")
            else:
                 print(f"    Timestamp: {timestamp}")
            print(f"    Image URL: {image_url}")
            print("-" * 20)


    except (requests.exceptions.RequestException, ValueError) as e:
        logger.error(f"Failed during LPR events processing: {e}", exc_info=True)
        raise # Re-raise to be caught by the main error handler


# Add other API handler functions here as needed
# def handle_cameras_api(api_token: str) -> None:
#     """
#     Fetches and prints camera list.
#     """
#     try:
#         data = fetch_api_data(api_token, "/cameras/v1/devices") # Use the endpoint constant if defined globally
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
        help="Number of days of history to query for LPR events (default: 1)."
    )
    parser.add_argument(
        "--log_level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO)."
    )

    args = parser.parse_args()

    # Set the logging level based on the command-line argument for the root logger
    log_level = getattr(logging, args.log_level.upper(), logging.INFO)
    logging.getLogger().setLevel(log_level)
    # Also set the level for the module logger explicitly
    logger.setLevel(log_level)


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
            if args.api == "lpr_events": # Updated API name
                 handler_function(api_token, args.history_days)
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
        "--log_level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO)."
    )

    args = parser.parse_args()

    # Set the logging level based on the command-line argument for the root logger
    log_level = getattr(logging, args.log_level.upper(), logging.INFO)
    logging.getLogger().setLevel(log_level)
    # Also set the level for the module logger explicitly
    logger.setLevel(log_level)


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
                 handler_function(api_token, args.history_days)
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
