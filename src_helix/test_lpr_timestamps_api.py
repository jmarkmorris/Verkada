#!/usr/bin/env python3
"""
Script to test the Verkada LPR Timestamps API endpoint.
Fetches timestamps for a specific license plate.
"""
import os
import sys
import json
import logging
import requests
import argparse
import time
import datetime
import traceback

# Configure logging
# Set root logger level to DEBUG to ensure all messages are processed by handlers.
# Handler levels will be set separately to control output destinations.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        # Stream handler for stdout - level will be set based on user input.
        logging.StreamHandler(sys.stdout),
        # File handler for debug logs - always log DEBUG and above to file.
        logging.FileHandler('lpr_timestamps_api_debug.log') # Log file name
    ]
)
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
LPR_TIMESTAMPS_ENDPOINT = "/cameras/v1/analytics/lpr/timestamps" # Endpoint for timestamps

def get_api_token(api_key: str) -> str:
    """Fetch short-lived API token."""
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        logger.debug(f"Requesting token with API key: {api_key[:5]}...{api_key[-4:]}")
        response = requests.post(url, headers=headers)
        logger.debug(f"Token response status code: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        logger.debug(f"Token response data keys: {list(data.keys())}")
        return data['token']
    except Exception as e:
        logger.error(f"API token retrieval failed: {e}")
        logger.error(f"Full exception traceback: {traceback.format_exc()}")
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


def fetch_lpr_timestamps_data(api_token: str, camera_id: str, license_plate: str, history_days: int):
    """Fetch LPR timestamps data for a specific license plate from Verkada API."""
    end_time = int(time.time())
    start_time = end_time - (history_days * 24 * 60 * 60)

    url = f"{VERKADA_API_BASE_URL}{LPR_TIMESTAMPS_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    params = {
        "camera_id": camera_id, # camera_id is a required parameter
        "license_plate": license_plate,
        "start_time": start_time,
        "end_time": end_time,
        "page_size": 100 # Re-adding page_size, trying a smaller value
    }

    try:
        logger.info(f"Fetching LPR timestamps for plate '{license_plate}' on camera '{camera_id}' from {url} for the last {history_days} days")
        logger.debug(f"Request headers: {headers}")
        logger.debug(f"Request parameters: {params}")
        logger.debug(f"Using API token: {api_token[:10]}...")
        logger.debug(f"Date range: {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)}")

        response = requests.get(url, headers=headers, params=params)
        logger.debug(f"LPR timestamps response status code: {response.status_code}")
        logger.debug(f"LPR timestamps response headers: {dict(response.headers)}")

        response.raise_for_status()

        # Debug the raw response content
        raw_content = response.content
        logger.debug(f"Raw response content length: {len(raw_content)} bytes")
        logger.debug(f"Raw response content preview: {raw_content[:200]}...")

        try:
            data = response.json()
            logger.debug(f"Response JSON parsed successfully")
            logger.debug(f"Response data type: {type(data)}")
            if isinstance(data, dict):
                logger.debug(f"Response data keys: {list(data.keys())}")
                if 'timestamps' in data:
                    logger.debug(f"Found 'timestamps' key with {len(data['timestamps'])} items")
                    # Avoid printing potentially large list in debug log
                    # logger.debug(f"First few timestamps: {data['timestamps'][:3] if len(data['timestamps']) > 0 else 'No timestamps'}")
                else:
                    logger.debug(f"'timestamps' key not found in response")
            elif isinstance(data, list):
                logger.debug(f"Response data is a list with {len(data)} items")
                if data:
                    # Avoid printing potentially large list in debug log
                    # logger.debug(f"First item keys: {list(data[0].keys()) if isinstance(data[0], dict) else 'Not a dict'}")
                    pass
            else:
                logger.debug(f"Response data is neither dict nor list: {type(data)}")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            logger.error(f"Response content: {response.content}")
            raise

        # Print the response in pretty format
        print(f"\n--- LPR Timestamps API Response for '{license_plate}' ---")
        # Use ensure_ascii=False to correctly display non-ASCII characters
        print(json.dumps(data, indent=4, ensure_ascii=False))
        sys.stdout.flush() # Explicitly flush stdout after printing JSON

        return data
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e}")
        logger.error(f"Response status code: {e.response.status_code}")
        logger.error(f"Response headers: {dict(e.response.headers)}")
        logger.error(f"Response content: {e.response.content}")

        if e.response.status_code == 403:
            logger.error(f"403 Forbidden error for {LPR_TIMESTAMPS_ENDPOINT}. Possible permission issue.")
            logger.error("Troubleshooting steps:")
            logger.error("1. Check your API key permissions in Verkada Command")
            logger.error("2. Ensure you have the correct access level for this endpoint")
            logger.error("3. Verify the API key is not expired")
        elif e.response.status_code == 404:
             logger.error(f"404 Not Found error for {LPR_TIMESTAMPS_ENDPOINT}. License plate '{license_plate}' may not exist or have no timestamps in the given range.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        logger.error(f"Error type: {type(e)}")
        logger.error(f"Full exception traceback: {traceback.format_exc()}")
        raise

def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada LPR Timestamps API")
    parser.add_argument(
        "--camera_id",
        required=True,
        help="The unique identifier of the camera (required)"
    )
    parser.add_argument(
        "--license_plate",
        required=True,
        help="The license plate to fetch timestamps for (required)"
    )
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
    # Removed --list-for-menu as it's handled by test_cameras_api.py now

    # Parse arguments
    args = parser.parse_args()

    # Set logging level for the stream handler based on the argument.
    # The root logger is already set to DEBUG in basicConfig.
    # Find the stream handler and set its level.
    stream_handler = None
    for handler in logging.getLogger().handlers:
        if isinstance(handler, logging.StreamHandler):
            stream_handler = handler
            break
    if stream_handler:
        stream_handler.setLevel(getattr(logging, args.log_level))

    logger.debug("Script started with log level: " + args.log_level)
    logger.debug(f"Arguments: camera_id={args.camera_id}, license_plate={args.license_plate}, history_days={args.history_days}")

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

        # Fetch LPR timestamps data
        logger.debug("Attempting to fetch LPR timestamps data...")
        # Removed temporary stream handler removal/re-addition logic
        lpr_timestamps_data = fetch_lpr_timestamps_data(api_token, args.camera_id, args.license_plate, args.history_days)
        logger.info(f"Successfully retrieved LPR timestamps data for plate '{args.license_plate}' on camera '{args.camera_id}'")

        # Generate and save JSON template if data is available
        # Assuming the key for the list of timestamps is 'timestamps'
        timestamps_list = lpr_timestamps_data.get('timestamps', []) if isinstance(lpr_timestamps_data, dict) else []
        logger.debug(f"Number of timestamps found: {len(timestamps_list)}")

        if timestamps_list:
            logger.debug(f"First timestamp item: {timestamps_list[0]}")
            template_data = create_template(timestamps_list[0])
            logger.debug(f"Template data created: {template_data}")

            template_output = {"timestamps": [template_data]} # Wrap in the expected list structure

            # Save the template to the src_helix directory
            output_filename = "src_helix/test_lpr_timestamps_api.json"
            logger.debug(f"Writing template to {output_filename}")
            with open(output_filename, 'w') as f:
                json.dump(template_output, f, indent=4)
            logger.info(f"Generated JSON template: {output_filename}")
        else:
            logger.warning(f"No timestamps found for plate '{args.license_plate}' on camera '{args.camera_id}' to generate a template.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}")
        logger.error(f"Full exception traceback: {traceback.format_exc()}")
        sys.exit(1)

if __name__ == '__main__':
    main()
