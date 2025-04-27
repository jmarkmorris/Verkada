#!/usr/bin/env python3
"""
Script to test the Verkada Cameras API endpoint.
Fetches and prints the list of cameras and saves a JSON template.
"""
import os
import sys
import json
import logging
import requests
import argparse

# Import shared utility functions and constants, including configure_logging and save_json_template
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, CAMERAS_ENDPOINT, _fetch_data, configure_logging, save_json_template

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


def fetch_cameras_data(api_token: str):
    """Fetch camera data from Verkada API (first page only)."""
    # Note: This function fetches only the first page.
    # Use fetch_all_cameras from api_utils for full list with pagination.
    try:
        # Use the new _fetch_data function
        data = _fetch_data(api_token, CAMERAS_ENDPOINT, method='GET')

        logger.debug(f"Raw camera response data: {data}") # Added debug log for raw data

        # Print the response in pretty format
        print("\n--- Cameras API Response ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        logger.debug(f"Returning data from fetch_cameras_data: {data}") # Added debug log before return
        return data
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {CAMERAS_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise # Re-raise the exception after logging
    except Exception as e: # Catch other potential exceptions during fetch/json parsing
        logger.error(f"Unexpected error during camera data fetch: {e}", exc_info=True) # Added traceback
        raise # Re-raise the exception


# Removed the _list_cameras_for_menu function


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Cameras API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR',
        help="Set the logging level (default: ERROR)"
    )
    # Removed --list-for-menu argument

    # Parse arguments
    args = parser.parse_args()

    # Configure logging using the centralized function
    configure_logging(args.log_level)

    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)

    # Otherwise, proceed with the standard test script logic
    cameras_data = None # Initialize to None
    try:
        # Get API token using imported function
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch camera data (first page)
        cameras_data = fetch_cameras_data(api_token)
        logger.info("Successfully retrieved camera data (first page)")

        # Debugging the data received and extracted list
        logger.debug(f"Data received in main: {cameras_data}")
        logger.debug(f"Type of data received in main: {type(cameras_data)}")

        # Generate and save JSON template if data is available
        # Get the raw value of the 'cameras' key first for debugging (Corrected key)
        raw_cameras_list = cameras_data.get('cameras')
        logger.debug(f"Raw value of 'cameras' key: {raw_cameras_list}")

        # Extract the list, defaulting to empty list if not found or not a list (Corrected key)
        cameras_list = raw_cameras_list if isinstance(raw_cameras_list, list) else []

        logger.debug(f"Extracted cameras_list in main: {cameras_list}")
        logger.debug(f"Length of cameras_list in main: {len(cameras_list)}")


        if cameras_list:
            logger.debug("cameras_list is not empty, attempting to generate template.") # Added debug log
            # Use the centralized save_json_template function
            output_filename = "src_helix/api-json/test_cameras_api.json"
            # Pass the first item of the list and the key to wrap it with
            save_json_template(cameras_list[0], output_filename, wrap_key="cameras")
        else:
            logger.warning("No cameras found on the first page to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
