#!/usr/bin/env python3
"""
Script to test the Verkada Notifications API endpoint.
Fetches ALL notifications within a specified time range.
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
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, NOTIFICATIONS_ENDPOINT, configure_logging, save_json_template, fetch_all_notifications

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Notifications API (Fetches All)")
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

    # Get API key from environment variable
    logger.debug("Attempting to get API_KEY environment variable...")
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)
    else:
        logger.debug(f"API_KEY found: {api_key[:5]}...{api_key[-4:]}")

    notifications_list = [] # Initialize to empty list
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Calculate time range
        end_time = int(time.time())
        start_time = end_time - (args.history_days * 24 * 60 * 60)
        logger.info(f"Querying notifications for the last {args.history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")

        # Prepare parameters for the fetch function
        params = {
            "start_time": start_time,
            "end_time": end_time
        }

        # Fetch ALL notifications using the function from api_utils
        logger.info(f"Attempting to fetch ALL notifications from {NOTIFICATIONS_ENDPOINT}")
        notifications_list, error_flag = fetch_all_notifications(api_token, params=params)

        # Check if an error occurred during fetching
        if error_flag:
            logger.error("Error occurred during pagination while fetching notifications. Data may be incomplete.")
            sys.exit(1)

        logger.info(f"Successfully retrieved {len(notifications_list)} notifications.")

        # Print the full list (or a subset for brevity if needed)
        print(f"\n--- Notifications API Response from {NOTIFICATIONS_ENDPOINT} (All Pages) ---")
        # Be cautious printing very large lists; consider printing only the first few items
        # or just the count in non-debug modes. For now, printing all.
        print(json.dumps(notifications_list, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON


        # Generate and save JSON template if data is available
        logger.debug(f"Number of notifications found: {len(notifications_list)}")

        if notifications_list:
            logger.debug(f"First notification item: {notifications_list[0]}")
            output_filename = "src_helix/api-json/test_notifications_api.json"
            save_json_template(notifications_list[0], output_filename, wrap_key="notifications")
        else:
            logger.warning("No notifications found to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
