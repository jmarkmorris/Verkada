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

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('lpoi_api_debug.log')
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
LPOI_ENDPOINT = "/cameras/v1/analytics/lpr/license_plate_of_interest"

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


def fetch_lpoi_data(api_token: str):
    """Fetch License Plates of Interest from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{LPOI_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching License Plates of Interest from {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Print the response in pretty format with increased indent width for better readability
        print("\n--- License Plates of Interest API Response ---")
        print(json.dumps(data, indent=4, ensure_ascii=False))
        
        return data
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {LPOI_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise

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
        
        # Fetch LPOI data
        lpoi_data = fetch_lpoi_data(api_token)
        logger.info("Successfully retrieved License Plates of Interest data")

        # Add debug logging for the fetched data structure
        logger.debug(f"Type of fetched data: {type(lpoi_data)}")
        if isinstance(lpoi_data, dict):
            logger.debug(f"Keys in fetched data: {list(lpoi_data.keys())}")
            # Corrected key from 'license_plates_of_interest' (plural) to 'license_plate_of_interest' (singular)
            logger.debug(f"Value for 'license_plate_of_interest' key: {lpoi_data.get('license_plate_of_interest')}")
        else:
            logger.debug("Fetched data is not a dictionary.")


        # Generate and save JSON template if data is available
        # Corrected key from 'license_plates_of_interest' (plural) to 'license_plate_of_interest' (singular)
        lpoi_list = lpoi_data.get('license_plate_of_interest', []) if isinstance(lpoi_data, dict) else []
        logger.debug(f"Length of lpoi_list: {len(lpoi_list)}")

        if lpoi_list:
            template_data = create_template(lpoi_list[0])
            # Keep the output key as plural for consistency with potential future use, but get data from singular key
            template_output = {"license_plates_of_interest": [template_data]}

            output_filename = "test_lpoi_api.json"
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No License Plates of Interest found to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
