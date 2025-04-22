#!/usr/bin/env python3
"""
Script to test the Verkada Access User Details API endpoint.
Fetches the user list first to get a user_id.
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
        # Save log file in the src_helix directory
        logging.FileHandler('src_helix/user_details_api_debug.log') # New log file name
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
        # Keep token request logging minimal for this script
        # logger.info(f"Requesting token from {url}")
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


def fetch_users_list_silently(api_token: str) -> list:
    """Fetch list of access users from Verkada API without printing full response."""
    url = f"{VERKADA_API_BASE_URL}{USERS_LIST_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching access users list silently from {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Don't print the full list here
        # print("\n--- Access Users List API Response ---")
        # print(json.dumps(data, indent=4))

        users = data.get('access_members', []) if isinstance(data, dict) else []
        if not users:
            logger.warning("No access members found in the response.")

        return users
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {USERS_LIST_ENDPOINT}. Possible permission issue.")
        # Keep error logging concise
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

        # Print the details response in pretty format
        print(f"\n--- Access User Details API Response (User ID: {user_id}) ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

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
    parser = argparse.ArgumentParser(description="Test Verkada Access User Details API") # Updated description
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO',
        help="Set the logging level (default: INFO)"
    )
    parser.add_argument(
        "--user_index",
        type=int,
        default=0,
        help="Index of the user in the list to fetch details for (default: 0)"
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

        # Fetch users list silently
        users_list = fetch_users_list_silently(api_token)
        logger.info(f"Silently retrieved access users list. Found {len(users_list)} users.")

        # Fetch details for the specified user if available
        if users_list:
            if args.user_index < 0 or args.user_index >= len(users_list):
                logger.error(f"Invalid user_index {args.user_index}. Must be between 0 and {len(users_list) - 1}.")
                sys.exit(1)

            selected_user = users_list[args.user_index]
            user_id_to_fetch = selected_user.get('user_id')

            if user_id_to_fetch:
                logger.info(f"Attempting to fetch details for user at index {args.user_index} (ID: {user_id_to_fetch})...")
                user_details = fetch_user_details(api_token, user_id_to_fetch)
                logger.info(f"Successfully retrieved details for user ID: {user_id_to_fetch}")

                # Generate and save JSON template if details were fetched
                if user_details:
                    template_data = create_template(user_details)
                    # Save the template to the src_helix directory
                    output_filename = "src_helix/test_user_details_api.json"
                    with open(output_filename, 'w') as f:
                        json.dump(template_data, f, indent=4)
                    logger.info(f"Generated JSON template: {output_filename}")
                else:
                    logger.warning(f"No details returned for user ID {user_id_to_fetch} to generate a template.")

            else:
                logger.warning(f"Could not find 'user_id' in the user object at index {args.user_index}.")
        else:
            logger.info("Skipping user details fetch because the user list is empty.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
