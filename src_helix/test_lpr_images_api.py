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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        # Save log file in the src_helix directory
        logging.FileHandler('src_helix/lpr_images_api_debug.log')
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
LPR_IMAGES_ENDPOINT = "/cameras/v1/analytics/lpr/imagesview"

def get_api_token(api_key: str) -> str:
    """Fetch short-lived API token."""
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['token']
    except Exception as e:
        logger.error(f"API token retrieval failed: {e}")
        raise

def create_template(data: dict) -> dict:
    """Recursively create a template dictionary with empty values."""
    template = {}
    for key, value in data.items():
        if isinstance(value, dict):
            template[key] = create_template(value)
        elif isinstance(value, list):
            # For lists, create a list containing one template item if the list is not empty
            template[key] = [create_template(value[0])] if value else []
        elif isinstance(value, str):
            template[key] = ""
        elif isinstance(value, (int, float)):
            template[key] = 0
        elif isinstance(value, bool):
            template[key] = False # Or None, depending on desired empty state for boolean
        else:
            template[key] = None # Handles None and other types

    return template


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
        "page_size": 200
    }

    try:
        logger.info(f"Fetching LPR images from {url} for the last {history_days} days")
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Print the response in pretty format
        print("\n--- LPR Images API Response ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {LPR_IMAGES_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
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
        default='INFO',
        help="Set the logging level (default: INFO)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Set logging level
    logging.getLogger().setLevel(getattr(logging, args.log_level))

    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)

    try:
        # Get API token
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Fetch LPR images data
        lpr_images_data = fetch_lpr_images_data(api_token, args.history_days)
        logger.info("Successfully retrieved LPR images data")

        # Generate and save JSON template if data is available
        # Assuming the key for the list of LPR images/events is 'lpr_events' or similar
        # Based on API docs, it seems the response is a list directly, not wrapped in a dict.
        # Let's assume it's a list of dictionaries.
        lpr_images_list = lpr_images_data if isinstance(lpr_images_data, list) else []

        if lpr_images_list:
            template_data = create_template(lpr_images_list[0])
            # Wrap in a list for the template output
            template_output = [template_data]

            # Save the template to the src_helix directory
            output_filename = "src_helix/test_lpr_images_api.json"
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
