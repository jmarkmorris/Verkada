#!/usr/bin/env python3
"""
Helper script to fetch lists of items (users, cameras) from the Verkada API
and output them as JSON to stdout.
Intended for use by shell scripts (like runtest.sh, testit.sh) for parsing.
Logs are directed to stderr to keep stdout clean for JSON output.

NOTE: This script fetches ONLY THE FIRST PAGE of results for efficiency,
as it's primarily used by testit.sh to get a single item ID.
"""
import os
import sys
import json
import logging
import argparse

# Import shared utility functions
from src_helix.api_utils import (
    get_api_token,
    _fetch_data,
    USERS_LIST_ENDPOINT,
    CAMERAS_ENDPOINT,
    configure_logging,
    LOGS_DIR
)

# Configure logging specifically for this script to output to stderr
def configure_list_items_logging(log_level_str: str = 'ERROR'):
    """
    Configures logging for list_items.py, directing stream output to stderr.

    Args:
        log_level_str: The desired logging level as a string.
    """
    root_logger = logging.getLogger()
    # Clear existing handlers first
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    root_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Stream handler for stderr
    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setFormatter(formatter)
    try:
        stream_handler.setLevel(getattr(logging, log_level_str.upper()))
    except AttributeError:
        print(f"WARNING: Invalid log level string '{log_level_str}'. Defaulting stream handler to ERROR.", file=sys.stderr)
        stream_handler.setLevel(logging.ERROR)

    root_logger.addHandler(stream_handler)

    # File handler for DEBUG logs
    log_file_path = os.path.join(LOGS_DIR, 'list_items_debug.log')
    try:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    except Exception as e:
        print(f"ERROR: Failed to create file handler for {log_file_path}: {e}", file=sys.stderr)


# Get the logger for this module
logger = logging.getLogger(__name__)


def main():
    """
    Main entry point for the script.

    Parses command-line arguments for item type (users/cameras) and log level.
    Retrieves the API key from environment variables.
    Obtains an API token.
    Fetches the *first page* of the specified item type.
    Outputs the list of items as JSON to standard output.
    Logs errors and informational messages to standard error.
    Exits with status 0 if successful, 1 on error.
    """
    parser = argparse.ArgumentParser(description="Fetch and list Verkada API items as JSON (First Page Only)")
    parser.add_argument(
        "--type",
        choices=['users', 'cameras'],
        required=True,
        help="Type of items to list (users or cameras)"
    )
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR',
        help="Set the logging level (default: ERROR)"
    )

    args = parser.parse_args()

    # Configure logging to stderr
    configure_list_items_logging(args.log_level)

    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)

    try:
        # Get API token
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        items_list = []
        endpoint = ""
        list_key = ""

        if args.type == 'users':
            endpoint = USERS_LIST_ENDPOINT
            list_key = 'access_members'
            logger.info(f"Fetching first page of {args.type}...")
        elif args.type == 'cameras':
            endpoint = CAMERAS_ENDPOINT
            list_key = 'cameras'
            logger.info(f"Fetching first page of {args.type}...")

        # Fetch only the first page using _fetch_data
        first_page_data = _fetch_data(api_token, endpoint, method='GET')

        # Extract the list from the response dictionary
        items_list = first_page_data.get(list_key, []) if isinstance(first_page_data, dict) else []

        if not isinstance(items_list, list):
            logger.error(f"Expected a list under the key '{list_key}' but found type {type(items_list)}. API response structure might have changed.")
            sys.exit(1)

        logger.info(f"Fetched {len(items_list)} {args.type} from the first page.")

        # Output the list as JSON to stdout
        json.dump(items_list, sys.stdout, indent=4, ensure_ascii=False)
        sys.stdout.write('\n')
        sys.stdout.flush()

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        logging.shutdown()

if __name__ == '__main__':
    main()
