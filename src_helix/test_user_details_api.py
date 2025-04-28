#!/usr/bin/env python3
"""
Script to test the Verkada Access User Details API endpoint.
Requires a user_id as input.
"""
import os
import sys
import json
import logging
import requests
import argparse

# Import shared utility functions and constants, including configure_logging and save_json_template
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, USERS_LIST_ENDPOINT, USER_DETAILS_ENDPOINT, _fetch_data, configure_logging, save_json_template

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)


def fetch_user_details(api_token: str, user_id: str):
    """
    Fetch specific access user details from Verkada API.

    Args:
        api_token: The short-lived API token.
        user_id: The unique identifier of the user to fetch.

    Returns:
        A dictionary containing the user details if successful.

    Raises:
        requests.exceptions.HTTPError: If the API returns an HTTP error status (4xx or 5xx).
        Exception: For other unexpected errors during the request or JSON parsing.
    """
    params = {
        "user_id": user_id
    }

    try:
        data = _fetch_data(api_token, USER_DETAILS_ENDPOINT, method='GET', params=params)

        logger.debug(f"Raw user details response data: {data}")

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
             logger.error(f"404 Not Found error for {USER_DETAILS_ENDPOINT}. User ID '{user_id}' may not exist.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error fetching user details: {e}", exc_info=True)
        raise


def main():
    """
    Main entry point for the script.

    Parses command-line arguments for user ID and log level.
    Retrieves the API key from environment variables.
    Obtains an API token.
    Fetches the details for the specified user ID.
    Prints the user details.
    Generates and saves a JSON template based on the fetched details.
    Exits with status 0 if successful, 1 on error.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Access User Details API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR',
        help="Set the logging level (default: ERROR)"
    )
    parser.add_argument(
        "--user_id",
        type=str,
        required=True,
        help="The unique identifier of the user to fetch details for"
    )


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

    user_details = None # Initialize to None
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch details for the specified user_id
        user_id_to_fetch = args.user_id
        logger.info(f"Attempting to fetch details for user ID: {user_id_to_fetch}...")

        # Add a small delay before fetching user details
        # time.sleep(0.5)

        user_details = fetch_user_details(api_token, user_id_to_fetch)

        # Print the custom line using the user_id provided
        print(f"\nDetail information for user ID: {user_id_to_fetch}")
        sys.stdout.flush()

        # Now print the full details response if it was successfully fetched
        if user_details:
            print(f"\n--- Access User Details API Response (User ID: {user_id_to_fetch}) ---")
            print(json.dumps(user_details, indent=4))
            sys.stdout.flush()
            logger.info(f"Successfully retrieved details for user ID: {user_id_to_fetch}")

            # Generate and save JSON template
            logger.debug("Generating JSON template...")
            output_filename = "src_helix/api-json/test_user_details_api.json"
            save_json_template(user_details, output_filename)

        else:
             logger.warning(f"No details returned for user ID {user_id_to_fetch}.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
