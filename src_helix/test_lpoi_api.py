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
import io
import contextlib

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
        logger.debug(f"DEBUG: Requesting token with API key: {api_key[:5]}...{api_key[-4:]}")
        response = requests.post(url, headers=headers)
        logger.debug(f"DEBUG: Token response status code: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        logger.debug(f"DEBUG: Token response data keys: {list(data.keys())}")
        return data['token']
    except Exception as e:
        logger.error(f"API token retrieval failed: {e}")
        logger.error(f"DEBUG: Full exception traceback: {traceback.format_exc()}")
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
        logger.debug(f"DEBUG: Request headers: {headers}")
        logger.debug(f"DEBUG: Using API token: {api_token[:10]}...")
        
        response = requests.get(url, headers=headers)
        logger.debug(f"DEBUG: LPOI response status code: {response.status_code}")
        logger.debug(f"DEBUG: LPOI response headers: {dict(response.headers)}")
        
        response.raise_for_status()
        
        # Debug the raw response content
        raw_content = response.content
        logger.debug(f"DEBUG: Raw response content length: {len(raw_content)} bytes")
        logger.debug(f"DEBUG: Raw response content preview: {raw_content[:200]}...")
        
        try:
            data = response.json()
            logger.debug(f"DEBUG: Response JSON parsed successfully")
            logger.debug(f"DEBUG: Response data type: {type(data)}")
            if isinstance(data, dict):
                logger.debug(f"DEBUG: Response data keys: {list(data.keys())}")
                if 'license_plate_of_interest' in data:
                    logger.debug(f"DEBUG: Found 'license_plate_of_interest' key with {len(data['license_plate_of_interest'])} items")
                    logger.debug(f"DEBUG: First few items: {data['license_plate_of_interest'][:3]}")
                else:
                    logger.debug(f"DEBUG: 'license_plate_of_interest' key not found in response")
            elif isinstance(data, list):
                logger.debug(f"DEBUG: Response data is a list with {len(data)} items")
                if data:
                    logger.debug(f"DEBUG: First item keys: {list(data[0].keys()) if isinstance(data[0], dict) else 'Not a dict'}")
            else:
                logger.debug(f"DEBUG: Response data is neither dict nor list: {type(data)}")
        except json.JSONDecodeError as e:
            logger.error(f"DEBUG: Failed to parse JSON response: {e}")
            logger.error(f"DEBUG: Response content: {response.content}")
            raise
        
        # Print the response in pretty format with increased indent width for better readability
        print("\n--- License Plates of Interest API Response ---")
        
        # Instead of printing line by line, which can cause issues with large responses,
        # use a different approach to handle the output
        try:
            # First, limit the number of items to display to prevent overwhelming output
            display_data = data.copy()
            if 'license_plate_of_interest' in display_data and len(display_data['license_plate_of_interest']) > 20:
                # Only show first 20 items to keep output manageable
                original_count = len(display_data['license_plate_of_interest'])
                display_data['license_plate_of_interest'] = display_data['license_plate_of_interest'][:20]
                display_data['_note'] = f"Showing first 20 of {original_count} license plates"
            
            # Temporarily redirect stdout to capture any debug output that might interfere
            with contextlib.redirect_stdout(io.StringIO()):
                # Generate the JSON string
                formatted_json = json.dumps(display_data, indent=2, ensure_ascii=False)
            
            # Now print to the real stdout
            print(formatted_json)
        except Exception as e:
            logger.error(f"DEBUG: Error formatting JSON for display: {e}")
            # Fallback to simple printing if formatting fails
            print("Error formatting full response. See debug log for details.")
            print(f"Response contains {len(data.get('license_plate_of_interest', []))} license plates")
        
        return data
    except requests.exceptions.HTTPError as e:
        logger.error(f"DEBUG: HTTP Error: {e}")
        logger.error(f"DEBUG: Response status code: {e.response.status_code}")
        logger.error(f"DEBUG: Response headers: {dict(e.response.headers)}")
        logger.error(f"DEBUG: Response content: {e.response.content}")
        
        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {LPOI_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        raise
    except Exception as e:
        logger.error(f"DEBUG: Unexpected error: {e}")
        logger.error(f"DEBUG: Error type: {type(e)}")
        logger.error(f"DEBUG: Full exception traceback: {traceback.format_exc()}")
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
    logger.debug("DEBUG: Script started with log level: " + args.log_level)

    # Get API key from environment variable
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set")
        sys.exit(1)
    else:
        logger.debug(f"DEBUG: API_KEY found: {api_key[:5]}...{api_key[-4:]}")

    try:
        # Get API token
        logger.debug("DEBUG: Attempting to get API token...")
        api_token = get_api_token(api_key)
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")
        
        # Fetch LPOI data
        logger.debug("DEBUG: Attempting to fetch LPOI data...")
        
        # Temporarily redirect debug logs to file only during data fetching
        # to prevent mixing with JSON output
        stream_handler = None
        for handler in logger.handlers:
            if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
                stream_handler = handler
                logger.removeHandler(handler)
                break
        
        try:
            lpoi_data = fetch_lpoi_data(api_token)
        finally:
            # Restore the stream handler
            if stream_handler:
                logger.addHandler(stream_handler)
        
        logger.info("Successfully retrieved License Plates of Interest data")

        # Add debug logging for the fetched data structure
        logger.debug(f"DEBUG: Type of fetched data: {type(lpoi_data)}")
        if isinstance(lpoi_data, dict):
            logger.debug(f"DEBUG: Keys in fetched data: {list(lpoi_data.keys())}")
            # Corrected key from 'license_plates_of_interest' (plural) to 'license_plate_of_interest' (singular)
            logger.debug(f"DEBUG: Value for 'license_plate_of_interest' key: {lpoi_data.get('license_plate_of_interest')}")
        else:
            logger.debug("DEBUG: Fetched data is not a dictionary.")

        # Generate and save JSON template if data is available
        # Corrected key from 'license_plates_of_interest' (plural) to 'license_plate_of_interest' (singular)
        lpoi_list = lpoi_data.get('license_plate_of_interest', []) if isinstance(lpoi_data, dict) else []
        logger.debug(f"DEBUG: Length of lpoi_list: {len(lpoi_list)}")

        if lpoi_list:
            logger.debug(f"DEBUG: First LPOI item: {lpoi_list[0]}")
            template_data = create_template(lpoi_list[0])
            logger.debug(f"DEBUG: Template data created: {template_data}")
            
            # Keep the output key as plural for consistency with potential future use, but get data from singular key
            template_output = {"license_plates_of_interest": [template_data]}

            output_filename = "test_lpoi_api.json"
            logger.debug(f"DEBUG: Writing template to {output_filename}")
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning("No License Plates of Interest found to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}")
        logger.error(f"DEBUG: Full exception traceback: {traceback.format_exc()}")
        sys.exit(1)

if __name__ == '__main__':
    main()
