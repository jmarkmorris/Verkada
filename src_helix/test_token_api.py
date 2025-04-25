#!/usr/bin/env python3
"""
Script to test the Verkada Token API endpoint.
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
file_handler = logging.FileHandler('src_helix/api-json/token_api_debug.log')
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

if __name__ == '__main__':
    main()
