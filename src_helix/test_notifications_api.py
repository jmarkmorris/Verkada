#!/usr/bin/env python3
"""
Script to test the Verkada Notifications API endpoint.
"""
import os # Import os
import sys
import json
import logging
import requests
import argparse
import time
import datetime
import traceback

# Import shared utility functions and the centralized logging function
# Import _fetch_data from api_utils
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, NOTIFICATIONS_ENDPOINT, _fetch_data, configure_logging

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


def fetch_notifications_data(api_token: str, endpoint: str, params=None):
    """Fetch notifications data from Verkada API."""
    try:
        # Use the new _fetch_data function
        data = _fetch_data(api_token, endpoint, method='GET', params=params)

        logger.debug(f"Raw notifications response data: {data}")

        # Print the response in pretty format
        print(f"\n--- Notifications API Response from {endpoint} ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e}")
        logger.error(f"Response status code: {e.response.status_code}")
        logger.error(f"Response headers: {dict(e.response.headers)}")
        logger.error(f"Response content: {e.response.content}")

        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {endpoint}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise # Re-raise the exception after logging
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise # Re-raise the exception


def handle_notifications_api(api_token: str, history_days: int):
    """Fetch notifications from Verkada API."""
    end_time = int(time.time())
    start_time = end_time - (history_days * 24 * 60 * 60)

    logger.info(f"Querying notifications for the last {history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "page_size": 200
    }

    try:
        logger.info(f"Attempting to fetch notifications from {NOTIFICATIONS_ENDPOINT}")
        notifications_data = fetch_notifications_data(api_token, NOTIFICATIONS_ENDPOINT, params)

        notifications_key = 'notifications'

        if notifications_key not in notifications_data or not notifications_data[notifications_key]:
            logger.warning(f"No {notifications_key} found in {NOTIFICATIONS_ENDPOINT} response")
        else:
            notifications = notifications_data[notifications_key]
            logger.info(f"Successfully retrieved {len(notifications)} notifications.")

        return notifications_data # Return the fetched data

    except Exception as e:
        # fetch_notifications_data already logs the specific error
        logger.error(f"Failed to fetch from {NOTIFICATIONS_ENDPOINT}: {e}", exc_info=True)
        return {} # Return empty dict on failure

def main():
    """Main entry point for the script."""
    # Add a critical log message at the very start of main
    # logger.critical("Script test_notifications_api.py started.") # Removed this specific critical log

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Notifications API")
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

    notifications_data = None # Initialize to None
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Handle notifications API
        logger.debug("Attempting to fetch notifications data...")
        notifications_data = handle_notifications_api(api_token, args.history_days)

        # Generate and save JSON template if data is available
        notifications_list = notifications_data.get('notifications', []) if isinstance(notifications_data, dict) else []
        logger.debug(f"Number of notifications found: {len(notifications_list)}")

        if notifications_list:
            logger.debug(f"First notification item: {notifications_list[0]}")
            template_data = create_template(notifications_list[0])
            logger.debug(f"Template data created: {template_data}")

            template_output = {"notifications": [template_data]} # Wrap in the expected list structure

            # Save the template to the src_helix directory
            output_filename = "src_helix/api-json/test_notifications_api.json"
            logger.debug(f"Writing template to {output_filename}")
            try:
                with open(output_filename, 'w') as f:
                    json.dump(template_output, f, indent=4)
                logger.info(f"Generated JSON template: {output_filename}")
            except Exception as write_e:
                logger.error(f"Failed to write JSON template to {output_filename}: {write_e}", exc_info=True)
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
