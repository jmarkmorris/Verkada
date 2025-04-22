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
        # Save log file in the src_helix directory
        logging.FileHandler('src_helix/token_api_debug.log')
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
        logger.info(f"Requesting token from {url}") # Keep this one as it's the primary purpose of this script
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Print the response in pretty format
        print("\n--- Token API Response ---")
        print(json.dumps(data, indent=4))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

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
        # Get API token and the full response data
        # Modify get_api_token to return the full data, not just the token string
        # Or, fetch data again if get_api_token must return only the token
        # Let's modify get_api_token to return the full data for simplicity here
        # NOTE: This requires a change to get_api_token signature/return type
        # Let's instead fetch the data again in main for clarity.

        # Get API token (assuming get_api_token still returns just the token string)
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Re-fetch the data to get the full response for templating
        # This is slightly inefficient but keeps get_api_token focused
        url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
        headers = {
            "Accept": "application/json",
            "x-api-key": api_key,
        }
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        token_data = response.json()

        # Generate and save JSON template
        if token_data:
            template_data = create_template(token_data)
            # Save the template to the src_helix directory
            output_filename = "src_helix/test_token_api.json"
            with open(output_filename, 'w') as f:
                json.dump(template_data, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No data returned from Token API to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
