#!/usr/bin/env python3
"""
Script to test the Verkada Cameras API endpoint.
Fetches and prints the list of ALL cameras and saves a JSON template.
"""
import os
import sys
import json
import logging
import argparse

# Import shared utility functions and constants, including configure_logging and save_json_template
# Import fetch_all_cameras from api_utils
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, CAMERAS_ENDPOINT, configure_logging, save_json_template, fetch_all_cameras

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)


def main():
    """
    Main entry point for the script.

    Parses command-line arguments for log level.
    Retrieves the API key from environment variables.
    Obtains an API token.
    Fetches all cameras.
    Prints the camera list.
    Generates and saves a JSON template based on the first camera found.
    Exits with status 0 if successful, 1 on error (including fetch errors).
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Cameras API (Fetches All Cameras)")
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
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)

    # Otherwise, proceed with the standard test script logic
    cameras_list = [] # Initialize to empty list
    try:
        # Get API token using imported function
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch ALL cameras list using the function from api_utils
        logger.info("Attempting to fetch ALL cameras...")
        cameras_list, error_flag = fetch_all_cameras(api_token)

        # Check if an error occurred during fetching
        if error_flag:
            logger.error("Error occurred during pagination while fetching cameras. Data may be incomplete.")
            # Exit with non-zero status to indicate failure
            sys.exit(1)

        logger.info(f"Successfully retrieved ALL cameras. Found {len(cameras_list)} cameras.")

        # Print the full list (or a subset for brevity if needed)
        print("\n--- Cameras API Response (All Cameras) ---")
        # Be cautious printing very large lists; consider printing only the first few items
        # or just the count in non-debug modes. For now, printing all.
        print(json.dumps(cameras_list, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON


        # Generate and save JSON template if data is available
        if cameras_list:
            logger.debug("cameras_list is not empty, attempting to generate template.")
            output_filename = "src_helix/api-json/test_cameras_api.json"
            save_json_template(cameras_list[0], output_filename, wrap_key="cameras")
        else:
            logger.warning("No cameras found to generate a template.")

    except Exception as e:
        # Log the execution failure
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
