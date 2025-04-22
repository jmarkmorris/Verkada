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
from typing import List, Dict, Any, Callable

# Configure basic logging (level will be set by argparse later)
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Ensure logging goes to stdout
        logging.FileHandler('lpoi_debug.log')  # Add file logging for debugging
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
LPOI_ENDPOINT = "/cameras/v1/analytics/lpr/license_plate_of_interest"
LPR_IMAGES_ENDPOINT = "/cameras/v1/analytics/lpr/imagesview" # Endpoint to get seen license plates
ALERTS_ENDPOINT = "/cameras/v1/notifications" # Endpoint to get alerts
ACCESS_EVENTS_ENDPOINT = "/access/v1/events" # Alternative endpoint for events

# Dictionary to map API names to their endpoints and handler functions
API_ENDPOINTS = {
    "lpr_events": {
        "handler": "handle_lpr_events", # Name of the function to call
        "description": "Fetch LPR events for License Plates of Interest"
    },
    "alerts": {
        "handler": "handle_alerts_api",
        "description": "Fetch alerts using the notifications endpoint"
    },
    "access_events": {
        "handler": "handle_access_events",
        "description": "Fetch access events"
    }
    # Add other APIs here as needed
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

def handle_alerts_api(api_token: str, history_days: int) -> None:
    """
    Attempts to fetch alerts or access events using alternative endpoints.

    Args:
        api_token: The short-lived Verkada API Token.
        history_days: The number of days of history to query for events.
    """
    try:
        # Calculate start and end time based on history_days
        end_time = int(time.time())
        start_time = end_time - (history_days * 24 * 60 * 60)
        logger.info(f"Querying events for the last {history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")

        # Try multiple endpoints in case of permission issues
        endpoints_to_try = [
            ("/access/v1/events", "access_events"),
            ("/cameras/v1/notifications", "camera_notifications"),
            ("/cameras/v1/analytics/lpr/imagesview", "lpr_images")
        ]

        for endpoint, endpoint_name in endpoints_to_try:
            try:
                logger.info(f"Attempting to fetch events from {endpoint}...")

                all_events = []
                page_token = None

                while True:
                    events_params = {
                        "start_time": start_time,
                        "end_time": end_time,
                        "page_size": 200 # Max page size for this endpoint
                    }
                    if page_token:
                        events_params["page_token"] = page_token

                    try:
                        events_data = fetch_api_data(api_token, endpoint, params=events_params)
                    except requests.exceptions.HTTPError as http_err:
                        logger.warning(f"Failed to fetch from {endpoint}: {http_err}")
                        break  # Try next endpoint or continue to next iteration

                    # Dynamically determine the events list key based on the endpoint
                    events_key = 'events' if endpoint == "/access/v1/events" else \
                                 'notifications' if endpoint == "/cameras/v1/notifications" else \
                                 'license_plates'

                    if events_key not in events_data or not isinstance(events_data[events_key], list):
                        logger.warning(f"Unexpected API response format for {endpoint_name}: missing or invalid '{events_key}' list. Raw data: {events_data}. Stopping pagination.")
                        break

                    events_page = events_data[events_key]
                    all_events.extend(events_page)

                    page_token = events_data.get('next_page_token')
                    if not page_token:
                        break  # Stop if there are no more pages

                    logger.info(f"Fetched {len(events_page)} {endpoint_name} events, fetching next page with token: {page_token}")

                # If we successfully fetched events, print and return
                if all_events:
                    logger.info(f"Fetched a total of {len(all_events)} {endpoint_name} events within the specified time range.")

                    print(f"\n--- {endpoint_name.upper()} Events ---")
                    for event in all_events:
                        print(f"  Event: {event}")
                        print("-" * 20)
                    return

            except Exception as e:
                logger.warning(f"Error fetching from {endpoint}: {e}")
                continue

        # If no events were found in any endpoint
        logger.info(f"No events found in the last {history_days} days from any attempted endpoint.")
        print("No events found. This could be due to API permission issues or no events during the specified time range.")

    except Exception as e:
        logger.error(f"Failed during events processing: {e}", exc_info=True)
        raise  # Re-raise to be caught by the main error handler

def main():
    """
    Main entry point for the script. Parses command-line arguments and calls the appropriate API handler.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Verkada API Query Script")
    parser.add_argument(
        "--api", 
        choices=list(API_ENDPOINTS.keys()), 
        required=True, 
        help="The API endpoint to query"
    )
    parser.add_argument(
        "--history_days", 
        type=int, 
        default=7, 
        help="Number of days of history to query (default: 7)"
    )
    parser.add_argument(
        "--log_level", 
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], 
        default='INFO', 
        help="Set the logging level (default: INFO)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Set logging level
    logging.getLogger().setLevel(getattr(logging, args.log_level))

    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set. Please set it before running the script.")
        sys.exit(1)

    try:
        # Get API token
        api_token = get_api_token(api_key)

        # Find and call the appropriate handler function dynamically
        api_name = args.api
        handler_name = API_ENDPOINTS[api_name]['handler']
        
        # Use globals() to dynamically find the function by its name
        handler_func = globals().get(handler_name)
        
        if not handler_func or not callable(handler_func):
            logger.error(f"Handler function not found or not callable for API: {api_name} ({handler_name})")
            logger.error(f"Available global functions: {list(globals().keys())}")
            raise ValueError(f"Handler function not found or not callable for API: {api_name} ({handler_name})")

        # Call the handler function with API token and history days
        handler_func(api_token, args.history_days)

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
