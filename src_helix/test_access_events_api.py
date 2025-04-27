#!/usr/bin/env python3
"""
Script to test the Verkada Access Events API endpoint.
Fetches ALL access events within a specified time range.
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
# Import fetch_all_access_events from api_utils
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, ACCESS_EVENTS_ENDPOINT, configure_logging, save_json_template, fetch_all_access_events

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


# Removed the old fetch_access_events_data function


# Removed the old handle_access_events_api function


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access Events API (Fetches All)")
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

    events_list = [] # Initialize to empty list
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Calculate time range
        end_time = int(time.time())
        start_time = end_time - (args.history_days * 24 * 60 * 60)
        logger.info(f"Querying access events for the last {args.history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")

        # Prepare parameters for the fetch function
        params = {
            "start_time": start_time,
            "end_time": end_time
            # page_size is handled by fetch_all_paginated_data
        }

        # Fetch ALL access events using the function from api_utils
        logger.info(f"Attempting to fetch ALL access events from {ACCESS_EVENTS_ENDPOINT}")
        # fetch_all_access_events now returns a tuple (list, error_flag)
        events_list, error_flag = fetch_all_access_events(api_token, params=params)

        # Check if an error occurred during fetching
        if error_flag:
            logger.error("Error occurred during pagination while fetching access events. Data may be incomplete.")
            # Exit with non-zero status to indicate failure
            sys.exit(1)

        logger.info(f"Successfully retrieved {len(events_list)} access events.")

        # Print the full list (or a subset for brevity if needed)
        print(f"\n--- Access Events API Response from {ACCESS_EVENTS_ENDPOINT} (All Pages) ---")
        # Be cautious printing very large lists; consider printing only the first few items
        # or just the count in non-debug modes. For now, printing all.
        print(json.dumps(events_list, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON


        # Generate and save JSON template if data is available
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
