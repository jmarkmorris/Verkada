#!/usr/bin/env python3
"""
Script to test the Verkada Access Users List API endpoint.
"""
import os
import sys
import json
import logging
import requests
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('users_list_api_debug.log') # Updated log file name
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
USERS_LIST_ENDPOINT = "/access/v1/access_users"  # Endpoint for listing users

def get_api_token(api_key: str) -> str:
    """Fetch short-lived API token."""
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        logger.info(f"Requesting token from {url}")
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


def fetch_users_list(api_token: str) -> list:
    """Fetch list of access users from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{USERS_LIST_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching access users data from {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Print the response in pretty format
        print("\n--- Access Users List API Response ---")
        print(json.dumps(data, indent=4))

        # Add debugging
        logger.debug(f"Type of data variable: {type(data)}")
        if isinstance(data, dict):
            logger.debug(f"Keys in data: {list(data.keys())}")
            # Corrected key check for debugging
            logger.debug(f"Value for 'access_members' key: {data.get('access_members')}") 
        else:
            logger.debug("Data variable is not a dictionary.")

        # Corrected key to 'access_members'
        users = data.get('access_members', []) if isinstance(data, dict) else []
        if not users:
            logger.warning("No access members found in the response.") # Updated warning message

        return data # Return the full data dictionary
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {USERS_LIST_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access Users List API") # Updated description
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
        
        # Fetch users list
        users_data = fetch_users_list(api_token) # Capture the full data
        users_list = users_data.get('access_members', []) if isinstance(users_data, dict) else []
        logger.info(f"Successfully retrieved access users list. Found {len(users_list)} users.")

        # Generate and save JSON template if data is available
        if users_list:
            template_data = create_template(users_list[0])
            template_output = {"access_members": [template_data]} # Wrap in the expected list structure

            output_filename = "test_users_list_api.json"
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No access users found to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
