#!/usr/bin/env python3
"""
Script to test the Verkada LPR Images API endpoint by filtering for License Plates of Interest (LPOI).
Fetches the LPOI list and LPR detection events from all LPR-enabled cameras
within a specified time range, then prints only the matching detections in a table.
"""
import os
import sys
import logging
import argparse
import time
import datetime
from collections import defaultdict # To easily count detections per hour

# Import shared utility functions and the centralized logging function
from src_helix.api_utils import get_api_token, VERKADA_API_BASE_URL, fetch_lpr_enabled_cameras, fetch_lpr_images_for_camera, format_timestamp, configure_logging, filter_lpr_by_lpoi, fetch_all_lpoi


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
    Filters the detections to include only those matching the LPOI list.
    Prints the matched detections in a formatted table.
    Exits with status 0 if successful, 1 on error (including fetch errors).
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test Verkada LPR Images API filtered by LPOI")
    parser.add_argument(
        "--history_hours",
        type=int,
        default=1,
        help="Number of hours of history to query (default: 1)"
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

        if not lpoi_plates:
            logger.warning("No License Plates of Interest found. Cannot filter LPR events. Exiting.")
            sys.exit(0)

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
                    # Add camera name to each detection for easier printing *before* filtering
                    for det in detections:
                        det['camera_name'] = camera_name
                    all_detections.extend(detections)
                except Exception as camera_fetch_error:
                    logger.error(f"Failed to fetch LPR images for camera {camera_name} (ID: {camera_id}): {camera_fetch_error}", exc_info=True)
                    error_occurred = True
            else:
                logger.warning(f"Skipping camera entry with no camera_id: {camera}")

        logger.info(f"Finished fetching LPR images from all LPR-enabled cameras. Total detections fetched: {total_detections_fetched}.")

        # --- Step 4: Filter detections by LPOI ---
        logger.info("Filtering detections for LPOI matches...")
        matched_detections = filter_lpr_by_lpoi(all_detections, lpoi_plates)
        logger.info(f"Found {len(matched_detections)} LPOI matches.")


        # --- Step 5: Print matched results in a table format ---
        if matched_detections:
            # Sort matched detections by license plate first, then by timestamp
            matched_detections.sort(key=lambda x: (x.get('license_plate', ''), x.get('timestamp', 0)))

            # Define column widths
            plate_width = 20
            gate_width = 30
            time_width = 20

            # Calculate total width for separator lines
            total_width = plate_width + gate_width + time_width + 6

            # Include the count of LPOI plates and the time range in the header
            formatted_start_time = format_timestamp(start_time)
            formatted_end_time = format_timestamp(end_time)

            # Print header with surrounding dashed lines
            print("-" * total_width)
            print(f"| LPR Match to LPoI {{{len(lpoi_plates)}}} ::::: {formatted_start_time} to {formatted_end_time} |")
            print("-" * total_width)
            print(f"{'License Plate':<{plate_width}} | {'Gate (Camera Name)':<{gate_width}} | {'Day/Time':<{time_width}}")
            print("-" * total_width)

            # Print rows, adding a separator between different license plates
            previous_plate = None
            for detection in matched_detections:
                license_plate = detection.get('license_plate', 'N/A')
                camera_name = detection.get('camera_name', 'Unknown Camera')
                timestamp = detection.get('timestamp')
                formatted_time = format_timestamp(timestamp) if timestamp is not None else 'N/A'

                if previous_plate is not None and license_plate != previous_plate:
                    print("-" * total_width)

                previous_plate = license_plate

                # Truncate if necessary to fit column width
                display_plate = (license_plate[:plate_width-3] + '...') if len(license_plate) > plate_width else license_plate
                display_gate = (camera_name[:gate_width-3] + '...') if len(camera_name) > gate_width else camera_name
                display_time = (formatted_time[:time_width-3] + '...') if len(formatted_time) > time_width else formatted_time

                print(f"{display_plate:<{plate_width}} | {display_gate:<{gate_width}} | {display_time:<{time_width}}")
        else:
            print("\nNo LPR detections matching License Plates of Interest found in the specified time range.")

        # --- Step 6: Check if errors occurred during fetching ---
        if error_occurred:
            logger.error("One or more errors occurred while fetching LPR images for cameras. Results may be incomplete.")
            sys.exit(1) # Exit with non-zero code to indicate failure

    except Exception as e:
        logger.error(f"Script execution failed: {e}", exc_info=True)
        sys.exit(1)
    finally:
        logging.shutdown()

if __name__ == '__main__':
    main()
