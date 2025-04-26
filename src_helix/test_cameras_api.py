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

# Import shared utility functions and constants, including configure_logging
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, CAMERAS_ENDPOINT, _fetch_data, configure_logging

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


def fetch_cameras_data(api_token: str):
    """Fetch camera data from Verkada API."""
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


def _list_cameras_for_menu(api_key: str):
    """
    Fetches cameras and prints them to stdout in 'index,id,name' format
    for use by the runtest.sh script menu. Filters for cameras with 'License' in their name.
    Suppresses standard logging to stdout.
    """
    # We get the logger again here to ensure we have the correct instance
    local_logger = logging.getLogger(__name__)
    temp_stream_handler = None

    # Temporarily remove the stream handler
    # *before* any API calls or printing the marker
    for handler in local_logger.handlers:
        if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
            temp_stream_handler = handler
            local_logger.removeHandler(handler)
            break # Assuming only one StreamHandler for stdout

    try:
        # Get API token using imported function
        # get_api_token now has debug logging, which goes to the file handler
        # It returns the full data, extract the token string
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")


        # Fetch camera data using the new _fetch_data function
        # Errors will be logged to file by the file handler via _fetch_data
        data = _fetch_data(api_token, CAMERAS_ENDPOINT, method='GET')

        # These debug logs will now go to the file handler because the logger level is DEBUG
        logger.debug(f"Raw camera response data in _list_for_menu: {data}")
        logger.debug(f"Type of data received in _list_for_menu: {type(data)}")

        # Filter for cameras with 'name' and 'camera_id' that contain 'License' (case-insensitive)
        all_cameras = [
            cam for cam in data.get('cameras', []) # Use .get with default empty list
            if isinstance(cam, dict) and 'name' in cam and 'camera_id' in cam and 'license' in cam['name'].lower()
        ]

        logger.debug(f"Extracted cameras_list in _list_for_menu: {all_cameras}")
        logger.debug(f"Length of cameras_list in _list_for_menu: {len(all_cameras)}")

        # Add a marker to indicate the start of the parsable output
        # Print directly to stdout, bypassing the logger
        print("---START_CAMERA_LIST---", file=sys.stdout)
        sys.stdout.flush() # Flush the marker immediately

        # Print cameras in a parsable format: index,id,name
        # Print nothing if the list is empty
        for i, cam in enumerate(all_cameras):
            # Clean the camera name to remove any commas that could break parsing
            clean_name = cam['name'].replace(',', ' ')
            # Use 'camera_id' when printing
            print(f"{i+1},{cam['camera_id']},{clean_name}", file=sys.stdout) # Print camera lines
        sys.stdout.flush() # Explicitly flush stdout after printing the list

    except Exception as e:
        # Log the error to the file handler
        logger.error(f"Error listing cameras for menu: {e}", exc_info=True)
        sys.exit(1) # Exit with non-zero status on error
    finally:
        # Re-add the stream handler
        if temp_stream_handler:
            local_logger.addHandler(temp_stream_handler)


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
    parser.add_argument(
        "--list-for-menu",
        action="store_true",
        help="Fetch and list cameras in a format suitable for the runtest.sh menu"
    )

    # Parse arguments
    args = parser.parse_args()

    # Configure logging using the centralized function
    configure_logging(args.log_level)

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
    cameras_data = None # Initialize to None
    try:
        # Get API token using imported function
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch camera data
        cameras_data = fetch_cameras_data(api_token)
        logger.info("Successfully retrieved camera data")

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
            template_data = create_template(cameras_list[0]) # Use imported function
            logger.debug(f"Template data created: {template_data}") # Added debug log for template data
            # Wrap in the expected list structure using the correct key 'cameras'
            template_output = {"cameras": [template_data]}

            # Save the template to the src_helix/api-json directory
            output_filename = "src_helix/api-json/test_cameras_api.json"
            logger.debug(f"Writing template to {output_filename}")
            try:
                with open(output_filename, 'w') as f:
                    json.dump(template_output, f, indent=4)
                logger.info(f"Generated JSON template: {output_filename}")
            except Exception as write_e:
                logger.error(f"Failed to write JSON template to {output_filename}: {write_e}", exc_info=True)
        else:
            logger.warning("No cameras found to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
