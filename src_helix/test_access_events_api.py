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
file_handler = logging.FileHandler('src_helix/access_events_api_debug.log')
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


ACCESS_EVENTS_ENDPOINT = "/access/v1/events" # Specific endpoint

def fetch_access_events_data(api_token: str, endpoint: str, params=None):
    """Fetch access events data from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{endpoint}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching data from {url}")
        logger.debug(f"Request headers: {headers}")
        logger.debug(f"Request parameters: {params}")
        logger.debug(f"Using API token: {api_token[:10]}...")

        response = requests.get(url, headers=headers, params=params)
        logger.debug(f"Access events response status code: {response.status_code}")
        logger.debug(f"Access events response headers: {dict(response.headers)}")

        response.raise_for_status()
        data = response.json()

        logger.debug(f"Raw access events response data: {data}")

        # Print the response in pretty format
        print(f"\n--- Access Events API Response from {endpoint} ---")
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
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise


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
        default='ERROR', # Changed default to ERROR
        help="Set the logging level (default: ERROR)" # Updated help text
    )

    # Parse arguments
    args = parser.parse_args()

    # Set logging level for the stream handler based on the argument.
    # The file handler level is already set to DEBUG.
    stream_handler.setLevel(getattr(logging, args.log_level))
    logger.debug(f"Stream handler level set to: {args.log_level}")

    # Get API key from environment variable
    logger.debug("Attempting to get API_KEY environment variable...")
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)
    else:
        logger.debug(f"API_KEY found: {api_key[:5]}...{api_key[-4:]}")

    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Handle access events API
        logger.debug("Attempting to fetch access events data...")
        events_data = handle_access_events_api(api_token, args.history_days)

        # Generate and save JSON template if data is available
        events_list = events_data.get('events', []) if isinstance(events_data, dict) else []
        logger.debug(f"Number of access events found: {len(events_list)}")

        if events_list:
            logger.debug(f"First access event item: {events_list[0]}")
            template_data = create_template(events_list[0])
            logger.debug(f"Template data created: {template_data}")

            template_output = {"events": [template_data]} # Wrap in the expected list structure

            # Save the template to the src_helix directory
            output_filename = "src_helix/api-json/test_access_events_api.json"
            logger.debug(f"Writing template to {output_filename}")
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No access events found to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
