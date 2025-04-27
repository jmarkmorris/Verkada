#!/usr/bin/env python3
"""
Script to test the Verkada Access Users List API endpoint.
Fetches and prints the list of access users and saves a JSON template.
"""
import os
import sys
import json
import logging
import requests
import argparse
import traceback

# Import shared utility functions and constants, including configure_logging and save_json_template
# Import _fetch_data from api_utils
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, USERS_LIST_ENDPOINT, _fetch_data, configure_logging, save_json_template

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


def fetch_users_list(api_token: str) -> dict:
    """Fetch list of access users from Verkada API (first page only)."""
    # Note: This function fetches only the first page.
    # Use fetch_all_access_users from api_utils for full list with pagination.
    try:
        # Use the new _fetch_data function
        data = _fetch_data(api_token, USERS_LIST_ENDPOINT, method='GET')

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
        raise # Re-raise the exception after logging
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True) # Added traceback
        raise # Re-raise the exception


# Removed the _list_users_for_selection function


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access Users List API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR',
        help="Set the logging level (default: ERROR)"
    )
    # Removed --list-for-selection argument


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

    users_data = None # Initialize to None
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")

        # Fetch users list (first page)
        logger.debug("Attempting to fetch users list data...")
        users_data = fetch_users_list(api_token) # Capture the full data
        users_list = users_data.get('access_members', []) if isinstance(users_data, dict) else []
        logger.info(f"Successfully retrieved access users list (first page). Found {len(users_list)} users on this page.")

        # Generate and save JSON template if data is available
        if users_list:
            logger.debug(f"First user item: {users_list[0]}")
            # Use the centralized save_json_template function
            output_filename = "src_helix/api-json/test_users_list_api.json"
            # Pass the first item of the list and the key to wrap it with
            save_json_template(users_list[0], output_filename, wrap_key="access_members")
        else:
            logger.warning("No access users found on the first page to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
