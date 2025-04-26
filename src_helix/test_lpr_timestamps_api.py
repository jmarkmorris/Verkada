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

# Import shared utility functions and the centralized logging function and save_json_template
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, LPR_TIMESTAMPS_ENDPOINT, fetch_lpr_enabled_cameras, fetch_lpr_images_for_camera, format_timestamp, _fetch_data, configure_logging, save_json_template # Import functions from api_utils

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


def fetch_lpr_timestamps_data(api_token: str, camera_id: str, license_plate: str, history_days: int):
    """Fetch LPR timestamps data (detections) for a specific license plate from Verkada API."""
    end_time = int(time.time())
    start_time = end_time - (history_days * 24 * 60 * 60)

    params = {
        "camera_id": camera_id, # camera_id is a required parameter
        "license_plate": license_plate,
        "start_time": start_time,
        "end_time": end_time,
        "page_size": 100 # Re-adding page_size, trying a smaller value
    }

    try:
        logger.info(f"Fetching LPR timestamps (detections) for plate '{license_plate}' on camera '{camera_id}' for the last {history_days} days")
        logger.debug(f"Date range: {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)}")

        # Use the new _fetch_data function
        data = _fetch_data(api_token, LPR_TIMESTAMPS_ENDPOINT, method='GET', params=params)

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


        # Print the response in pretty format
        print(f"\n--- LPR Timestamps API Response for '{license_plate}' ---")
        # Use ensure_ascii=False to correctly display non-ASCII characters
        print(json.dumps(data, indent=4, ensure_ascii=False))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        # _fetch_data already logged the basic HTTP error details
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
        # _fetch_data already logged the unexpected error with traceback
        # Log a higher-level error here if needed, or just re-raise
        logger.error(f"Failed to fetch LPR timestamps data: {e}")
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
        default='ERROR',
        help="Set the logging level (default: ERROR)"
    )
    # Removed --list-for-menu as it's handled by test_cameras_api.py now

    # Parse arguments
    args = parser.parse_args()

    # Configure logging using the centralized function
    configure_logging(args.log_level)

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
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key) # Use imported function
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...") # Keep this info log
        logger.debug(f"Retrieved API token: {api_token[:10]}...") # Debug token

        # Fetch LPR timestamps data
        logger.debug("Attempting to fetch LPR timestamps data...") # Debug before fetching data
        lpr_timestamps_data = fetch_lpr_timestamps_data(api_token, args.camera_id, args.license_plate, args.history_days)
        logger.info(f"Successfully retrieved LPR timestamps data for plate '{args.license_plate}' on camera '{args.camera_id}'")

        # Generate and save JSON template based on the fetched data structure
        # Use the centralized save_json_template function
        output_filename = "src_helix/api-json/test_lpr_timestamps_api.json"
        # Pass the fetched data directly. No wrap_key needed as the template is the root object.
        save_json_template(lpr_timestamps_data, output_filename)

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
