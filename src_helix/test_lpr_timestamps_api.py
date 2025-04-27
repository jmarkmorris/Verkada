#!/usr/bin/env python3
"""
Script to test the Verkada LPR Timestamps API endpoint.
Fetches ALL timestamps (returned under the 'detections' key) for a specific license plate
within a given time range.
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
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, LPR_TIMESTAMPS_ENDPOINT, configure_logging, save_json_template, fetch_all_lpr_timestamps

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)


def main():
    """
    Main entry point for the script.

    Parses command-line arguments for camera ID, license plate, history duration, and log level.
    Retrieves the API key from environment variables.
    Obtains an API token.
    Fetches all LPR timestamps (detections) for the specified plate/camera/time range.
    Prints the list of detections.
    Generates and saves a JSON template based on the first detection found.
    Exits with status 0 if successful, 1 on error (including fetch errors).
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada LPR Timestamps API (Fetches All)")
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

    # Parse arguments
    args = parser.parse_args()

    # Configure logging using the centralized function
    configure_logging(args.log_level)

    # Add debug logging to show the arguments received
    logger.debug(f"Arguments received: camera_id='{args.camera_id}', license_plate='{args.license_plate}', history_days={args.history_days}, log_level={args.log_level}")

    # Get API key from environment variable
    logger.debug("Attempting to get API_KEY environment variable...")
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)
    else:
        logger.debug(f"API_KEY found: {api_key[:5]}...{api_key[-4:]}")

    lpr_timestamps_list = [] # Initialize to empty list
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")
        logger.debug(f"Retrieved API token: {api_token[:10]}...")

        # Calculate time range
        end_time = int(time.time())
        start_time = end_time - (args.history_days * 24 * 60 * 60)

        # Prepare parameters for the fetch function
        params = {
            "camera_id": args.camera_id,
            "license_plate": args.license_plate,
            "start_time": start_time,
            "end_time": end_time
        }

        # Fetch ALL LPR timestamps data using the function from api_utils
        logger.info(f"Attempting to fetch ALL LPR timestamps (detections) for plate '{args.license_plate}' on camera '{args.camera_id}' for the last {args.history_days} days")
        logger.debug(f"Date range: {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)}")
        lpr_timestamps_list, error_flag = fetch_all_lpr_timestamps(api_token, params=params)

        # Check if an error occurred during fetching
        if error_flag:
            logger.error("Error occurred during pagination while fetching LPR timestamps. Data may be incomplete.")
            sys.exit(1)

        logger.info(f"Successfully retrieved {len(lpr_timestamps_list)} LPR timestamps (detections) for plate '{args.license_plate}' on camera '{args.camera_id}'")

        # Print the full list (or a subset for brevity if needed)
        print(f"\n--- LPR Timestamps API Response for '{args.license_plate}' (All Pages) ---")
        # Be cautious printing very large lists; consider printing only the first few items
        # or just the count in non-debug modes. For now, printing all.
        print(json.dumps(lpr_timestamps_list, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON


        # Generate and save JSON template if data is available
        if lpr_timestamps_list:
            logger.debug(f"First LPR timestamp item: {lpr_timestamps_list[0]}")
            output_filename = "src_helix/api-json/test_lpr_timestamps_api.json"
            save_json_template(lpr_timestamps_list[0], output_filename, wrap_key="detections")
        else:
            logger.warning("No LPR timestamps found to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
