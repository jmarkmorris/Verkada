#!/usr/bin/env python3
"""
Script to test the Verkada Cameras API endpoint.
"""
import os # Import os
import sys
import json
import logging
import requests
import argparse

# Import shared utility functions and constants
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, TOKEN_ENDPOINT

# Get the logger for this module
logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG)

# Define the logs directory path
LOGS_DIR = 'src_helix/logs'

# Add diagnostic prints for directory creation
print(f"DEBUG (cameras): Attempting to create log directory: {LOGS_DIR}", file=sys.stderr)

# Ensure the logs directory exists
try:
    os.makedirs(LOGS_DIR, exist_ok=True)
    print(f"DEBUG (cameras): Log directory created or already exists: {LOGS_DIR}", file=sys.stderr)
except Exception as e:
    print(f"ERROR (cameras): Failed to create log directory {LOGS_DIR}: {e}", file=sys.stderr)
    # Note: We don't exit here, just report the error and continue.


# Create formatters and add them to the handlers
# Define formatter BEFORE the try block where it's used
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter) # Set formatter for stream handler

# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix/logs directory
log_file_path = os.path.join(LOGS_DIR, 'cameras_api_debug.log')

# Add diagnostic prints for file handler creation
print(f"DEBUG (cameras): Attempting to create file handler for: {log_file_path} (Absolute: {os.path.abspath(log_file_path)})", file=sys.stderr)

try:
    file_handler = logging.FileHandler(log_file_path)
    print(f"DEBUG (cameras): File handler created successfully for: {log_file_path}", file=sys.stderr)
    file_handler.setLevel(logging.DEBUG) # Set file handler level to DEBUG
    file_handler.setFormatter(formatter) # Set formatter for file handler

    # Add handlers to the logger
    # Prevent duplicate handlers if the script is somehow imported multiple times
    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        print("DEBUG (cameras): Handlers added to logger.", file=sys.stderr)
    else:
         print("DEBUG (cameras): Logger already has handlers.", file=sys.stderr)

except Exception as e:
    print(f"ERROR (cameras): Failed to create file handler for {log_file_path}: {e}", file=sys.stderr)
    # If file handler creation fails, logging to file won't work.
    # The script will continue, but file logs will be missing.


# Remove the basicConfig call as we are configuring handlers manually
# logging.basicConfig(...)


# VERKADA_API_BASE_URL = "https://api.verkada.com" # Removed, imported from api_utils
# TOKEN_ENDPOINT = "/token" # Removed, imported from api_utils
CAMERAS_ENDPOINT = "/cameras/v1/devices"

# def get_api_token(api_key: str) -> str: # Removed, imported from api_utils
#     """Fetch short-lived API token."""
#     url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
#     headers = {
#         "Accept": "application/json",
#         "x-api-key": api_key,
#     }
#
#     try:
#         # logger.info(f"Requesting token from {url}") # Removed redundant info log
#         logger.debug(f"Requesting token from {url}") # Keep debug log
#         response = requests.post(url, headers=headers)
#         response.raise_for_status()
#         data = response.json()
#         return data['token']
#     except Exception as e:
#         logger.error(f"API token retrieval failed: {e}")
#         raise

# def create_template(data: dict) -> dict: # Removed, imported from api_utils
#     """Recursively create a template dictionary with empty values."""
#     template = {}
#     for key, value in data.items():
#         if isinstance(value, dict):
#             template[key] = create_template(value)
#         elif isinstance(value, list):
#             # For lists, create a list containing one template item if the list is not empty
#             template[key] = [create_template(value[0])] if value else []
#         elif isinstance(value, str):
#             template[key] = ""
#         elif isinstance(value, (int, float)):
#             template[key] = 0
#         elif isinstance(value, bool):
#             template[key] = False # Or None, depending on desired empty state for boolean
#         else:
#             template[key] = None # Handles None and other types
#
#     return template


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
        logger.debug(f"Camera response status code: {response.status_code}") # Added debug log
        logger.debug(f"Camera response headers: {dict(response.headers)}") # Added debug log

        response.raise_for_status()
        data = response.json()

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
        raise
    except Exception as e: # Catch other potential exceptions during fetch/json parsing
        logger.error(f"Unexpected error during camera data fetch: {e}", exc_info=True) # Added traceback
        raise


def _list_cameras_for_menu(api_key: str):
    """
    Fetches cameras and prints them to stdout in 'index,id,name' format
    for use by the runtest.sh script menu. Filters for cameras with 'License' in their name.
    Suppresses standard logging to stdout.
    """
    # We get the logger again here to ensure we have the correct instance
    local_logger = logging.getLogger(__name__)
    temp_stream_handler = None
    # original_level = local_logger.level # Store original level - REMOVED

    # Temporarily remove the stream handler
    # *before* any API calls or printing the marker
    for handler in local_logger.handlers:
        if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
            temp_stream_handler = handler
            local_logger.removeHandler(handler)
            break # Assuming only one StreamHandler for stdout

    # local_logger.setLevel(logging.CRITICAL) # Temporarily set logger level to CRITICAL - REMOVED


    try:
        # Get API token using imported function
        # get_api_token now has debug logging, which goes to the file handler
        api_token = get_api_token(api_key)

        # Fetch camera data (errors will be logged to file by the file handler)
        url = f"{VERKADA_API_BASE_URL}{CAMERAS_ENDPOINT}"
        headers = {
            "Accept": "application/json",
            "x-verkada-auth": api_token,
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        cameras = response.json()

        # These debug logs will now go to the file handler because the logger level is DEBUG
        logger.debug(f"Raw camera response data in _list_for_menu: {cameras}")
        logger.debug(f"Type of data received in _list_for_menu: {type(cameras)}")

        # Filter for cameras with 'name' and 'camera_id' that contain 'License' (case-insensitive)
        all_cameras = [
            cam for cam in cameras.get('cameras', []) # Use .get with default empty list
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
        # Re-add the stream handler and restore original level
        if temp_stream_handler:
            local_logger.addHandler(temp_stream_handler)
        # local_logger.setLevel(original_level) # Restore logger level - REMOVED


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Cameras API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR', # Changed default to ERROR
        help="Set the logging level (default: ERROR)" # Updated help text
    )
    parser.add_argument(
        "--list-for-menu",
        action="store_true",
        help="Fetch and list cameras in a format suitable for the runtest.sh menu"
    )

    # Parse arguments
    args = parser.parse_args()

    # Set logging level for the stream handler based on the argument.
    # The file handler level is already set to DEBUG.
    stream_handler.setLevel(getattr(logging, args.log_level))
    logger.debug(f"Stream handler level set to: {args.log_level}")


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
        # Get API token using imported function
        api_token = get_api_token(api_key)
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
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No cameras found to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
