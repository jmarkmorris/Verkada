#!/usr/bin/env python3
"""
Script to test the Verkada Alerts API endpoint.
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
        logging.FileHandler('alerts_api_debug.log')
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
ALERTS_ENDPOINT = "/cameras/v1/notifications"
ALTERNATIVE_ENDPOINTS = [
    "/access/v1/events",
    "/cameras/v1/analytics/lpr/imagesview"
]

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

def fetch_api_data(api_token: str, endpoint: str, params=None):
    """Fetch data from Verkada API."""
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
        print(f"\n--- API Response from {endpoint} ---")
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

def handle_alerts_api(api_token: str, history_days: int):
    """Fetch alerts from Verkada API with fallback mechanisms."""
    end_time = int(time.time())
    start_time = end_time - (history_days * 24 * 60 * 60)
    
    logger.info(f"Querying alerts for the last {history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "page_size": 200
    }

    # List of endpoints to try
    endpoints_to_try = [ALERTS_ENDPOINT] + ALTERNATIVE_ENDPOINTS

    for endpoint in endpoints_to_try:
        try:
            logger.info(f"Attempting to fetch events from {endpoint}")
            
            events_data = fetch_api_data(api_token, endpoint, params)
            
            # Determine the correct key based on the endpoint
            events_key = 'notifications' if endpoint == ALERTS_ENDPOINT else \
                         'events' if endpoint == "/access/v1/events" else \
                         'license_plates'

            if events_key not in events_data or not events_data[events_key]:
                logger.warning(f"No {events_key} found in {endpoint} response")
                continue

            events = events_data[events_key]
            
            print(f"\n--- Events from {endpoint} ---")
            print(json.dumps(events, indent=4))
            
            return

        except Exception as e:
            logger.warning(f"Failed to fetch from {endpoint}: {e}")
            continue

    # If all endpoints fail
    logger.error("Unable to fetch events from any endpoint")
    print("\nTroubleshooting:")
    print("1. Verify API key permissions")
    print("2. Check network connectivity")
    print("3. Confirm Verkada API is accessible")

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Alerts API")
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
        
        # Handle alerts API
        handle_alerts_api(api_token, args.history_days)
    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
