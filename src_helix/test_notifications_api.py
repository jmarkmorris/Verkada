#!/usr/bin/env python3
"""
Script to test the Verkada Notifications API endpoint.
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
        logging.FileHandler('notifications_api_debug.log') # Renamed log file
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
NOTIFICATIONS_ENDPOINT = "/cameras/v1/notifications" # Renamed constant

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

def fetch_notifications_data(api_token: str, endpoint: str, params=None): # Renamed function
    """Fetch notifications data from Verkada API."""
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
        print(f"\n--- Notifications API Response from {endpoint} ---") # Updated print message
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

def handle_notifications_api(api_token: str, history_days: int): # Renamed function
    """Fetch notifications from Verkada API."""
    end_time = int(time.time())
    start_time = end_time - (history_days * 24 * 60 * 60)
    logger.info(f"Querying notifications for the last {history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})") # Updated log message

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "page_size": 200
    }

    # Directly call the notifications endpoint without fallback
    try:
        logger.info(f"Attempting to fetch notifications from {NOTIFICATIONS_ENDPOINT}")
        
        notifications_data = fetch_notifications_data(api_token, NOTIFICATIONS_ENDPOINT, params)
        
        notifications_key = 'notifications' 

        if notifications_key not in notifications_data or not notifications_data[notifications_key]:
            logger.warning(f"No {notifications_key} found in {NOTIFICATIONS_ENDPOINT} response")
        else:
            notifications = notifications_data[notifications_key]
            # Optional: print details if needed, already printed in fetch function
            # print(f"\n--- Notifications from {NOTIFICATIONS_ENDPOINT} ---")
            # print(json.dumps(notifications, indent=4))
            logger.info(f"Successfully retrieved {len(notifications)} notifications.")

    except Exception as e:
        logger.error(f"Failed to fetch from {NOTIFICATIONS_ENDPOINT}: {e}")
        # Removed fallback logic and associated error messages

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Notifications API") # Updated description
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
        # Handle notifications API
        handle_notifications_api(api_token, args.history_days) # Call renamed function
    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
