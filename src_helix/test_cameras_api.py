#!/usr/bin/env python3
"""
Script to test the Verkada Cameras API endpoint.
"""
import os
import sys
import json
import logging
import requests
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('cameras_api_debug.log')
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
CAMERAS_ENDPOINT = "/cameras/v1/devices"

def get_api_token(api_key: str) -> str:
    """Fetch short-lived API token."""
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['token']
    except Exception as e:
        logger.error(f"API token retrieval failed: {e}")
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


def fetch_cameras_data(api_token: str):
    """Fetch camera data from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{CAMERAS_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching camera data from {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Print the response in pretty format
        print("\n--- Cameras API Response ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {CAMERAS_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise

def _list_cameras_for_menu(api_key: str):
    """
    Fetches cameras and prints them to stdout in 'index,id,name' format
    for use by the runtest.sh script menu. Suppresses standard logging to stdout.
    """
    # Temporarily disable stream handler to prevent logs from interfering with stdout
    root_logger = logging.getLogger()
    stream_handler = None
    for handler in root_logger.handlers:
        if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
            stream_handler = handler
            root_logger.removeHandler(handler)
            break # Assuming only one StreamHandler for stdout

    try:
        # Get API token
        api_token = get_api_token(api_key)

        # Fetch camera data (errors will be logged to file by fetch_cameras_data)
        url = f"{VERKADA_API_BASE_URL}{CAMERAS_ENDPOINT}"
        headers = {
            "Accept": "application/json",
            "x-verkada-auth": api_token,
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        cameras = response.json()

        # Filter for cameras with 'name' and 'id'
        all_cameras = [
            cam for cam in cameras.get('devices', []) # Use .get with default empty list
            if isinstance(cam, dict) and 'name' in cam and 'id' in cam
        ]

        # Print cameras in a parsable format: index,id,name
        # Print nothing if the list is empty
        for i, cam in enumerate(all_cameras):
            # Clean the camera name to remove any commas that could break parsing
            clean_name = cam['name'].replace(',', ' ')
            print(f"{i+1},{cam['id']},{clean_name}")
        sys.stdout.flush() # Explicitly flush stdout after printing the list

    except Exception as e:
        # Log the error to the file handler
        logger.error(f"Error listing cameras for menu: {e}", exc_info=True)
        sys.exit(1) # Exit with non-zero status on error
    finally:
        # Re-add the stream handler
        if stream_handler:
            root_logger.addHandler(stream_handler)


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Cameras API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO',
        help="Set the logging level (default: INFO)"
    )
    parser.add_argument(
        "--list-for-menu",
        action="store_true",
        help="Fetch and list cameras in a format suitable for the runtest.sh menu"
    )

    # Parse arguments
    args = parser.parse_args()

    # Set logging level
    logging.getLogger().setLevel(getattr(logging, args.log_level))

    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)

    # If --list-for-menu is set, run the helper function and exit
    if args.list_for_menu:
        _list_cameras_for_menu(api_key)
        sys.exit(0) # Exit successfully after listing

    # Otherwise, proceed with the standard test script logic
    try:
        # Get API token
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch camera data
        cameras_data = fetch_cameras_data(api_token)
        logger.info("Successfully retrieved camera data")

        # Generate and save JSON template if data is available
        cameras_list = cameras_data.get('devices', []) if isinstance(cameras_data, dict) else []
        if cameras_list:
            template_data = create_template(cameras_list[0])
            template_output = {"devices": [template_data]} # Wrap in the expected list structure

            # Save the template to the src_helix directory
            output_filename = "src_helix/test_cameras_api.json"
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No cameras found to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
