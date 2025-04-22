#!/bin/bash

# This script isolates and debugs the camera listing logic from runtest.sh

# Check if API_KEY is set
if [ -z "$API_KEY" ]; then
  echo "Error: API_KEY environment variable is not set."
  echo "Please set it before running this script:"
  echo "  export API_KEY=\"your_verkada_api_key\""
  exit 1
fi

# Define variables needed for the isolated block
# Set LOG_LEVEL to DEBUG to see the raw output
LOG_LEVEL="DEBUG"
script_name="test_lpr_timestamps_api.py" # Set this to match the condition in the block

echo "--- Starting Isolation Script ---"
echo "API_KEY: ${API_KEY:0:5}...${API_KEY: -4}"
echo "LOG_LEVEL: $LOG_LEVEL"
echo "script_name: $script_name"
echo "---------------------------------"

# Start of the isolated block from runtest.sh
# Handle script requiring license_plate and camera_id (via selection menu)
if [[ "$script_name" == "test_lpr_timestamps_api.py" ]]; then
    echo "Condition matched: script_name is $script_name"
    echo "Fetching list of all cameras..."

    # Fetch and list all cameras using test_cameras_api.py with --list-for-menu
    # Capture both stdout and stderr
    echo "Executing: python src_helix/test_cameras_api.py --log_level \"$LOG_LEVEL\" --list-for-menu 2>&1"
    all_cameras_raw_output=$(python src_helix/test_cameras_api.py --log_level "$LOG_LEVEL" --list-for-menu 2>&1)
    script_exit_code=$? # Capture exit code

    echo "--- State after fetching cameras ---"
    echo "script_exit_code: $script_exit_code"
    echo "all_cameras_raw_output:"
    echo "$all_cameras_raw_output"
    echo "--- End state ---"

    if [ $script_exit_code -ne 0 ]; then
      echo "Failed to fetch camera list (exit code $script_exit_code). Aborting isolation script."
      echo "Please check the 'cameras_api_debug.log' file for details."
      # In the original script, this would return to the menu. Here, we exit.
      exit 1
    fi

    # Extract only the camera list lines after the marker using awk
    # The marker is "---START_CAMERA_LIST---"
    echo "Extracting camera list using awk..."
    camera_list_output=$(echo "$all_cameras_raw_output" | awk '/---START_CAMERA_LIST---/{flag=1; next} flag')

    echo "--- State after awk extraction ---"
    echo "camera_list_output:"
    echo "$camera_list_output"
    echo "Length of camera_list_output: ${#camera_list_output}" # Added length check
    echo "--- End state ---"

    # The original script would continue here to build and display the menu.
    # We stop here as requested.

fi
# End of the isolated block

echo "--- Isolation Script Finished ---"
