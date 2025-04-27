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

# Import shared utility functions and constants, including configure_logging and save_json_template
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, TOKEN_ENDPOINT, configure_logging, save_json_template

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Token API")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR',
        help="Set the logging level (default: ERROR)"
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

    token_data = None # Initialize to None
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        token_data = get_api_token(api_key)
        # Log the token itself from the returned data
        retrieved_token = token_data.get('token', 'N/A')
        logger.info(f"Successfully retrieved API token: {retrieved_token[:10]}...")
        logger.debug(f"Retrieved API token data: {token_data}")


        # Print the response in pretty format
        print("\n--- Token API Response ---")
        print(json.dumps(token_data, indent=4))
        sys.stdout.flush()


        # Generate and save JSON template
        if token_data:
            logger.debug("Generating JSON template...")
            output_filename = "src_helix/api-json/test_token_api.json"
            save_json_template(token_data, output_filename)
        else:
            logger.warning("No data returned from Token API to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
