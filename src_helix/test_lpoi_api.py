#!/usr/bin/env python3
"""
Script to test the Verkada License Plates of Interest API endpoint.
Fetches ALL LPOI items and saves a JSON template.
"""
import os
import sys
import json
import logging
import requests
import argparse
import traceback

# Import shared utility functions and the centralized logging function and save_json_template
# Import fetch_all_lpoi from api_utils
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, LPOI_ENDPOINT, configure_logging, save_json_template, fetch_all_lpoi

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada License Plates of Interest API (Fetches All)")
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO',
        help="Set the logging level (default: INFO)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Configure logging using the centralized function
    configure_logging(args.log_level)

    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)
    else:
        logger.debug(f"API_KEY found: {api_key[:5]}...{api_key[-4:]}")

    lpoi_list = [] # Initialize to empty list
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch ALL LPOI data using the function from api_utils
        logger.info("Attempting to fetch ALL LPOI data...")
        lpoi_list, error_flag = fetch_all_lpoi(api_token)

        # Check if an error occurred during fetching
        if error_flag:
            logger.error("Error occurred during pagination while fetching LPOI list. Data may be incomplete.")
            # Exit with non-zero status to indicate failure
            sys.exit(1)

        logger.info(f"Successfully retrieved ALL License Plates of Interest. Found {len(lpoi_list)} items.")

        # Print the full list (or a subset for brevity if needed)
        print("\n--- LPOI API Response (All Items) ---")
        # Be cautious printing very large lists; consider printing only the first few items
        # or just the count in non-debug modes. For now, printing all.
        print(json.dumps(lpoi_list, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON


        # Add debug logging for the fetched data structure (the list)
        logger.debug(f"Type of fetched data list: {type(lpoi_list)}")
        if isinstance(lpoi_list, list):
            logger.debug(f"Length of fetched data list: {len(lpoi_list)}")
            if lpoi_list:
                logger.debug(f"First item keys: {list(lpoi_list[0].keys()) if isinstance(lpoi_list[0], dict) else 'Not a dict'}")
        else:
            logger.debug("Fetched data is not a list.")


        # Generate and save JSON template if data is available
        logger.debug(f"Length of lpoi_list for template generation: {len(lpoi_list)}")

        if lpoi_list:
            logger.debug(f"First LPOI item for template: {lpoi_list[0]}")
            output_filename = "src_helix/api-json/test_lpoi_api.json"
            save_json_template(lpoi_list[0], output_filename, wrap_key="license_plates_of_interest")
        else:
            logger.warning("No License Plates of Interest found to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}")
        logger.error(f"Full exception traceback: {traceback.format_exc()}")
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
