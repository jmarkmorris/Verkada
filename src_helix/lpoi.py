"""
Script to retrieve and print License Plates of Interest from a Verkada organization.
"""
"""
Script to retrieve and print License Plates of Interest from a Verkada organization.
"""
import os
import sys
import logging
import requests
import argparse
from typing import List, Dict, Any

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
LPOI_ENDPOINT = "/cameras/v1/analytics/lpr/license_plate_of_interest"

# Dictionary to map API names to their endpoints and handler functions
API_ENDPOINTS = {
    "lpoi": {
        "endpoint": LPOI_ENDPOINT,
        "handler": "handle_lpoi_api", # Name of the function to call
        "description": "Fetch License Plates of Interest"
    }
    # Add other APIs here as needed
    # "cameras": {
    #     "endpoint": "/cameras/v1/devices",
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


def fetch_api_data(api_token: str, endpoint: str) -> Dict[str, Any]:
    """
    Fetches data from a specified Verkada API endpoint using an API token.

    Args:
        api_token: The short-lived Verkada API Token.
        endpoint: The API endpoint path (e.g., "/cameras/v1/analytics/lpr/license_plate_of_interest").

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

    logger.info(f"Fetching data from {url}")

    try:
        response = requests.get(url, headers=headers)
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


def handle_lpoi_api(api_token: str) -> None:
    """
    Fetches and prints License Plates of Interest.
    """
    try:
        data = fetch_api_data(api_token, LPOI_ENDPOINT)

        if 'license_plate_of_interest' not in data or not isinstance(data['license_plate_of_interest'], list):
            raise ValueError("Unexpected API response format for LPOI: missing or invalid 'license_plate_of_interest' list.")

        lpois = data['license_plate_of_interest']

        if not lpois:
            logger.info("No License Plates of Interest found.")
            return

        logger.info(f"Found {len(lpois)} License Plates of Interest:")
        for lpoi in lpois:
            # Keep printing LPOI details to stdout as it's the script's main output
            # Access dictionary keys based on API response structure
            license_plate = lpoi.get('license_plate', 'N/A')
            description = lpoi.get('description', 'N/A')
            creation_time = lpoi.get('creation_time', 'N/A')

            print(f"  License Plate: {license_plate}")
            print(f"    Description: {description}")
            print(f"    Creation Time: {creation_time}")
            print("-" * 20)

        if 'next_page_token' in data and data['next_page_token']:
            logger.warning("Pagination detected for LPOI. Only the first page of results is being returned.")
            # TODO: Implement full pagination if needed

    except (requests.exceptions.RequestException, ValueError) as e:
        logger.error(f"Failed to handle LPOI API: {e}", exc_info=True)
        raise # Re-raise to be caught by the main error handler


# Add other API handler functions here as needed
# def handle_cameras_api(api_token: str) -> None:
#     """
#     Fetches and prints camera list.
#     """
#     try:
#         data = fetch_api_data(api_token, API_ENDPOINTS["cameras"]["endpoint"])
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
