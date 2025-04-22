#!/usr/bin/env python3
"""
Script to test the Verkada Access Users API endpoint.
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
        logging.FileHandler('users_api_debug.log')  # Changed log file name
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
USERS_LIST_ENDPOINT = "/access/v1/access_users"  # Endpoint for listing users
USER_DETAILS_ENDPOINT = "/access/v1/access_users/user" # Endpoint for getting a specific user

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
        
        return users
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {USERS_LIST_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise

def fetch_user_details(api_token: str, user_id: str):
    """Fetch specific access user details from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{USER_DETAILS_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }
    params = {
        "user_id": user_id
    }

    try:
        logger.info(f"Fetching details for user_id {user_id} from {url}")
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Print the response in pretty format
        print(f"\n--- Access User Details API Response (User ID: {user_id}) ---")
        print(json.dumps(data, indent=4))
        
        return data
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {USER_DETAILS_ENDPOINT} with user_id {user_id}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        elif e.response.status_code == 404:
             logger.error(f"404 Not Found error for {USER_DETAILS_ENDPOINT} with user_id {user_id}. User may not exist.")
        raise

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access Users API")
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
        users_list = fetch_users_list(api_token)
        logger.info(f"Successfully retrieved access users list. Found {len(users_list)} users.")

        # Fetch details for the first user if available
        if users_list:
            first_user = users_list[0]
            user_id_to_fetch = first_user.get('user_id')
            
            if user_id_to_fetch:
                logger.info(f"Attempting to fetch details for the first user (ID: {user_id_to_fetch})...")
                user_details = fetch_user_details(api_token, user_id_to_fetch)
                logger.info(f"Successfully retrieved details for user ID: {user_id_to_fetch}")
            else:
                logger.warning("Could not find 'user_id' in the first user object.")
        else:
            logger.info("Skipping user details fetch because the user list is empty.")
            
    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
