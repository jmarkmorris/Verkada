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

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('token_api_debug.log')
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"

def get_api_token(api_key: str) -> str:
    """Fetch short-lived API token."""
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        logger.info(f"Requesting token from {url}")
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Print the response in pretty format
        print("\n--- Token API Response ---")
        print(json.dumps(data, indent=4))
        
        return data['token']
    except Exception as e:
        logger.error(f"API token retrieval failed: {e}")
        raise

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada Token API")
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
    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
