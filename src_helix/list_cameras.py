#!/usr/bin/env python3
"""
Helper script to list cameras with 'License' in their name.
Used by runtest.sh to provide a selection menu for LPR tests.
"""
import os
import sys
import json
import logging
import requests

# Configure logging (minimal output for a helper script)
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

VERKADA_API_BASE_URL = "https://api.verkada.com"
TOKEN_ENDPOINT = "/token"
CAMERAS_ENDPOINT = "/cameras/v1/devices"

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

def fetch_cameras_data(api_token: str) -> list:
    """Fetch camera data from Verkada API."""
    url = f"{VERKADA_API_BASE_URL}{CAMERAS_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('devices', []) if isinstance(data, dict) else []
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error fetching cameras: {e}")
        return []
    except Exception as e:
        logger.error(f"Error fetching cameras: {e}")
        return []

def main():
    """Main entry point for the script."""
    api_key = os.environ.get('API_KEY')
    if not api_key:
        logger.error("API_KEY environment variable is not set.")
        sys.exit(1)

    try:
        api_token = get_api_token(api_key)
        cameras = fetch_cameras_data(api_token)

        # Filter for cameras with 'name' and 'id' (list all cameras)
        all_cameras = [
            cam for cam in cameras
            if 'name' in cam and 'id' in cam
        ]

        if not all_cameras:
            logger.error("No cameras found in the organization.")
            sys.exit(1)

        # Print cameras in a parsable format: index,id,name
        for i, cam in enumerate(all_cameras):
            print(f"{i+1},{cam['id']},{cam['name']}")

    except Exception as e:
        logger.error(f"Script execution failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
