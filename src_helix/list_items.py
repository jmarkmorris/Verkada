#!/usr/bin/env python3
"""
Helper script to fetch lists of items (users, cameras) from the Verkada API
and output them as JSON to stdout.
Intended for use by shell scripts (like runtest.sh, testit.sh) for parsing.
Logs are directed to stderr to keep stdout clean for JSON output.
"""
import os
import sys
import json
import logging
import argparse

# Import shared utility functions, including the new fetch_all functions
from src_helix.api_utils import (
    get_api_token,
    fetch_all_access_users,
    fetch_all_cameras,
    configure_logging,
    LOGS_DIR # Import LOGS_DIR to potentially configure file logging path
)

# Configure logging specifically for this script to output to stderr
# This ensures stdout is clean for the JSON output.
# We still use the configure_logging function but might adjust handlers if needed.
# Let's re-configure the root logger to use stderr for stream output.
def configure_list_items_logging(log_level_str: str = 'ERROR'):
    """
    Configures logging for list_items.py, directing stream output to stderr.
    """
    root_logger = logging.getLogger()
    # Clear existing handlers first
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    root_logger.setLevel(logging.DEBUG) # Set root to DEBUG to capture all messages

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Stream handler for stderr
    stream_handler = logging.StreamHandler(sys.stderr) # Direct stream output to stderr
    stream_handler.setFormatter(formatter)
    try:
        stream_handler.setLevel(getattr(logging, log_level_str.upper()))
    except AttributeError:
        print(f"WARNING: Invalid log level string '{log_level_str}'. Defaulting stream handler to ERROR.", file=sys.stderr)
        stream_handler.setLevel(logging.ERROR)

    root_logger.addHandler(stream_handler)

    # Optional: Add a file handler for DEBUG logs if desired, similar to api_utils
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
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Fetch and list Verkada API items as JSON")
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
        if args.type == 'users':
            logger.info("Fetching all access users...")
            items_list = fetch_all_access_users(api_token)
            logger.info(f"Fetched {len(items_list)} access users.")
        elif args.type == 'cameras':
            logger.info("Fetching all cameras...")
            items_list = fetch_all_cameras(api_token)
            logger.info(f"Fetched {len(items_list)} cameras.")

        # Output the list as JSON to stdout
        # Use ensure_ascii=False to handle non-ASCII characters correctly
        json.dump(items_list, sys.stdout, indent=4, ensure_ascii=False)
        sys.stdout.write('\n') # Add a newline at the end
        sys.stdout.flush() # Ensure output is written immediately

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
