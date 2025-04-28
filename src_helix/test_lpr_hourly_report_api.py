#!/usr/bin/env python3
"""
Script to generate an hourly demographic report of LPR detections,
categorized into License Plates of Interest (LPOI) and Non-LPOI.
Fetches the LPOI list and all LPR detection events within a specified
time range, then aggregates and prints counts per hour in a table.
"""
import os
import sys
import logging
import argparse
import time
import datetime
from collections import defaultdict # To easily count detections per hour

# Import shared utility functions and the centralized logging function
from src_helix.api_utils import get_api_token, VERKADA_API_BASE_URL, fetch_lpr_enabled_cameras, fetch_lpr_images_for_camera, format_timestamp, configure_logging, fetch_all_lpoi


# Get the logger for this module. It will be configured by configure_logging in main.
logger = logging.getLogger(__name__)


def main():
    """
    Main entry point for the script.

    Parses command-line arguments for history duration and log level.
    Retrieves the API key from environment variables.
    Obtains an API token.
    Fetches the list of License Plates of Interest (LPOI).
    Fetches all LPR-enabled cameras.
    For each LPR camera, fetches all LPR image detections within the specified history.
    Aggregates detections by hour, categorizing them as LPOI or Non-LPOI.
    Prints the hourly counts in a formatted table.
    Exits with status 0 if successful, 1 on error (including fetch errors).
    """
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
        default='ERROR',
        help="Set the logging level (default: ERROR)"
    )

    # Parse arguments
    args = parser.parse_args()

    # Configure logging using the centralized function
    configure_logging(args.log_level)

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

    error_occurred = False # Flag to track if any fetch failed
    try:
        # Get API token
        logger.debug("Attempting to get API token...")
        token_data = get_api_token(api_key)
        api_token = token_data.get('token')
        if not api_token:
             raise ValueError("API token not found in response.")

        logger.info(f"Successfully retrieved API token: {api_token[:10]}...")

        # --- Step 1: Fetch License Plates of Interest (LPOI) ---
        logger.info("Fetching License Plates of Interest...")
        all_lpoi_items, lpoi_error_flag = fetch_all_lpoi(api_token)

        # Check if an error occurred during LPOI fetching
        if lpoi_error_flag:
            logger.error("Error occurred during pagination while fetching LPOI list. Cannot proceed.")
            sys.exit(1)

        # Extract just the license plate strings from the list and convert to a set for efficient lookup
        lpoi_plates = {item.get('license_plate') for item in all_lpoi_items if isinstance(item, dict) and item.get('license_plate')}

        logger.info(f"Successfully retrieved {len(lpoi_plates)} License Plates of Interest.")
        logger.debug(f"LPOI list: {lpoi_plates}")

        # --- Step 2: Fetch LPR-enabled cameras ---
        logger.info("Fetching LPR-enabled cameras...")
        lpr_cameras = fetch_lpr_enabled_cameras(api_token)

        if not lpr_cameras:
            logger.warning("No LPR-enabled cameras found. Exiting.")
            sys.exit(0)

        # Create a mapping from camera_id to camera name for easy lookup
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
                try:
                    detections = fetch_lpr_images_for_camera(api_token, camera_id, start_time, end_time)
                    total_detections_fetched += len(detections)
                    all_detections.extend(detections)
                except Exception as camera_fetch_error:
                    logger.error(f"Failed to fetch LPR images for camera {camera_name} (ID: {camera_id}): {camera_fetch_error}", exc_info=True)
                    error_occurred = True
            else:
                logger.warning(f"Skipping camera entry with no camera_id: {camera}")

        logger.info(f"Finished fetching LPR images from all LPR-enabled cameras. Total detections fetched: {total_detections_fetched}.")

        # --- Step 4: Categorize and Aggregate Detections by Hour ---
        hourly_counts = defaultdict(lambda: {'lpoi': 0, 'non_lpoi': 0})

        logger.info("Categorizing and aggregating detections by hour...")
        for det in all_detections:
            if isinstance(det, dict) and 'license_plate' in det and 'timestamp' in det:
                timestamp = det['timestamp']
                license_plate = det['license_plate']

                try:
                    dt_object = datetime.datetime.fromtimestamp(timestamp)
                    date_str = dt_object.strftime('%Y-%m-%d')
                    hour = dt_object.hour

                    category = 'lpoi' if license_plate in lpoi_plates else 'non_lpoi'
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
            sorted_hours = sorted(hourly_counts.keys())

            date_width = 10
            hour_width = 15
            non_lpoi_width = 10
            lpoi_width = 10
            total_width = date_width + hour_width + non_lpoi_width + lpoi_width + (3 * 3) + 2

            print("-" * total_width)
            formatted_start_date = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d')
            formatted_end_date = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d')

            print(f"LPR Hourly Report ::: {formatted_start_date} to {formatted_end_date}")
            print("-" * total_width)
            print(f"{'Date':<{date_width}} | {'Hour':<{hour_width}} | {'Non-LPOI':<{non_lpoi_width}} | {'LPOI':<{lpoi_width}}")
            print("-" * total_width)

            previous_date = None
            for date_str, hour in sorted_hours:
                counts = hourly_counts[(date_str, hour)]
                non_lpoi_count = counts['non_lpoi']
                lpoi_count = counts['lpoi']

                dt_start_of_hour = datetime.datetime.strptime(f"{date_str} {hour:02d}:00:00", '%Y-%m-%d %H:%M:%S')
                dt_end_of_hour = dt_start_of_hour + datetime.timedelta(hours=1)

                formatted_hour_start = dt_start_of_hour.strftime('%I %p')
                formatted_hour_end = dt_end_of_hour.strftime('%I %p')
                hour_range_str = f"{formatted_hour_start} - {formatted_hour_end}"

                if previous_date is not None and (hour == 0 or hour == 12):
                     print("-" * total_width)

                print(f"{date_str:<{date_width}} | {hour_range_str:<{hour_width}} | {non_lpoi_count:<{non_lpoi_width}} | {lpoi_count:<{lpoi_width}}")

                previous_date = date_str

            print("-" * total_width)

        else:
            print("\nNo LPR detections found in the specified time range to generate an hourly report.")

        # --- Step 6: Check if errors occurred during fetching ---
        if error_occurred:
            logger.error("One or more errors occurred while fetching LPR images for cameras. Report may be incomplete.")
            sys.exit(1) # Exit with non-zero code to indicate failure

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        logging.shutdown()

if __name__ == '__main__':
    main()
