import json
import logging
import requests
import traceback
import sys # Import sys for stream handler

logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG)

# Create handlers for the api_utils logger
# Stream handler for stdout (optional, but useful for immediate feedback)
# Level will be set based on the calling script's configuration if propagation is enabled,
# or can be set here if needed. Let's set it to WARNING by default for this handler.
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.WARNING) # Default stream level for api_utils

# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix directory
file_handler = logging.FileHandler('src_helix/api_utils_debug.log')
file_handler.setLevel(logging.DEBUG) # File handler always logs DEBUG and above

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
# Prevent duplicate handlers if the module is somehow imported multiple times
if not logger.handlers:
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"

def get_api_token(api_key: str) -> str:
    """Fetch short-lived API token from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{TOKEN_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key,
    }

    try:
        logger.debug(f"Requesting token from {url} with API key: {api_key[:5]}...{api_key[-4:]}")
        response = requests.post(url, headers=headers)
        logger.debug(f"Token response status code: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        logger.debug(f"Token response data keys: {list(data.keys())}")
        return data['token']
    except Exception as e:
        # This error is now logged to src_helix/api_utils_debug.log
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
