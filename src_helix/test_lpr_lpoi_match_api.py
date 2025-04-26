#!/usr/bin/env python3
"""
Script to test the Verkada LPR Images API endpoint by filtering for License Plates of Interest (LPOI).
Fetches the LPOI list and LPR detection events from all LPR-enabled cameras
within a specified time range, then prints only the matching detections in a table.
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
from collections import defaultdict # To easily count detections per hour

# Import shared utility functions
from src_helix.api_utils import get_api_token, VERKADA_API_BASE_URL, fetch_lpr_enabled_cameras, fetch_lpr_images_for_camera, format_timestamp # Import functions from api_utils

# Import necessary fetch functions from other test scripts
# Assuming these functions are designed to be imported and reused and return data.
try:
    # fetch_lpoi_data now returns a tuple: (raw_first_page_data, all_lpoi_items_list)
    from src_helix.test_lpoi_api import fetch_lpoi_data as fetch_lpoi_data_and_list
    # Removed import from test_lpr_images_api_all_cameras
    # from src_helix.test_lpr_images_api_all_cameras import fetch_lpr_enabled_cameras, fetch_lpr_images_for_camera, format_timestamp
except ImportError as e:
    # Updated error message to reflect the correct import source
    print(f"Error importing necessary functions: {e}", file=sys.stderr)
    print("Please ensure 'test_lpoi_api.py' and 'api_utils.py' exist and are in the correct path.", file=sys.stderr)
    sys.exit(1)


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
log_file_path = os.path.join(LOGS_DIR, 'lpr_lpoi_match_api_debug.log')

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


# Get loggers for imported modules to control their output level
# This is necessary because imported modules configure their own loggers.
# A more robust logging strategy might configure the root logger or pass levels explicitly.
lpoi_logger = logging.getLogger('src_helix.test_lpoi_api')
lpr_images_all_cameras_logger = logging.getLogger('src_helix.test_lpr_images_api_all_cameras')
api_utils_logger = logging.getLogger('src_helix.api_utils') # Also need api_utils logger


def main():
    """Main entry point for the script."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada LPR Images API filtered by LPOI")
    parser.add_argument(
        "--history_hours",
        type=int,
        default=1,
        help="Number of hours of history to query for LPR images (default: 1)"
    )
    parser.add_argument(
        "--log_level",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR', # Changed default to ERROR
        help="Set the logging level (default: ERROR)" # Updated help text
    )

    # Parse arguments
    args = parser.parse_args()

    # Set logging level for the logger itself, the stream handler,
    # AND the loggers of the imported modules based on the argument.
    log_level = getattr(logging, args.log_level)

    logger.setLevel(log_level) # Set the main script's logger level
    stream_handler.setLevel(log_level) # Set the main script's stream handler level

    # Set the levels for the imported module loggers
    lpoi_logger.setLevel(log_level)
    lpr_images_all_cameras_logger.setLevel(log_level)
    api_utils_logger.setLevel(log_level) # Set level for api_utils logger


    logger.debug(f"Main logger level set to: {args.log_level}")
    logger.debug(f"Stream handler level set to: {args.log_level}")
    logger.debug(f"Imported logger levels set to: {args.log_level}")


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

        # --- Step 1: Fetch License Plates of Interest (LPOI) ---
        logger.info("Fetching License Plates of Interest...")
        # fetch_lpoi_data_and_list now returns a tuple (raw_data, list_of_lpoi)
        raw_lpoi_data, all_lpoi_items = fetch_lpoi_data_and_list(api_token) # Use the imported function

        # Extract just the license plate strings from the list and convert to a set for efficient lookup
        # Ensure all_lpoi_items is treated as a list
        lpoi_plates = {item.get('license_plate') for item in all_lpoi_items if isinstance(item, dict) and item.get('license_plate')}

        logger.info(f"Successfully retrieved {len(lpoi_plates)} License Plates of Interest.")
        logger.debug(f"LPOI list: {lpoi_plates}")

        if not lpoi_plates:
            logger.warning("No License Plates of Interest found. Cannot filter LPR events. Exiting.")
            sys.exit(0)

        # --- Step 2: Fetch LPR-enabled cameras ---
        logger.info("Fetching LPR-enabled cameras...")
        lpr_cameras = fetch_lpr_enabled_cameras(api_token) # Use the imported function

        if not lpr_cameras:
            logger.warning("No LPR-enabled cameras found. Exiting.")
            sys.exit(0)

        # Create a mapping from camera_id to camera name for easy lookup
        camera_name_map = {cam['camera_id']: cam.get('name', 'Unnamed Camera') for cam in lpr_cameras}
        logger.debug(f"Camera ID to Name map created: {camera_name_map}")

        # --- Step 3: Fetch LPR images for each camera and filter by LPOI ---
        logger.info(f"Querying LPR images for the last {args.history_hours} hours...")
        end_time = int(time.time())
        start_time = end_time - (args.history_hours * 60 * 60)
        logger.info(f"Time range: {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)}")

        matched_detections = []
        total_detections_fetched = 0

        for camera in lpr_cameras:
            camera_id = camera.get('camera_id')
            camera_name = camera.get('name', 'Unnamed Camera')
            if camera_id:
                logger.info(f"Fetching LPR images for camera: {camera_name} (ID: {camera_id})")
                detections = fetch_lpr_images_for_camera(api_token, camera_id, start_time, end_time) # Use imported function
                total_detections_fetched += len(detections)

                # Filter detections for this camera
                for det in detections:
                    # Ensure detection is a dictionary and has 'license_plate' and 'timestamp'
                    if isinstance(det, dict) and 'license_plate' in det and 'timestamp' in det:
                        if det['license_plate'] in lpoi_plates:
                            # Add camera name to the detection for printing
                            det['camera_name'] = camera_name
                            matched_detections.append(det)
                            logger.debug(f"Matched LPOI: {det.get('license_plate')} on camera {camera_name}")
                    else:
                         logger.warning(f"Skipping malformed detection entry for camera {camera_name}: {det}")

            else:
                logger.warning(f"Skipping camera entry with no camera_id: {camera}")

        logger.info(f"Finished fetching LPR images from all LPR-enabled cameras. Total detections fetched: {total_detections_fetched}. Matched LPOI detections: {len(matched_detections)}")

        # --- Step 4: Print matched results in a table format ---
        if matched_detections:
            # Sort matched detections by license plate first, then by timestamp
            # Using default values for get() to handle potential missing keys gracefully
            matched_detections.sort(key=lambda x: (x.get('license_plate', ''), x.get('timestamp', 0)))

            # Define column widths (adjust as needed)
            plate_width = 20
            gate_width = 30
            time_width = 20

            # Calculate total width for separator lines
            total_width = plate_width + gate_width + time_width + 6

            # Include the count of LPOI plates (for context) and the time range in the header
            formatted_start_time = format_timestamp(start_time) # Use imported function
            formatted_end_time = format_timestamp(end_time) # Use imported function

            # Print header with surrounding dashed lines
            print("-" * total_width) # Top separator line
            print(f"| LPR Match to LPoI {{{len(lpoi_plates)}}} ::::: {formatted_start_time} to {formatted_end_time} |")
            print("-" * total_width) # Separator line after title
            print(f"{'License Plate':<{plate_width}} | {'Gate (Camera Name)':<{gate_width}} | {'Day/Time':<{time_width}}")
            print("-" * total_width) # Header separator line

            # Print rows, adding a separator between different license plates
            previous_plate = None
            for detection in matched_detections:
                license_plate = detection.get('license_plate', 'N/A')
                camera_name = detection.get('camera_name', 'Unknown Camera') # Use the added camera_name
                timestamp = detection.get('timestamp')
                formatted_time = format_timestamp(timestamp) if timestamp is not None else 'N/A' # Use imported format_timestamp

                # Add a separator line if the license plate changes (and it's not the first row)
                if previous_plate is not None and license_plate != previous_plate:
                    print("-" * total_width) # Group separator line

                # Update the previous plate tracker
                previous_plate = license_plate

                # Truncate if necessary to fit column width
                display_plate = (license_plate[:plate_width-3] + '...') if len(license_plate) > plate_width else license_plate
                display_gate = (camera_name[:gate_width-3] + '...') if len(camera_name) > gate_width else camera_name
                display_time = (formatted_time[:time_width-3] + '...') if len(formatted_time) > time_width else formatted_time

                print(f"{display_plate:<{plate_width}} | {display_gate:<{gate_width}} | {display_time:<{time_width}}")
        else:
            print("\nNo LPR detections matching License Plates of Interest found in the specified time range.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
