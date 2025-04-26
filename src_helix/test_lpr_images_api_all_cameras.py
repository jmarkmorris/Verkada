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
from src_helix.api_utils import get_api_token, VERKADA_API_BASE_URL, fetch_lpr_enabled_cameras, fetch_lpr_images_for_camera, format_timestamp # Import functions from api_utils

# Get the logger for this module
logger = logging.getLogger(__name__)
# Set the logger level initially to DEBUG to capture all messages for the file handler
logger.setLevel(logging.DEBUG)

# Define the logs directory path
LOGS_DIR = 'src_helix/logs'

# Ensure the logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create handlers
# Stream handler for stdout - level will be set based on user input in main
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter) # Set formatter for stream handler

# File handler for debug logs - always log DEBUG and above to file
# Save log file in the src_helix/logs directory
log_file_path = os.path.join(LOGS_DIR, 'lpr_images_all_cameras_api_debug.log')

# Create file handler, handling potential errors
try:
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG) # File handler always logs DEBUG and above
    file_handler.setFormatter(formatter) # Set formatter for file handler

    # Add handlers to the logger
    # Prevent duplicate handlers if the script is somehow imported multiple times
    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

except Exception as e:
    # If file handler creation fails, log an error to the console (via stream_handler)
    # and continue without the file handler.
    logger.error(f"Failed to create file handler for {log_file_path}: {e}")


# Removed redundant endpoint definitions, they are in api_utils now
# CAMERAS_ENDPOINT = "/cameras/v1/devices"
# LPR_IMAGES_ENDPOINT = "/cameras/v1/analytics/lpr/images"

# Removed fetch_lpr_enabled_cameras, fetch_lpr_images_for_camera, format_timestamp definitions
# They are now in api_utils.py


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
        default='ERROR', # Changed default to ERROR
        help="Set the logging level (default: ERROR)" # Updated help text
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
        # get_api_token now returns the full data dictionary
        token_data = get_api_token(api_key) # Use imported function
        # Extract the token string from the returned dictionary
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")

        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # Calculate time range based on history_hours
        end_time = int(time.time())
        start_time = end_time - (args.history_hours * 60 * 60)
        logger.info(f"Querying LPR images for the last {args.history_hours} hours (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")


        # Fetch LPR-enabled cameras
        logger.debug("Attempting to fetch LPR-enabled cameras...")
        lpr_cameras = fetch_lpr_enabled_cameras(api_token) # Use imported function

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
                detections = fetch_lpr_images_for_camera(api_token, camera_id, start_time, end_time) # Use imported function
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
                formatted_time = format_timestamp(timestamp) if timestamp is not None else 'N/A' # Use imported function

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
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
