#!/usr/bin/env python3
"""
Script to generate an hourly demographic report of LPR detections,
categorized into License Plates of Interest (LPOI) and Non-LPOI.
Fetches the LPOI list and all LPR detection events within a specified
time range, then aggregates and prints counts per hour in a table.
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
log_file_path = os.path.join(LOGS_DIR, 'lpr_hourly_report_api_debug.log')

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
    parser = argparse.ArgumentParser(description="Generate Hourly LPR Report (LPOI vs Non-LPOI)")
    parser.add_argument(
        "--history_hours",
        type=int,
        default=24, # Default to 24 hours for a full day report
        help="Number of hours of history to query for LPR images (default: 24)"
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

        # FIX: Use the extracted api_token string for logging
        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # --- Step 1: Fetch License Plates of Interest (LPOI) ---
        logger.info("Fetching License Plates of Interest...")

        # fetch_lpoi_data_and_list now returns a tuple: (raw_first_page_data, all_lpoi_items_list)
        raw_lpoi_data, all_lpoi_items = fetch_lpoi_data_and_list(api_token) # Use the imported function

        # Extract just the license plate strings from the list and convert to a set for efficient lookup
        # Ensure all_lpoi_items is treated as a list
        lpoi_plates = {item.get('license_plate') for item in all_lpoi_items if isinstance(item, dict) and item.get('license_plate')}

        logger.info(f"Successfully retrieved {len(lpoi_plates)} License Plates of Interest.")
        logger.debug(f"LPOI list: {lpoi_plates}")

        # --- Step 2: Fetch LPR-enabled cameras ---
        logger.info("Fetching LPR-enabled cameras...")
        lpr_cameras = fetch_lpr_enabled_cameras(api_token) # Use the imported function

        if not lpr_cameras:
            logger.warning("No LPR-enabled cameras found. Exiting.")
            sys.exit(0)

        # Create a mapping from camera_id to camera name for easy lookup (not strictly needed for this report, but good practice)
        camera_name_map = {cam['camera_id']: cam.get('name', 'Unnamed Camera') for cam in lpr_cameras}
        logger.debug(f"Camera ID to Name map created: {camera_name_map}")

        # --- Step 3: Fetch ALL LPR images for each camera ---
        logger.info(f"Querying ALL LPR images for the last {args.history_hours} hours...")
        end_time = int(time.time())
        start_time = end_time - (args.history_hours * 60 * 60)
        logger.info(f"Time range: {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)}")

        all_detections = []
        total_detections_fetched = 0

        for camera in lpr_cameras:
            camera_id = camera.get('camera_id')
            camera_name = camera.get('name', 'Unnamed Camera')
            if camera_id:
                logger.info(f"Fetching LPR images for camera: {camera_name} (ID: {camera_id})")
                detections = fetch_lpr_images_for_camera(api_token, camera_id, start_time, end_time) # Use imported function
                total_detections_fetched += len(detections)
                all_detections.extend(detections) # Add all detections, filtering comes next

            else:
                logger.warning(f"Skipping camera entry with no camera_id: {camera}")

        logger.info(f"Finished fetching LPR images from all LPR-enabled cameras. Total detections fetched: {total_detections_fetched}.")

        # --- Step 4: Categorize and Aggregate Detections by Hour ---
        hourly_counts = defaultdict(lambda: {'lpoi': 0, 'non_lpoi': 0})

        logger.info("Categorizing and aggregating detections by hour...")
        for det in all_detections:
            # Ensure detection is a dictionary and has 'license_plate' and 'timestamp'
            if isinstance(det, dict) and 'license_plate' in det and 'timestamp' in det:
                timestamp = det['timestamp']
                license_plate = det['license_plate']

                try:
                    # Convert timestamp to datetime object in local timezone
                    dt_object = datetime.datetime.fromtimestamp(timestamp)
                    # Get date (YYYY-MM-DD) and hour (0-23)
                    date_str = dt_object.strftime('%Y-%m-%d')
                    hour = dt_object.hour # 0-23

                    # Determine if it's LPOI or Non-LPOI
                    category = 'lpoi' if license_plate in lpoi_plates else 'non_lpoi'

                    # Increment the count for the specific hour and category
                    hourly_counts[(date_str, hour)][category] += 1

                except (TypeError, ValueError) as e:
                    logger.warning(f"Skipping detection with invalid timestamp {timestamp}: {e}")
                except Exception as e:
                    logger.error(f"Unexpected error processing detection {det}: {e}", exc_info=True)

            else:
                 logger.warning(f"Skipping malformed detection entry: {det}")


        logger.info(f"Finished aggregating detections. Found data for {len(hourly_counts)} distinct hours.")

        # --- Step 5: Print the Hourly Report Table ---
        if hourly_counts:
            # Sort the hours for printing
            sorted_hours = sorted(hourly_counts.keys())

            # Define column widths (adjust as needed)
            # Define column widths (adjust as needed)
            date_width = 10 # YYYY-MM-DD
            hour_width = 15 # HH AM/PM - HH AM/PM
            non_lpoi_width = 10 # Count (Adjusted)
            lpoi_width = 10 # Count (Adjusted)

            # Calculate total width for separator lines
            # Add 3 for each column separator '|' and 2 for padding ' | '
            total_width = date_width + hour_width + non_lpoi_width + lpoi_width + (3 * 3) + 2

            # Print header
            print("-" * total_width) # Top separator line
            # Report title including the date range queried
            formatted_start_date = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d')
            formatted_end_date = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d')

            # Remove leading/trailing '|' from the title line
            print(f"LPR Hourly Report ::: {formatted_start_date} to {formatted_end_date}")
            print("-" * total_width) # Separator line after title
            # Remove ' Count' from column headers
            print(f"{'Date':<{date_width}} | {'Hour':<{hour_width}} | {'Non-LPOI':<{non_lpoi_width}} | {'LPOI':<{lpoi_width}}")
            print("-" * total_width) # Header separator line

            previous_date = None
            for date_str, hour in sorted_hours:
                counts = hourly_counts[(date_str, hour)]
                non_lpoi_count = counts['non_lpoi']
                lpoi_count = counts['lpoi']

                # Format the hour range (e.g., "03 PM - 04 PM")
                # Create datetime objects for the start and end of the hour
                dt_start_of_hour = datetime.datetime.strptime(f"{date_str} {hour:02d}:00:00", '%Y-%m-%d %H:%M:%S')
                dt_end_of_hour = dt_start_of_hour + datetime.timedelta(hours=1)

                # Use '%I %p' to get hour and AM/PM without minutes
                formatted_hour_start = dt_start_of_hour.strftime('%I %p')
                formatted_hour_end = dt_end_of_hour.strftime('%I %p')
                hour_range_str = f"{formatted_hour_start} - {formatted_hour_end}"

                # Add separator line at midnight (hour 0) and noon (hour 12), but not before the very first row
                if previous_date is not None and (hour == 0 or hour == 12):
                     print("-" * total_width) # Group separator line

                # Print the data row
                print(f"{date_str:<{date_width}} | {hour_range_str:<{hour_width}} | {non_lpoi_count:<{non_lpoi_width}} | {lpoi_count:<{lpoi_width}}")

                previous_date = date_str # Update previous date tracker

            print("-" * total_width) # Bottom separator line

        else:
            print("\nNo LPR detections found in the specified time range to generate an hourly report.")

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure logs are flushed before exiting
        logging.shutdown()

if __name__ == '__main__':
    main()
