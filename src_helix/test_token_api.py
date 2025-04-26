#!/usr/bin/env python3
"""
Script to test the Verkada Token API endpoint.
"""
import os # Import os
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

# Define the logs directory path
LOGS_DIR = 'src_helix/logs'

# Add diagnostic prints for directory creation
print(f"DEBUG (token): Attempting to create log directory: {LOGS_DIR}", file=sys.stderr)

# Ensure the logs directory exists
try:
    os.makedirs(LOGS_DIR, exist_ok=True)
    print(f"DEBUG (token): Log directory created or already exists: {LOGS_DIR}", file=sys.stderr)
except Exception as e:
    print(f"ERROR (token): Failed to create log directory {LOGS_DIR}: {e}", file=sys.stderr)
    # Note: We don't exit here, just report the error and continue.

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter) # Set formatter for stream handler

# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix/logs directory
log_file_path = os.path.join(LOGS_DIR, 'token_api_debug.log')

# Add diagnostic prints for file handler creation
print(f"DEBUG (token): Attempting to create file handler for: {log_file_path} (Absolute: {os.path.abspath(log_file_path)})", file=sys.stderr)

try:
    file_handler = logging.FileHandler(log_file_path)
    print(f"DEBUG (token): File handler created successfully for: {log_file_path}", file=sys.stderr)
    file_handler.setLevel(logging.DEBUG) # File handler always logs DEBUG and above
    file_handler.setFormatter(formatter) # Set formatter for file handler

    # Add handlers to the logger
    # Prevent duplicate handlers if the script is somehow imported multiple times
    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        print("DEBUG (token): Handlers added to logger.", file=sys.stderr)
    else:
         print("DEBUG (token): Logger already has handlers.", file=sys.stderr)

except Exception as e:
    print(f"ERROR (token): Failed to create file handler for {log_file_path}: {e}", file=sys.stderr)
    # If file handler creation fails, logging to file won't work.
    # The script will continue, but file logs will be missing.


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Token API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR', # Changed default to ERROR
        help="Set the logging level (default: ERROR)" # Updated help text
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

        # Re-fetch the data to get the full response for templating
        # This is slightly inefficient but keeps get_api_token focused
        url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
        headers = {
            "Accept": "application/json",
            "x-api-key": api_key,
        }
        logger.debug(f"Re-fetching token data from {url} for templating...")
        response = requests.post(url, headers=headers)
        logger.debug(f"Token re-fetch response status code: {response.status_code}")
        logger.debug(f"Token re-fetch response headers: {dict(response.headers)}")

        response.raise_for_status()
        token_data = response.json()
        logger.debug("Successfully re-fetched token data for templating.")
        logger.debug(f"Raw token re-fetch data: {token_data}")


        # Print the response in pretty format
        print("\n--- Token API Response ---")
        print(json.dumps(token_data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON


        # Generate and save JSON template
        if token_data:
            logger.debug("Generating JSON template...")
            template_data = create_template(token_data)
            logger.debug(f"Template data created: {template_data}")
            # Save the template to the src_helix directory
            output_filename = "src_helix/api-json/test_token_api.json"
            logger.debug(f"Writing template to {output_filename}")
            with open(output_filename, 'w') as f:
                json.dump(template_data, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No data returned from Token API to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
