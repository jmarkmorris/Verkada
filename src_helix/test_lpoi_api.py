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
        
        # Print the response in pretty format
        print("\n--- License Plates of Interest API Response ---")
        print(json.dumps(data, indent=4))
        
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
    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
