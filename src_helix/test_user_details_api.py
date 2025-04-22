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
import traceback

# Import shared utility functions and constants
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, TOKEN_ENDPOINT

# Get the logger for this module
logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG)

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix directory
file_handler = logging.FileHandler('src_helix/user_details_api_debug.log')
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


USERS_LIST_ENDPOINT = "/access/v1/access_users"  # Endpoint for listing users
USER_DETAILS_ENDPOINT = "/access/v1/access_users/user" # Endpoint for getting a specific user


def fetch_users_list_silently(api_token: str) -> list:
    """Fetch list of access users from Verkada API without printing full response."""
    url = f"{VERKADA_API_BASE_URL}{USERS_LIST_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching access users list silently from {url}")
        logger.debug(f"Request headers: {headers}")
        logger.debug(f"Using API token: {api_token[:10]}...")

        response = requests.get(url, headers=headers)
        logger.debug(f"Users list (silent) response status code: {response.status_code}")
        logger.debug(f"Users list (silent) response headers: {dict(response.headers)}")

        response.raise_for_status()
        data = response.json()

        logger.debug(f"Raw users list (silent) response data: {data}")

        users = data.get('access_members', []) if isinstance(data, dict) else []
        if not users:
            logger.warning("No access members found in the response.")

        return users
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error fetching user list silently: {e}")
        logger.error(f"Response status code: {e.response.status_code}")
        logger.error(f"Response headers: {dict(e.response.headers)}")
        logger.error(f"Response content: {e.response.content}")
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {USERS_LIST_ENDPOINT}. Possible permission issue.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error fetching user list silently: {e}", exc_info=True)
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
        logger.debug(f"Request headers: {headers}")
        logger.debug(f"Request parameters: {params}")
        logger.debug(f"Using API token: {api_token[:10]}...")

        response = requests.get(url, headers=headers, params=params)
        logger.debug(f"User details response status code: {response.status_code}")
        logger.debug(f"User details response headers: {dict(response.headers)}")

        response.raise_for_status()
        data = response.json()

        logger.debug(f"Raw user details response data: {data}")

        # Print the details response in pretty format
        print(f"\n--- Access User Details API Response (User ID: {user_id}) ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error fetching user details: {e}")
        logger.error(f"Response status code: {e.response.status_code}")
        logger.error(f"Response headers: {dict(e.response.headers)}")
        logger.error(f"Response content: {e.response.content}")

        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {USER_DETAILS_ENDPOINT} with user_id {user_id}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        elif e.response.status_code == 404:
             logger.error(f"404 Not Found error for {USER_DETAILS_ENDPOINT} with user_id {user_id}. User may not exist.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error fetching user details: {e}", exc_info=True)
        raise


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access User Details API")
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

        # Fetch users list silently
        logger.debug("Attempting to fetch users list silently...")
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
                    logger.debug("Generating JSON template...")
                    template_data = create_template(user_details)
                    logger.debug(f"Template data created: {template_data}")

                    # Save the template to the src_helix directory
                    output_filename = "src_helix/test_user_details_api.json"
                    logger.debug(f"Writing template to {output_filename}")
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
