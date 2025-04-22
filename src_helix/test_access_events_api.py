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

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('access_events_api_debug.log') # New log file
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
ACCESS_EVENTS_ENDPOINT = "/access/v1/events" # Specific endpoint

def get_api_token(api_key: str) -> str:
    """Fetch short-lived API token."""
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['token']
    except Exception as e:
        logger.error(f"API token retrieval failed: {e}")
        raise

def create_template(data: dict) -> dict:
    """Recursively create a template dictionary with empty values."""
    template = {}
    for key, value in data.items():
        if isinstance(value, dict):
            template[key] = create_template(value)
        elif isinstance(value, list):
            # For lists, create a list containing one template item if the list is not empty
            template[key] = [create_template(value[0])] if value else []
        elif isinstance(value, str):
            template[key] = ""
        elif isinstance(value, (int, float)):
            template[key] = 0
        elif isinstance(value, bool):
            template[key] = False # Or None, depending on desired empty state for boolean
        else:
            template[key] = None # Handles None and other types

    return template


def fetch_access_events_data(api_token: str, endpoint: str, params=None):
    """Fetch access events data from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{endpoint}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching data from {url}")
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Print the response in pretty format
        print(f"\n--- Access Events API Response from {endpoint} ---")
        print(json.dumps(data, indent=4))
        
        return data
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {endpoint}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
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

    # Directly call the access events endpoint
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
        logger.error(f"Failed to fetch from {ACCESS_EVENTS_ENDPOINT}: {e}")
        return {} # Return empty dict on failure

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access Events API") # Updated description
    parser.add_argument(
        "--history_days", 
        type=int, 
        default=7, 
        help="Number of days of history to query (default: 7)"
    )
    parser.add_argument(
        "--log_level", 
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], 
        default='INFO', 
        help="Set the logging level (default: INFO)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Set logging level
    logging.getLogger().setLevel(getattr(logging, args.log_level))

    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)

    try:
        # Get API token
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")
        
        # Handle access events API
        events_data = handle_access_events_api(api_token, args.history_days) # Capture the returned data

        # Generate and save JSON template if data is available
        events_list = events_data.get('events', []) if isinstance(events_data, dict) else []
        if events_list:
            template_data = create_template(events_list[0])
            template_output = {"events": [template_data]} # Wrap in the expected list structure

            output_filename = "test_access_events_api.json"
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
