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
import time # Import the time module

# Import shared utility functions and constants, including configure_logging and save_json_template
# Import _fetch_data from api_utils
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, USERS_LIST_ENDPOINT, USER_DETAILS_ENDPOINT, _fetch_data, configure_logging, save_json_template

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


def fetch_users_list_silently(api_token: str) -> list:
    """Fetch list of access users from Verkada API without printing full response."""
    try:
        # Use the new _fetch_data function
        data = _fetch_data(api_token, USERS_LIST_ENDPOINT, method='GET')

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
        raise # Re-raise the exception after logging
    except Exception as e:
        logger.error(f"Unexpected error fetching user list silently: {e}", exc_info=True)
        raise # Re-raise the exception


def fetch_user_details(api_token: str, user_id: str):
    """Fetch specific access user details from Verkada API."""
    params = {
        "user_id": user_id
    }

    try:
        # Use the new _fetch_data function
        data = _fetch_data(api_token, USER_DETAILS_ENDPOINT, method='GET', params=params)

        logger.debug(f"Raw user details response data: {data}")

        # Print the details response in pretty format
        # This print happens AFTER the custom print line below
        # print(f"\n--- Access User Details API Response (User ID: {user_id}) ---")
        # print(json.dumps(data, indent=4))
        # sys.stdout.flush() # Explicitly flush stdout after printing JSON

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
             logger.error(f"404 Not Found error for {USER_DETAILS_ENDPOINT}. User may not exist.")
        raise # Re-raise the exception after logging
    except Exception as e:
        logger.error(f"Unexpected error fetching user details: {e}", exc_info=True)
        raise # Re-raise the exception


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access User Details API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR',
        help="Set the logging level (default: ERROR)"
    )
    parser.add_argument(
        "--user_index",
        type=int,
        default=0,
        help="Index of the user in the list to fetch details for (default: 0)"
    )
    # Add new argument to receive the 1-based user number from the menu
    parser.add_argument(
        "--user_number",
        type=int,
        required=False, # Not required if script is run directly
        help="The 1-based number of the user selected from the menu"
    )
    # Removed --user_display_string argument
    # parser.add_argument(
    #     "--user_display_string",
    #     type=str,
    #     required=False, # Not required if script is run directly
    #     help="The full display string of the user selected from the menu"
    # )


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

    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
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

            selected_user_from_list = users_list[args.user_index] # Keep this for the base record print
            user_id_to_fetch = selected_user_from_list.get('user_id')

            if user_id_to_fetch:
                # Print the base user record before fetching details
                print("\n--- Base User Record (from list) ---")
                print(json.dumps(selected_user_from_list, indent=4))
                sys.stdout.flush() # Explicitly flush stdout

                logger.info(f"Attempting to fetch details for user at index {args.user_index} (ID: {user_id_to_fetch})...")

                # Add a small delay before fetching user details
                time.sleep(0.5) # Pause for 0.5 seconds

                user_details = fetch_user_details(api_token, user_id_to_fetch)

                # Print the custom line using the user number and name from the *list* record
                if selected_user_from_list and isinstance(selected_user_from_list, dict):
                    # Get name from the list record, which contains full_name
                    full_name_from_list = selected_user_from_list.get('full_name', 'Unnamed User')
                    # Use 1-based number if provided, else calculate from index
                    user_number_display = args.user_number if args.user_number is not None else args.user_index + 1
                    print(f"\nDetail information for user {user_number_display}) {full_name_from_list}")
                    sys.stdout.flush() # Explicitly flush stdout

                # Now print the full details response if it was successfully fetched
                if user_details:
                    print(f"\n--- Access User Details API Response (User ID: {user_id_to_fetch}) ---")
                    print(json.dumps(user_details, indent=4))
                    sys.stdout.flush() # Explicitly flush stdout
                    logger.info(f"Successfully retrieved details for user ID: {user_id_to_fetch}")

                    # Generate and save JSON template
                    logger.debug("Generating JSON template...")
                    # Use the centralized save_json_template function
                    output_filename = "src_helix/api-json/test_user_details_api.json"
                    # Pass the data directly, no wrap_key needed as it's not a list item
                    save_json_template(user_details, output_filename)

                else:
                     logger.warning(f"No details returned for user ID {user_id_to_fetch}.")

            else:
                logger.warning(f"Could not find 'user_id' in the user object at index {args.user_index}.")
        else:
            logger.info("Skipping user details fetch because the user list is empty.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
