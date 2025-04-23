#!/usr/bin/env python3
"""
Script to test the Verkada LPR Timestamps API endpoint.
Fetches timestamps (returned under the 'detections' key) for a specific license plate.
Saves a JSON template of the expected response structure to a file.
"""
import os
import sys
import json
import logging
import requests
import argparse
import time
import datetime
import traceback

# Import shared utility functions
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL

# Get the logger for this module
logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG)

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix directory
file_handler = logging.FileHandler('src_helix/lpr_timestamps_api_debug.log')
file_handler.setLevel(logging.DEBUG)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
# Prevent duplicate handlers if the script is somehow imported multiple times
if not logger.handlers:
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


LPR_TIMESTAMPS_ENDPOINT = "/cameras/v1/analytics/lpr/timestamps" # Endpoint for timestamps


def fetch_lpr_timestamps_data(api_token: str, camera_id: str, license_plate: str, history_days: int):
    """Fetch LPR timestamps data (detections) for a specific license plate from Verkada API."""
    end_time = int(time.time())
    start_time = end_time - (history_days * 24 * 60 * 60)

    url = f"{VERKADA_API_BASE_URL}{LPR_TIMESTAMPS_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    params = {
        "camera_id": camera_id, # camera_id is a required parameter
        "license_plate": license_plate,
        "start_time": start_time,
        "end_time": end_time,
        "page_size": 100 # Re-adding page_size, trying a smaller value
    }

    try:
        logger.info(f"Fetching LPR timestamps (detections) for plate '{license_plate}' on camera '{camera_id}' from {url} for the last {history_days} days")
        logger.debug(f"Request headers: {headers}")
        logger.debug(f"Request parameters: {params}")
        logger.debug(f"Using API token: {api_token[:10]}...")
        logger.debug(f"Date range: {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)}")

        response = requests.get(url, headers=headers, params=params)
        logger.debug(f"LPR timestamps response status code: {response.status_code}")
        logger.debug(f"LPR timestamps response headers: {dict(response.headers)}")

        response.raise_for_status()

        # Debug the raw response content length, but not the content itself
        raw_content = response.content
        logger.debug(f"Raw response content length: {len(raw_content)} bytes")
        # Removed logging of raw_content preview to avoid dumping potential binary data


        try:
            data = response.json()
            logger.debug(f"Response JSON parsed successfully")
            logger.debug(f"Response data type: {type(data)}")
            if isinstance(data, dict):
                logger.debug(f"Response data keys: {list(data.keys())}")
                # Check for the actual key 'detections'
                if 'detections' in data:
                    logger.debug(f"Found 'detections' key with {len(data['detections'])} items")
                else:
                    logger.debug(f"'detections' key not found in response") # Updated log
            elif isinstance(data, list):
                # This case is unlikely based on observed response, but kept for robustness
                logger.debug(f"Response data is a list with {len(data)} items")
                if data:
                    pass
            else:
                logger.debug(f"Response data is neither dict nor list: {type(data)}")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            logger.error(f"Response content: {response.content}")
            raise

        # Print the response in pretty format
        print(f"\n--- LPR Timestamps API Response for '{license_plate}' ---")
        # Use ensure_ascii=False to correctly display non-ASCII characters
        print(json.dumps(data, indent=4, ensure_ascii=False))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e}")
        logger.error(f"Response status code: {e.response.status_code}")
        logger.error(f"Response headers: {dict(e.response.headers)}")
        logger.error(f"Response content: {e.response.content}")

        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {LPR_TIMESTAMPS_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        elif e.response.status_code == 404:
             logger.error(f"404 Not Found error for {LPR_TIMESTAMPS_ENDPOINT}. License plate '{license_plate}' may not exist or have no detections in the given range.") # Updated log
        # Re-raise the exception after logging
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        logger.error(f"Error type: {type(e)}")
        logger.error(f"Full exception traceback: {traceback.format_exc()}")
        # Re-raise the exception after logging
        raise

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada LPR Timestamps API")
    parser.add_argument(
        "--camera_id",
        required=True,
        help="The unique identifier of the camera (required)"
    )
    parser.add_argument(
        "--license_plate",
        required=True,
        help="The license plate to fetch timestamps for (required)"
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
        default='ERROR', # Changed default to ERROR
        help="Set the logging level (default: ERROR)" # Updated help text
    )
    # Removed --list-for-menu as it's handled by test_cameras_api.py now

    # Parse arguments
    args = parser.parse_args()

    # Set logging level for the stream handler based on the argument.
    # The file handler level is already set to DEBUG.
    # Use the stream_handler instance defined globally for this logger.
    stream_handler.setLevel(getattr(logging, args.log_level))
    logger.debug(f"Stream handler level set to: {args.log_level}") # Log level confirmation

    # Add debug logging to show the arguments received
    logger.debug(f"Arguments received: camera_id='{args.camera_id}', license_plate='{args.license_plate}', history_days={args.history_days}, log_level={args.log_level}") # Debug parsed args

    # Get API key from environment variable
    logger.debug("Attempting to get API_KEY environment variable...") # Debug before getting API key
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)
    else:
        logger.debug(f"API_KEY found: {api_key[:5]}...{api_key[-4:]}") # Debug API key found

    lpr_timestamps_data = None # Initialize to None
    try:
        # Get API token
        logger.debug("Attempting to get API token...") # Debug before getting token
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...") # Keep this info log
        logger.debug(f"Retrieved API token: {api_token[:10]}...") # Debug token

        # Fetch LPR timestamps data
        logger.debug("Attempting to fetch LPR timestamps data...") # Debug before fetching data
        lpr_timestamps_data = fetch_lpr_timestamps_data(api_token, args.camera_id, args.license_plate, args.history_days)
        logger.info(f"Successfully retrieved LPR timestamps data for plate '{args.license_plate}' on camera '{args.camera_id}'")

        # Generate and save JSON template based on the expected structure
        # The template should always have the same structure regardless of the data returned
        template_output = {
            "camera_id": "",
            "detections": [0], # Template for a list of integers
            "license_plate": "",
            "next_page_token": 0 # Assuming next_page_token is an integer
        }

        logger.debug(f"Template data created: {template_output}")

        # Save the template to the src_helix directory
        output_filename = "src_helix/test_lpr_timestamps_api.json"
        logger.debug(f"Writing JSON template to {output_filename}")
        try:
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4, ensure_ascii=False)
            logger.info(f"Generated JSON template: {output_filename}")
        except Exception as write_e:
            logger.error(f"Failed to write JSON template to {output_filename}: {write_e}", exc_info=True)

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
