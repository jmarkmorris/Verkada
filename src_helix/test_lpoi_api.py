#!/usr/bin/env python3
"""
Script to test the Verkada License Plates of Interest API endpoint.
"""
import os
import sys
import json
import logging
import requests
import argparse
import traceback

# Import shared utility functions and the centralized logging function and save_json_template
# Import _fetch_data from api_utils
from src_helix.api_utils import get_api_token, create_template, VERKADA_API_BASE_URL, LPOI_ENDPOINT, _fetch_data, configure_logging, save_json_template

# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)

# Removed the old logging setup code (handlers, formatters, addHandler calls)


def fetch_lpoi_data(api_token: str) -> tuple[dict | None, list]:
    """
    Fetch ALL License Plates of Interest from Verkada API, handling pagination.
    Returns a tuple: (raw_first_page_data, all_lpoi_items_list).
    raw_first_page_data is the dictionary response from the first page fetch,
    or None if the first fetch fails.
    all_lpoi_items_list is the accumulated list of all LPOI items from all pages.
    """
    all_lpoi = []
    page_token = None
    page_count = 0
    raw_first_page_data = None # Store the raw data from the first page

    logger.info(f"Fetching License Plates of Interest from {LPOI_ENDPOINT}")

    while True:
        params = {
            "page_size": 1000 # Use max page size
        }
        if page_token:
            params["page_token"] = page_token
            logger.debug(f"Fetching page {page_count + 1} with page_token: {page_token}")
        else:
             logger.debug(f"Fetching initial page {page_count + 1}")

        try:
            # Use the new _fetch_data function
            data = _fetch_data(api_token, LPOI_ENDPOINT, method='GET', params=params)

            logger.debug(f"Response data type: {type(data)}")

            if page_count == 0:
                raw_first_page_data = data # Store the raw data from the first page

            if isinstance(data, dict):
                logger.debug(f"Response data keys: {list(data.keys())}")
                # The API response structure is a dictionary with 'license_plate_of_interest' key
                current_page_items = data.get('license_plate_of_interest', [])
                if not isinstance(current_page_items, list):
                     logger.warning(f"Expected 'license_plate_of_interest' list in response for page {page_count + 1}, but got {type(current_page_items)}. Stopping pagination.")
                     break # Stop if the key is not a list

                logger.debug(f"Found 'license_plate_of_interest' key with {len(current_page_items)} items on page {page_count + 1}")
                all_lpoi.extend(current_page_items)
                logger.debug(f"Added {len(current_page_items)} items from page {page_count + 1}. Total LPOI fetched so far: {len(all_lpoi)}")

                page_token = data.get('next_page_token') # Get next page token from the dictionary
            else:
                logger.warning(f"Response data for page {page_count + 1} is not a dictionary: {type(data)}. Stopping pagination.")
                break # Stop if the response is not a dictionary

            page_count += 1

            if page_token:
                logger.debug(f"Next page token found: {page_token}. Continuing pagination.")
                # Optional: Add a small delay to avoid hitting rate limits
                # time.sleep(0.1)
            else:
                logger.debug(f"No next page token found. Ending pagination.")
                break # No more pages

        except Exception as e:
            # _fetch_data already logged the specific error (HTTP, JSON, etc.)
            # Log a higher-level error here and stop pagination
            logger.error(f"Failed to fetch LPOI, page {page_count + 1}: {e}")
            break # Stop pagination on any error

    logger.info(f"Finished fetching License Plates of Interest. Total LPOI fetched: {len(all_lpoi)}")
    # Avoid printing the full list here to keep output clean when imported.
    # Debug logs already capture the raw data per page.

    # Return the raw data from the first page and the accumulated list
    return raw_first_page_data, all_lpoi

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada License Plates of Interest API")
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

    raw_lpoi_data = None # Initialize to None
    lpoi_list = [] # Initialize to empty list
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch LPOI data - fetch_lpoi_data now returns raw data and the list
        logger.debug("Attempting to fetch LPOI data...")
        raw_lpoi_data, lpoi_list = fetch_lpoi_data(api_token)

        logger.info("Successfully retrieved License Plates of Interest data")

        # Print the raw response in pretty format if available
        if raw_lpoi_data is not None:
            print("\n--- LPOI API Response (First Page) ---")
            print(json.dumps(raw_lpoi_data, indent=4))
            sys.stdout.flush() # Explicitly flush stdout after printing JSON
        else:
            logger.warning("Could not retrieve raw LPOI data to print.")


        # Add debug logging for the fetched data structure (the list)
        logger.debug(f"Type of fetched data list: {type(lpoi_list)}")
        if isinstance(lpoi_list, list):
            logger.debug(f"Length of fetched data list: {len(lpoi_list)}")
            if lpoi_list:
                logger.debug(f"First item keys: {list(lpoi_list[0].keys()) if isinstance(lpoi_list[0], dict) else 'Not a dict'}")
        else:
            logger.debug("Fetched data is not a list.")


        # Generate and save JSON template if data is available
        # Corrected key from 'license_plates_of_interest' (plural) to 'license_plate_of_interest' (singular)
        # Avoid printing the full list in debug log
        # logger.debug(f"Value for 'license_plate_of_interest' key: {lpoi_data.get('license_plate_of_interest')}")


        logger.debug(f"Length of lpoi_list for template generation: {len(lpoi_list)}")

        if lpoi_list:
            logger.debug("First LPOI item for template: {lpoi_list[0]}")
            # Use the centralized save_json_template function
            output_filename = "src_helix/api-json/test_lpoi_api.json"
            # Pass the first item of the list and the key to wrap it with (using the plural key for the template file)
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
