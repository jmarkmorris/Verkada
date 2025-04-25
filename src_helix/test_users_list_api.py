#!/usr/bin/env python3
"""
Script to test the Verkada Access Users List API endpoint.
Can also list users in a parsable format for menu selection.
"""
import os
import sys
import json
import logging
import requests
import argparse
import traceback # Import traceback

# Import shared utility functions and constants
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, TOKEN_ENDPOINT

# Get the logger for this module
logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG) # Set logger level to DEBUG

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix directory
file_handler = logging.FileHandler('src_helix/users_list_api_debug.log')
file_handler.setLevel(logging.DEBUG) # Set file handler level to DEBUG

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


def fetch_users_list(api_token: str) -> dict: # Changed return type hint to dict
    """Fetch list of access users from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{USERS_LIST_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching access users data from {url}")
        logger.debug(f"Request headers: {headers}") # Added debug log
        logger.debug(f"Using API token: {api_token[:10]}...") # Added debug log

        response = requests.get(url, headers=headers)
        logger.debug(f"Users list response status code: {response.status_code}") # Added debug log
        logger.debug(f"Users list response headers: {dict(response.headers)}") # Added debug log

        response.raise_for_status()
        data = response.json()

        logger.debug(f"Raw users list response data: {data}") # Added debug log

        # Print the response in pretty format
        print("\n--- Access Users List API Response ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

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
        logger.error(f"HTTP Error: {e}") # Added detailed error logging
        logger.error(f"Response status code: {e.response.status_code}") # Added detailed error logging
        logger.error(f"Response headers: {dict(e.response.headers)}") # Added detailed error logging
        logger.error(f"Response content: {e.response.content}") # Added detailed error logging

        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {USERS_LIST_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True) # Added traceback
        raise


def _list_users_for_selection(api_key: str):
    """
    Fetches users and prints them to stdout in 'index,user_id,name' format
    for use by the runtest.sh script menu.
    Suppresses standard logging to stdout during the listing process.
    """
    # We get the logger again here to ensure we have the correct instance
    local_logger = logging.getLogger(__name__)
    temp_stream_handler = None

    # Temporarily remove the stream handler
    # *before* any API calls or printing the marker
    for handler in local_logger.handlers:
        if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
            temp_stream_handler = handler
            local_logger.removeHandler(handler)
            break # Assuming only one StreamHandler for stdout

    try:
        # Get API token using imported function
        # get_api_token now has debug logging, which goes to the file handler
        api_token = get_api_token(api_key)

        # Fetch user data (errors will be logged to file by the file handler)
        url = f"{VERKADA_API_BASE_URL}{USERS_LIST_ENDPOINT}"
        headers = {
            "Accept": "application/json",
            "x-verkada-auth": api_token,
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # These debug logs will now go to the file handler because the logger level is DEBUG
        logger.debug(f"Raw user list data in _list_for_selection: {data}")
        logger.debug(f"Type of data received in _list_for_selection: {type(data)}")

        # Extract the list of users using the correct key 'access_members'
        all_users = data.get('access_members', []) if isinstance(data, dict) else []

        logger.debug(f"Extracted users_list in _list_for_selection: {all_users}")
        logger.debug(f"Length of users_list in _list_for_selection: {len(all_users)}")

        # Add a marker to indicate the start of the parsable output
        # Print directly to stdout, bypassing the logger
        print("---START_USER_LIST---", file=sys.stdout)
        sys.stdout.flush() # Flush the marker immediately

        # Print users in a parsable format: index,user_id,name
        # Print nothing if the list is empty
        for i, user in enumerate(all_users):
            # Ensure user is a dict and has required keys: 'user_id' and 'full_name'
            if isinstance(user, dict) and 'user_id' in user and 'full_name' in user:
                 # Use the full_name provided by the API
                 full_name = user.get('full_name') or "Unnamed User" # Provide a default name

                 # Clean the name to remove any commas that could break parsing
                 clean_name = full_name.replace(',', ' ')

                 print(f"{i+1},{user['user_id']},{clean_name}", file=sys.stdout) # Print user lines
            else:
                 # Updated warning message to reflect the keys being checked
                 logger.warning(f"Skipping user entry due to missing 'user_id' or 'full_name': {user}")

        sys.stdout.flush() # Explicitly flush stdout after printing the list

    except Exception as e:
        # Log the error to the file handler
        logger.error(f"Error listing users for selection: {e}", exc_info=True)
        sys.exit(1) # Exit with non-zero status on error
    finally:
        # Re-add the stream handler
        if temp_stream_handler:
            local_logger.addHandler(temp_stream_handler)


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access Users List API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR', # Changed default to ERROR
        help="Set the logging level (default: ERROR)" # Updated help text
    )
    parser.add_argument(
        "--list-for-selection",
        action="store_true",
        help="Fetch and list users in a format suitable for the runtest.sh menu"
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

    # If --list-for-selection is set, run the helper function and exit
    if args.list_for_selection:
        _list_users_for_selection(api_key)
        sys.exit(0) # Exit successfully after listing


    # Otherwise, proceed with the standard test script logic
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch users list
        logger.debug("Attempting to fetch users list data...")
        users_data = fetch_users_list(api_token) # Capture the full data
        users_list = users_data.get('access_members', []) if isinstance(users_data, dict) else []
        logger.info(f"Successfully retrieved access users list. Found {len(users_list)} users.")

        # Generate and save JSON template if data is available
        if users_list:
            logger.debug(f"First user item: {users_list[0]}")
            template_data = create_template(users_list[0])
            logger.debug(f"Template data created: {template_data}")

            template_output = {"access_members": [template_data]} # Wrap in the expected list structure

            # Save the template to the src_helix directory
            output_filename = "src_helix/api-json/test_users_list_api.json"
            logger.debug(f"Writing template to {output_filename}")
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
