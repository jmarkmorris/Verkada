#!/usr/bin/env python3
"""
Script to test the Verkada Access Events API endpoint.
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
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, ACCESS_EVENTS_ENDPOINT, _fetch_data, configure_logging, save_json_template

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


def fetch_access_events_data(api_token: str, endpoint: str, params=None):
    """Fetch access events data from Verkada API."""
    try:
        # Use the new _fetch_data function
        data = _fetch_data(api_token, endpoint, method='GET', params=params)

        logger.debug(f"Raw access events response data: {data}")

        # Print the response in pretty format
        print(f"\n--- Access Events API Response from {endpoint} ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        # _fetch_data already logged the basic HTTP error details
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {endpoint}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise # Re-raise the exception after logging
    except Exception as e:
        # _fetch_data already logged the unexpected error with traceback
        # Log a higher-level error here if needed, or just re-raise
        logger.error(f"Failed to fetch access events data: {e}")
        raise # Re-raise the exception


def handle_access_events_api(api_token: str, history_days: int):
    """Fetch access events from Verkada API."""
    end_time = int(time.time())
    start_time = end_time - (history_days * 24 * 60 * 60)

    logger.info(f"Querying access events for the last {history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "page_size": 200
    }

    try:
        logger.info(f"Attempting to fetch access events from {ACCESS_EVENTS_ENDPOINT}")
        events_data = fetch_access_events_data(api_token, ACCESS_EVENTS_ENDPOINT, params)

        events_key = 'events'

        if events_key not in events_data or not events_data[events_key]:
            logger.warning(f"No {events_key} found in {ACCESS_EVENTS_ENDPOINT} response")
        else:
            events = events_data[events_key]
            logger.info(f"Successfully retrieved {len(events)} access events.")

        return events_data # Return the fetched data

    except Exception as e:
        # fetch_access_events_data already logs the specific error
        logger.error(f"Failed to fetch from {ACCESS_EVENTS_ENDPOINT}: {e}", exc_info=True)
        return {} # Return empty dict on failure

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access Events API")
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

    events_data = None # Initialize to None
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Handle access events API
        logger.debug("Attempting to fetch access events data...")
        events_data = handle_access_events_api(api_token, args.history_days)

        # Generate and save JSON template if data is available
        events_list = events_data.get('events', []) if isinstance(events_data, dict) else []
        logger.debug(f"Number of access events found: {len(events_list)}")

        if events_list:
            logger.debug(f"First access event item: {events_list[0]}")
            # Use the centralized save_json_template function
            output_filename = "src_helix/api-json/test_access_events_api.json"
            # Pass the first item of the list and the key to wrap it with
            save_json_template(events_list[0], output_filename, wrap_key="events")
        else:
            logger.warning("No access events found to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
