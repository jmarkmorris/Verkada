#!/usr/bin/env python3
"""
Script to test the Verkada LPR Images API endpoint for all LPR-enabled cameras.
Fetches LPR detection events (images, license plates, timestamps) for all
cameras with 'License' in their name within a specified time range.
Prints the results in a formatted table.
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

# Import shared utility functions
from src_helix.api_utils import get_api_token, VERKADA_API_BASE_URL

# Get the logger for this module
logger = logging.getLogger(__name__)
# Set the logger level to DEBUG so it processes all messages
logger.setLevel(logging.DEBUG)

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix directory
file_handler = logging.FileHandler('src_helix/lpr_images_all_cameras_api_debug.log')
file_handler.setLevel(logging.DEBUG)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
# Prevent duplicate handlers if the script is somehow imported multiple times
if not logger.handlers:
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


CAMERAS_ENDPOINT = "/cameras/v1/devices"
LPR_IMAGES_ENDPOINT = "/cameras/v1/analytics/lpr/images"


def fetch_lpr_enabled_cameras(api_token: str) -> list:
    """
    Fetches all cameras and filters for those with 'License' in their name.
    Returns a list of camera dictionaries.
    """
    url = f"{VERKADA_API_BASE_URL}{CAMERAS_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }

    try:
        logger.info(f"Fetching all camera data from {url}")
        response = requests.get(url, headers=headers)
        logger.debug(f"Cameras response status code: {response.status_code}")
        response.raise_for_status()
        data = response.json()

        logger.debug(f"Raw camera response data: {data}")

        # Extract the list of cameras, defaulting to empty list if not found or not a list
        all_cameras = data.get('cameras')
        if not isinstance(all_cameras, list):
             logger.warning(f"Expected 'cameras' list in response, but got {type(all_cameras)}. Returning empty list.")
             return []

        # Filter for cameras with 'name' and 'camera_id' that contain 'License' (case-insensitive)
        lpr_cameras = [
            cam for cam in all_cameras
            if isinstance(cam, dict) and 'name' in cam and 'camera_id' in cam and 'license' in cam['name'].lower()
        ]

        logger.info(f"Found {len(lpr_cameras)} LPR-enabled cameras (filtered by 'License' in name).")
        logger.debug(f"LPR-enabled cameras found: {[c.get('name', 'Unnamed') for c in lpr_cameras]}")

        return lpr_cameras
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error fetching camera list: {e}")
        logger.error(f"Response status code: {e.response.status_code}")
        logger.error(f"Response content: {e.response.content}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error fetching camera list: {e}", exc_info=True)
        raise


def fetch_lpr_images_for_camera(api_token: str, camera_id: str, start_time: int, end_time: int) -> list:
    """
    Fetches LPR images (detections) for a single camera within a time range,
    handling pagination. Returns a list of detection dictionaries.
    """
    url = f"{VERKADA_API_BASE_URL}{LPR_IMAGES_ENDPOINT}"
    headers = {
        "Accept": "application/json",
        "x-verkada-auth": api_token,
    }
    all_detections = []
    page_token = None
    page_count = 0

    logger.debug(f"Fetching LPR images for camera ID: {camera_id} from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)}")

    while True:
        params = {
            "camera_id": camera_id,
            "start_time": start_time,
            "end_time": end_time,
            "page_size": 200 # Max page size
        }
        if page_token:
            params["page_token"] = page_token
            logger.debug(f"Fetching page {page_count + 1} with page_token: {page_token}")
        else:
             logger.debug(f"Fetching initial page for camera ID: {camera_id}")


        try:
            response = requests.get(url, headers=headers, params=params)
            logger.debug(f"LPR images response status code for camera {camera_id}, page {page_count + 1}: {response.status_code}")
            response.raise_for_status()
            data = response.json()

            logger.debug(f"Raw LPR images response data for camera {camera_id}, page {page_count + 1}: {data}")

            # The API response structure for /images is a dictionary with 'camera_id', 'detections', 'next_page_token'
            detections = data.get('detections', []) if isinstance(data, dict) else []
            if not isinstance(detections, list):
                 logger.warning(f"Expected 'detections' list in response for camera {camera_id}, page {page_count + 1}, but got {type(detections)}. Stopping pagination for this camera.")
                 break # Stop if detections is not a list

            all_detections.extend(detections)
            logger.debug(f"Added {len(detections)} detections from page {page_count + 1}. Total detections so far: {len(all_detections)}")

            page_token = data.get('next_page_token') if isinstance(data, dict) else None
            page_count += 1

            if page_token:
                logger.debug(f"Next page token found: {page_token}. Continuing pagination.")
                # Optional: Add a small delay to avoid hitting rate limits
                # time.sleep(0.1)
            else:
                logger.debug("No next page token found. Ending pagination for this camera.")
                break # No more pages

        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error fetching LPR images for camera {camera_id}, page {page_count + 1}: {e}")
            logger.error(f"Response status code: {e.response.status_code}")
            logger.error(f"Response content: {e.response.content}")
            # Decide whether to stop or continue with the next camera on error
            # For now, we'll log and stop fetching for this camera
            break
        except Exception as e:
            logger.error(f"Unexpected error fetching LPR images for camera {camera_id}, page {page_count + 1}: {e}", exc_info=True)
            # Log and stop fetching for this camera
            break

    logger.info(f"Finished fetching LPR images for camera {camera_id}. Total detections: {len(all_detections)}")
    return all_detections


def format_timestamp(unix_timestamp: int) -> str:
    """Converts a Unix timestamp (seconds) to a human-readable string."""
    try:
        dt_object = datetime.datetime.fromtimestamp(unix_timestamp)
        return dt_object.strftime('%Y-%m-%d %H:%M:%S')
    except (TypeError, ValueError) as e:
        logger.warning(f"Could not format timestamp {unix_timestamp}: {e}")
        return str(unix_timestamp) # Return original value or error indicator


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada LPR Images API for all LPR-enabled cameras")
    parser.add_argument(
        "--history_hours",
        type=int,
        default=1,
        help="Number of hours of history to query (default: 1)"
    )
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO',
        help="Set the logging level (default: INFO)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Set logging level for the stream handler based on the argument.
    stream_handler.setLevel(getattr(logging, args.log_level))
    logger.debug(f"Stream handler level set to: {args.log_level}")

    # Add debug logging to show the arguments received
    logger.debug(f"Arguments received: history_hours={args.history_hours}, log_level={args.log_level}")

    # Get API key from environment variable
    logger.debug("Attempting to get API_KEY environment variable...")
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

        # Calculate time range based on history_hours
        end_time = int(time.time())
        start_time = end_time - (args.history_hours * 60 * 60)
        logger.info(f"Querying LPR images for the last {args.history_hours} hours (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")


        # Fetch LPR-enabled cameras
        logger.debug("Attempting to fetch LPR-enabled cameras...")
        lpr_cameras = fetch_lpr_enabled_cameras(api_token)

        if not lpr_cameras:
            logger.warning("No LPR-enabled cameras found. Exiting.")
            sys.exit(0)

        # Create a mapping from camera_id to camera name for easy lookup
        camera_name_map = {cam['camera_id']: cam.get('name', 'Unnamed Camera') for cam in lpr_cameras}
        logger.debug(f"Camera ID to Name map created: {camera_name_map}")

        all_detections = []
        # Fetch LPR images for each LPR-enabled camera
        for camera in lpr_cameras:
            camera_id = camera.get('camera_id')
            camera_name = camera.get('name', 'Unnamed Camera')
            if camera_id:
                logger.info(f"Fetching LPR images for camera: {camera_name} (ID: {camera_id})")
                detections = fetch_lpr_images_for_camera(api_token, camera_id, start_time, end_time)
                # Add camera name to each detection for easier printing
                for det in detections:
                    det['camera_name'] = camera_name
                all_detections.extend(detections)
            else:
                logger.warning(f"Skipping camera entry with no camera_id: {camera}")


        logger.info(f"Finished fetching LPR images from all LPR-enabled cameras. Total detections found: {len(all_detections)}")

        # Sort detections by timestamp (optional, but makes output easier to read)
        all_detections.sort(key=lambda x: x.get('timestamp', 0))

        # Print results in a table format
        if all_detections:
            print("\n--- LPR Detections Table ---")
            # Define column widths (adjust as needed)
            plate_width = 20
            gate_width = 30
            time_width = 20

            # Print header
            print(f"{'License Plate':<{plate_width}} | {'Gate (Camera Name)':<{gate_width}} | {'Day/Time':<{time_width}}")
            print("-" * (plate_width + gate_width + time_width + 6)) # Separator line

            # Print rows
            for detection in all_detections:
                license_plate = detection.get('license_plate', 'N/A')
                camera_name = detection.get('camera_name', 'Unknown Camera') # Use the added camera_name
                timestamp = detection.get('timestamp')
                formatted_time = format_timestamp(timestamp) if timestamp is not None else 'N/A'

                # Truncate if necessary to fit column width
                display_plate = (license_plate[:plate_width-3] + '...') if len(license_plate) > plate_width else license_plate
                display_gate = (camera_name[:gate_width-3] + '...') if len(camera_name) > gate_width else camera_name
                display_time = (formatted_time[:time_width-3] + '...') if len(formatted_time) > time_width else formatted_time


                print(f"{display_plate:<{plate_width}} | {display_gate:<{gate_width}} | {display_time:<{time_width}}")
        else:
            print("\nNo LPR detections found in the last hour for LPR-enabled cameras.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
