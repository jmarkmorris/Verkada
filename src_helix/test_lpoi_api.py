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
# import io # Removed unused import
# import contextlib # Removed unused import

# Import shared utility functions and constants
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
log_file_path = os.path.join(LOGS_DIR, 'lpoi_api_debug.log')

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


# Removed basicConfig call
# logging.basicConfig(...)

# VERKADA_API_BASE_URL = "https://api.verkada.com" # Removed, imported from api_utils
# TOKEN_ENDPOINT = "/token" # Removed, imported from api_utils
LPOI_ENDPOINT = "/cameras/v1/analytics/lpr/license_plate_of_interest"

# def get_api_token(api_key: str) -> str: # Removed, imported from api_utils
#     """Fetch short-lived API token."""
#     url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
#     headers = {
#         "Accept": "application/json",
#         "x-api-key": api_key,
#     }
#
#     try:
#         logger.debug(f"Requesting token with API key: {api_key[:5]}...{api_key[-4:]}")
#         response = requests.post(url, headers=headers)
#         logger.debug(f"Token response status code: {response.status_code}")
#         response.raise_for_status()
#         data = response.json()
#         logger.debug(f"Token response data keys: {list(data.keys())}")
#         return data['token']
#     except Exception as e:
#         logger.error(f"API token retrieval failed: {e}")
#         logger.error(f"Full exception traceback: {traceback.format_exc()}")
#         raise

# def create_template(data: dict) -> dict: # Removed, imported from api_utils
#     """Recursively create a template dictionary with empty values."""
#     template = {}
#     for key, value in data.items():
#         if isinstance(value, dict):
#             template[key] = create_template(value)
#         elif isinstance(value, list):
#             # For lists, create a list containing one template item if the list is not empty
#             template[key] = [create_template(value[0])] if value else []
#         elif isinstance(value, str):
#             template[key] = ""
#         elif isinstance(value, (int, float)):
#             template[key] = 0
#         elif isinstance(value, bool):
#             template[key] = False # Or None, depending on desired empty state for boolean
#         else:
#             template[key] = None # Handles None and other types
#
#     return template


def fetch_lpoi_data(api_token: str) -> tuple[dict | None, list]:
    """
    Fetch ALL License Plates of Interest from Verkada API, handling pagination.
    Returns a tuple: (raw_first_page_data, all_lpoi_items_list).
    raw_first_page_data is the dictionary response from the first page fetch,
    or None if the first fetch fails.
    all_lpoi_items_list is the accumulated list of all LPOI items from all pages.
    """
    url = f"{VERKADA_API_BASE_URL}{LPOI_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }
    all_lpoi = []
    page_token = None
    page_count = 0
    raw_first_page_data = None # Store the raw data from the first page

    logger.info(f"Fetching License Plates of Interest from {url}")

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
            logger.debug(f"Request headers: {headers}")
            logger.debug(f"Request parameters: {params}")
            logger.debug(f"Using API token: {api_token[:10]}...")

            response = requests.get(url, headers=headers, params=params)
            logger.debug(f"LPOI response status code for page {page_count + 1}: {response.status_code}")
            response.raise_for_status()

            # Debug the raw response content length
            raw_content = response.content
            logger.debug(f"Raw response content length for page {page_count + 1}: {len(raw_content)} bytes")

            try:
                data = response.json()
                logger.debug(f"Response JSON parsed successfully for page {page_count + 1}")
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

            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response for page {page_count + 1}: {e}")
                logger.error(f"Response content: {response.content}")
                # Stop pagination on JSON error
                break

            page_count += 1

            if page_token:
                logger.debug(f"Next page token found: {page_token}. Continuing pagination.")
                # Optional: Add a small delay to avoid hitting rate limits
                # time.sleep(0.1)
            else:
                logger.debug(f"No next page token found. Ending pagination.")
                break # No more pages

        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error fetching LPOI, page {page_count + 1}: {e}")
            logger.error(f"Response status code: {e.response.status_code}")
            logger.error(f"Response headers: {dict(e.response.headers)}")
            logger.error(f"Response content: {e.response.content}")
            # Decide whether to stop or continue on error
            # For now, we'll log and stop fetching
            break
        except Exception as e:
            logger.error(f"Unexpected error fetching LPOI, page {page_count + 1}: {e}", exc_info=True)
            # Stop pagination on unexpected error
            break

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

    # Set logging level for the stream handler based on the argument.
    # The file handler level is already set to DEBUG.
    stream_handler.setLevel(getattr(logging, args.log_level))
    logger.debug(f"Stream handler level set to: {args.log_level}")

    # Get API key from environment variable
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
            template_data = create_template(lpoi_list[0])
            logger.debug(f"Template data created: {template_data}")

            # Keep the output key as plural for consistency with potential future use, but get data from singular key
            template_output = {"license_plates_of_interest": [template_data]}

            # Save the template to the src_helix directory
            output_filename = "src_helix/api-json/test_lpoi_api.json"
            logger.debug(f"Writing template to {output_filename}")
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No License Plates of Interest found to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}")
        logger.error(f"Full exception traceback: {traceback.format_exc()}")
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
