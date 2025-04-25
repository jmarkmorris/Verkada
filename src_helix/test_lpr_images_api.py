#!/usr/bin/env python3
"""
Script to test the Verkada LPR Images API endpoint.
"""
import os
import sys
import json
import logging
import requests
import argparse
import time
import traceback # Import traceback

# Import shared utility functions and constants
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL

# Get the logger for this module
logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG) # Set logger level to DEBUG

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix directory
file_handler = logging.FileHandler('src_helix/lpr_images_api_debug.log')
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


LPR_IMAGES_ENDPOINT = "/cameras/v1/analytics/lpr/imagesview"

def fetch_lpr_images_data(api_token: str, history_days: int):
    """Fetch LPR images data from Verkada API."""
    end_time = int(time.time())
    start_time = end_time - (history_days * 24 * 60 * 60)

    url = f"{VERKADA_API_BASE_URL}{LPR_IMAGES_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }
    params = {
        "start_time": start_time,
        "end_time": end_time,
        "page_size": 200 # Example page size, adjust as needed
    }

    try:
        logger.info(f"Fetching LPR images from {url} for the last {history_days} days")
        logger.debug(f"Request headers: {headers}") # Added debug log
        logger.debug(f"Request parameters: {params}") # Added debug log
        logger.debug(f"Using API token: {api_token[:10]}...") # Added debug log

        response = requests.get(url, headers=headers, params=params)
        logger.debug(f"LPR images response status code: {response.status_code}") # Added debug log
        logger.debug(f"LPR images response headers: {dict(response.headers)}") # Added debug log

        response.raise_for_status()
        data = response.json()

        logger.debug(f"Raw LPR images response data: {data}") # Added debug log

        # Print the response in pretty format
        print("\n--- LPR Images API Response ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e}") # Added detailed error logging
        logger.error(f"Response status code: {e.response.status_code}") # Added detailed error logging
        logger.error(f"Response headers: {dict(e.response.headers)}") # Added detailed error logging
        logger.error(f"Response content: {e.response.content}") # Added detailed error logging

        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {LPR_IMAGES_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise
    except Exception as e: # Catch other potential exceptions during fetch/json parsing
        logger.error(f"Unexpected error during LPR images fetch: {e}", exc_info=True) # Added traceback
        raise

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada LPR Images API")
    parser.add_argument(
        "--history_days",
        type=int,
        default=7,
        help="Number of days of history to query (default: 7)"
    )
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
    logger.debug(f"Stream handler level set to: {args.log_level}") # Added debug log


    # Get API key from environment variable
    logger.debug("Attempting to get API_KEY environment variable...") # Added debug log
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)
    else:
        logger.debug(f"API_KEY found: {api_key[:5]}...{api_key[-4:]}") # Added debug log

    try:
        # Get API token
        logger.debug("Attempting to get API token...") # Added debug log
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch LPR images data
        logger.debug("Attempting to fetch LPR images data...") # Added debug log
        lpr_images_data = fetch_lpr_images_data(api_token, args.history_days)
        logger.info("Successfully retrieved LPR images data")

        # Add debug logging for the fetched data structure
        logger.debug(f"Type of fetched data: {type(lpr_images_data)}")
        if isinstance(lpr_images_data, list):
            logger.debug(f"Number of items in fetched data: {len(lpr_images_data)}")
            if lpr_images_data:
                logger.debug(f"First item keys: {list(lpr_images_data[0].keys()) if isinstance(lpr_images_data[0], dict) else 'Not a dict'}")
        else:
            logger.debug("Fetched data is not a list.")


        # Generate and save JSON template if data is available
        # Assuming the key for the list of LPR images/events is 'lpr_events' or similar
        # Based on API docs, it seems the response is a list directly, not wrapped in a dict.
        # Let's assume it's a list of dictionaries.
        lpr_images_list = lpr_images_data if isinstance(lpr_images_data, list) else []
        logger.debug(f"Length of lpr_images_list: {len(lpr_images_list)}") # Added debug log

        if lpr_images_list:
            logger.debug("lpr_images_list is not empty, attempting to generate template.") # Added debug log
            template_data = create_template(lpr_images_list[0])
            logger.debug(f"Template data created: {template_data}") # Added debug log

            # Wrap in a list for the template output
            template_output = [template_data]

            # Save the template to the src_helix directory
            output_filename = "src_helix/api-json/test_lpr_images_api.json"
            logger.debug(f"Writing template to {output_filename}") # Added debug log
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No LPR images found to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
