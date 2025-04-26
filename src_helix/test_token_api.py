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
# get_api_token now returns the full data dictionary
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, TOKEN_ENDPOINT

# Get the logger for this module
logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG)

# Define the logs directory path
LOGS_DIR = 'src_helix/logs'

# Ensure the logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter) # Set formatter for stream handler

# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix/logs directory
log_file_path = os.path.join(LOGS_DIR, 'token_api_debug.log')

# Create file handler, handling potential errors
try:
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG) # File handler always logs DEBUG and above
    file_handler.setFormatter(formatter) # Set formatter for file handler

    # Add handlers to the logger
    # Prevent duplicate handlers if the script is somehow imported multiple times
    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

except Exception as e:
    # If file handler creation fails, log an error to the console (via stream_handler)
    # and continue without the file handler.
    logger.error(f"Failed to create file handler for {log_file_path}: {e}")


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

    token_data = None # Initialize to None
    try:
        # Get API token - get_api_token now returns the full data dictionary
        logger.debug("Attempting to get API token...")
        token_data = get_api_token(api_key)
        # Log the token itself from the returned data
        retrieved_token = token_data.get('token', 'N/A')
        logger.info(f"Successfully retrieved API token: {retrieved_token[:10]}...")
        logger.debug(f"Retrieved API token data: {token_data}")


        # Print the response in pretty format
        print("\n--- Token API Response ---")
        # Print the data returned by get_api_token
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
            try:
                with open(output_filename, 'w') as f:
                    json.dump(template_data, f, indent=4)
                logger.info(f"Generated JSON template: {output_filename}")
            except Exception as write_e:
                logger.error(f"Failed to write JSON template to {output_filename}: {write_e}", exc_info=True)
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
