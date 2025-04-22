#!/bin/bash

# Check if API_KEY is set
if [ -z "$API_KEY" ]; then
  echo "Error: API_KEY environment variable is not set."
  echo "Please set it before running this script:"
  echo "  export API_KEY=\"your_verkada_api_key\""
  exit 1
fi

# Default log level - Changed to ERROR
LOG_LEVEL="ERROR"

# Function to display the menu
show_menu() {
  echo "================================================================================"
  echo " Verkada API Test Script Runner"
  echo "================================================================================"
  echo " API_KEY: ${API_KEY:0:5}...${API_KEY: -4}"
  echo " Current Log Level: $LOG_LEVEL"
  echo "--------------------------------------------------------------------------------"
  echo " Select a test to run (Alphabetical Order by Endpoint):"
  echo " 1) /access/v1/access_users (test_users_list_api.py)"
  echo " 2) /access/v1/access_users/user (test_user_details_api.py)"
  echo " 3) /access/v1/events (test_access_events_api.py)"
  echo " 4) /cameras/v1/analytics/lpr/imagesview (test_lpr_images_api.py)"
  echo " 5) /cameras/v1/analytics/lpr/license_plate_of_interest (test_lpoi_api.py)"
  echo " 6) /cameras/v1/analytics/lpr/timestamps (test_lpr_timestamps_api.py)"
  echo " 7) /cameras/v1/devices (test_cameras_api.py)"
  echo " 8) /cameras/v1/notifications (test_notifications_api.py)"
  echo " 9) /token (test_token_api.py)"
  echo "--------------------------------------------------------------------------------"
  echo " L) Change Log Level (Current: $LOG_LEVEL)"
  echo " 0) Exit"
  echo "================================================================================"
}

# Function to change log level
change_log_level() {
  echo "--------------------------------------------------------------------------------"
  echo " Select Log Level:"
  echo " 1) DEBUG    - Detailed information, useful for diagnosis"
  echo " 2) INFO     - Confirmation that things are working as expected"
  echo " 3) WARNING  - Something unexpected happened, but software is still working"
  echo " 4) ERROR    - Software failed to perform a function due to a problem"
  echo " 5) CRITICAL - Serious error, program may be unable to continue"
  echo "--------------------------------------------------------------------------------"
  read -p "Enter your choice [1-5]: " level_choice
  
  case $level_choice in
    1) LOG_LEVEL="DEBUG" ;;
    2) LOG_LEVEL="INFO" ;;
    3) LOG_LEVEL="WARNING" ;;
    4) LOG_LEVEL="ERROR" ;;
    5) LOG_LEVEL="CRITICAL" ;;
    *) echo "Invalid choice. Log level unchanged." ;;
  esac
  
  echo "Log level set to: $LOG_LEVEL"
  read -n 1 -s -r -p "Press any key to return to the menu..."
  echo
}

# Function to run a test script
run_test() {
  local script_name="$1"
  local extra_args=()

  # Handle scripts requiring history_days
  if [[ "$script_name" == "src_helix/test_lpr_images_api.py" || \
        "$script_name" == "src_helix/test_notifications_api.py" || \
        "$script_name" == "src_helix/test_access_events_api.py" || \
        "$script_name" == "src_helix/test_lpr_timestamps_api.py" ]]; then
    read -p "Enter history_days (default: 7): " history_days
    history_days=${history_days:-7} # Set default if empty
    if ! [[ "$history_days" =~ ^[0-9]+$ ]]; then
        echo "Invalid input. Using default history_days=7."
        history_days=7
    fi
    extra_args+=("--history_days" "$history_days")
  fi

  # Handle script requiring user_index
  if [[ "$script_name" == "src_helix/test_user_details_api.py" ]]; then
    read -p "Enter user_index (default: 0): " user_index
    user_index=${user_index:-0} # Set default if empty
     if ! [[ "$user_index" =~ ^[0-9]+$ ]]; then
        echo "Invalid input. Using default user_index=0."
        user_index=0
    fi
    extra_args+=("--user_index" "$user_index")
  fi

  # Handle script requiring license_plate and camera_id (via selection menu)
  if [[ "$script_name" == "src_helix/test_lpr_timestamps_api.py" ]]; then
    echo "Fetching list of all cameras..."
    # Fetch and list all cameras using test_cameras_api.py as a module with --list-for-menu
    # Capture both stdout and stderr
    # Use python -m to ensure imports within test_cameras_api work correctly
    all_cameras_raw_output=$(python -m src_helix.test_cameras_api --log_level "$LOG_LEVEL" --list-for-menu 2>&1)
    script_exit_code=$? # Capture exit code

    if [ "$LOG_LEVEL" == "DEBUG" ]; then
        echo "--- Raw output from test_cameras_api.py ---"
        echo "$all_cameras_raw_output"
        echo "--- End raw output ---"
    fi

    if [ $script_exit_code -ne 0 ]; then
      echo "Failed to fetch camera list (exit code $script_exit_code). Aborting."
      echo "Please check the 'cameras_api_debug.log' file for details."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    # Extract only the camera list lines after the marker using awk
    # Set flag=1 when marker is found, skip marker line (next), print lines when flag is 1
    camera_list_output=$(echo "$all_cameras_raw_output" | awk '/---START_CAMERA_LIST---/{flag=1; next} flag')

    if [ "$LOG_LEVEL" == "DEBUG" ]; then
        echo "--- Filtered camera list output ---"
        echo "$camera_list_output"
        echo "--- End filtered output ---"
    fi


    # Build camera selection menu
    echo "--------------------------------------------------------------------------------"
    echo " Select a camera for LPR timestamps test:"
    echo " (Choose an LPR-enabled camera)"
    echo "--------------------------------------------------------------------------------"
    camera_options=()
    # Now pipe the filtered output to the while loop
    while IFS=',' read -r index camera_id camera_name; do
      # The filtering should ensure we only get valid lines, but keep the check for safety
      if [ -n "$index" ] && [ -n "$camera_id" ] && [ -n "$camera_name" ]; then
        echo " $index) $camera_name"
        camera_options+=("$camera_id") # Store camera_id in an array
      fi
    done <<< "$camera_list_output" # Use the filtered output

    # Check if any cameras were actually parsed
    if [ ${#camera_options[@]} -eq 0 ]; then
        echo "No cameras were found or parsed from the list."
        echo "This could mean the API returned no cameras, or there was an issue parsing the output."
        echo "Please check the 'cameras_api_debug.log' file for details."
        read -n 1 -s -r -p "Press any key to return to the menu..."
        echo
        return
    fi

    echo "--------------------------------------------------------------------------------"
    echo " 0) Cancel"
    echo "--------------------------------------------------------------------------------"

    read -p "Enter your choice: " camera_choice

    if [ "$camera_choice" -eq 0 ]; then
      echo "Operation cancelled."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    # Validate choice and get camera_id
    if ! [[ "$camera_choice" =~ ^[0-9]+$ ]] || [ "$camera_choice" -lt 1 ] || [ "$camera_choice" -gt ${#camera_options[@]} ]; then
      echo "Invalid choice. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    selected_camera_id="${camera_options[$((camera_choice-1))]}"
    echo "Selected camera ID: $selected_camera_id"
    extra_args+=("--camera_id" "$selected_camera_id")

    read -p "Enter license plate (required): " license_plate
    if [ -z "$license_plate" ]; then
      echo "License plate cannot be empty. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi
    extra_args+=("--license_plate" "$license_plate")
  fi

  # Convert script path to module path (e.g., src_helix/test_script.py -> src_helix.test_script)
  local module_path=$(echo "$script_name" | sed 's/\.py$//' | sed 's/\//./g')

  echo "--------------------------------------------------------------------------------"
  echo "Running: python -m $module_path --log_level $LOG_LEVEL ${extra_args[@]}"
  echo "--------------------------------------------------------------------------------"
  # Execute the script as a module
  python -m "$module_path" --log_level "$LOG_LEVEL" "${extra_args[@]}"
  echo "--------------------------------------------------------------------------------"
  read -n 1 -s -r -p "Press any key to return to the menu..."
  echo # Add a newline after the key press
}

# Main loop
while true; do
  clear # Clear screen for better readability
  show_menu
  read -p "Enter your choice [0-9 or L] (default: 0): " choice
  
  # Set default choice to 0 (Exit) if empty
  choice=${choice:-0}

  case $choice in
    1) run_test "src_helix/test_users_list_api.py" ;; # /access/v1/access_users
    2) run_test "src_helix/test_user_details_api.py" ;; # /access/v1/access_users/user
    3) run_test "src_helix/test_access_events_api.py" ;; # /access/v1/events
    4) run_test "src_helix/test_lpr_images_api.py" ;; # /cameras/v1/analytics/lpr/imagesview
    5) run_test "src_helix/test_lpoi_api.py" ;; # /cameras/v1/analytics/lpr/license_plate_of_interest
    6) run_test "src_helix/test_lpr_timestamps_api.py" ;; # /cameras/v1/analytics/lpr/timestamps
    7) run_test "src_helix/test_cameras_api.py" ;; # /cameras/v1/devices
    8) run_test "src_helix/test_notifications_api.py" ;; # /cameras/v1/notifications
    9) run_test "src_helix/test_token_api.py" ;; # /token
    [Ll]) change_log_level ;;
    0) echo "Exiting."; exit 0 ;;
    *) echo "Invalid choice. Please try again." ;;
  esac
  echo # Add a newline for spacing before next menu display
done
