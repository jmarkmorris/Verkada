#!/bin/bash

# Determine the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Determine the repository root directory
# Assume the script is either in the root or in src_helix
if [[ "$SCRIPT_DIR" == */src_helix ]]; then
  # If script is in src_helix, the root is the parent directory
  REPO_ROOT="$(dirname "$SCRIPT_DIR")"
else
  # If script is in the root (or elsewhere), assume the current directory is the root
  REPO_ROOT="$SCRIPT_DIR"
fi

# Change to the repository root directory
# This ensures all relative paths (like src_helix/...) and python module imports (src_helix....)
# work correctly regardless of where the script was called from.
cd "$REPO_ROOT" || { echo "Error: Could not change to repository root $REPO_ROOT"; exit 1; }

# Now the script is running from the repository root.

# Check if API_KEY is set
if [ -z "$API_KEY" ]; then
  echo "Error: API_KEY environment variable is not set."
  echo "Please set it before running this script:"
  echo "  export API_KEY=\"your_verkada_api_key\""
  exit 1
fi

# Default log level - Changed to ERROR
LOG_LEVEL="ERROR"

# Variable to store the captured user list for selection (used by test_user_details_api.py)
USER_LIST_CACHE=""

# Define menu items as an array of strings: "index,description,api_endpoint,script_file"
# Defined globally so it's accessible in the main loop
menu_items=(
  "1,Access Users List,/access/v1/access_users,src_helix/test_users_list_api.py"
  "2,Access User Details,/access/v1/access_users/user,src_helix/test_user_details_api.py"
  "3,Access Events,/access/v1/events,src_helix/test_access_events_api.py"
  "4,LPR Images (Single Cam),/cameras/v1/analytics/lpr/imagesview,src_helix/test_lpr_images_api.py"
  "5,LPOI List,/cameras/v1/analytics/lpr/license_plate_of_interest,src_helix/test_lpoi_api.py"
  "6,LPR Timestamps (Plate/Cam),/cameras/v1/analytics/lpr/timestamps,src_helix/test_lpr_timestamps_api.py"
  "7,Camera List,/cameras/v1/devices,src_helix/test_cameras_api.py"
  "8,Camera Notifications,/cameras/v1/notifications,src_helix/test_notifications_api.py"
  "9,Get API Token,/token,src_helix/test_token_api.py"
  "10,LPR Images (All LPR Cams),/cameras/v1/analytics/lpr/images,src_helix/test_lpr_images_api_all_cameras.py"
  "11,LPR Images (LPOI Match),/cameras/v1/analytics/lpr/images,src_helix/test_lpr_lpoi_match_api.py"
  "12,LPR Images (Non-LPOI),/cameras/v1/analytics/lpr/images,src_helix/test_lpr_non_lpoi_report_api.py"
  "13,LPR Images (Hourly Report),/cameras/v1/analytics/lpr/images,src_helix/test_lpr_hourly_report_api.py"
)


# Function to display the menu
show_menu() {
  echo "============================================================================================================================================"
  echo " Verkada API Test Script Runner"
  echo "============================================================================================================================================"
  # API_KEY and Current Log Level are shown elsewhere or not needed in the main menu
  echo " Select a test to run:"
  echo "============================================================================================================================================"

  # Calculate column widths
  local max_index_width=0
  local max_desc_width=0
  local max_api_width=0
  local max_script_width=0

  for item_string in "${menu_items[@]}"; do
    # Parse the comma-separated string
    IFS=',' read -r index desc api script <<< "$item_string"

    # Use printf %s to handle potential special characters in strings
    local index_len=$(printf "%s" "$index" | wc -m)
    local desc_len=$(printf "%s" "$desc" | wc -m)
    local api_len=$(printf "%s" "$api" | wc -m)
    local script_len=$(printf "%s" "$script" | wc -m)

    if (( index_len > max_index_width )); then max_index_width=$index_len; fi
    if (( desc_len > max_desc_width )); then max_desc_width=$desc_len; fi
    if (( api_len > max_api_width )); then max_api_width=$api_len; fi
    if (( script_len > max_script_width )); then max_script_width=$script_len; fi
  done

  # Add some padding
  max_index_width=$((max_index_width + 2))
  max_desc_width=$((max_desc_width + 2))
  max_api_width=$((max_api_width + 2))
  max_script_width=$((max_script_width + 2))

  # Print header
  printf "%-${max_index_width}s | %-${max_desc_width}s | %-${max_api_width}s | %-${max_script_width}s\n" "Test" "Description" "API Endpoint" "Script File"

  # Print separator line
  printf "%-${max_index_width}s-|-%-${max_desc_width}s-|-%-${max_api_width}s-|-%-${max_script_width}s\n" \
    "$(printf '%*s' "$max_index_width" | tr ' ' '-')" \
    "$(printf '%*s' "$max_desc_width" | tr ' ' '-')" \
    "$(printf '%*s' "$max_api_width" | tr ' ' '-')" \
    "$(printf '%*s' "$max_script_width" | tr ' ' '-')"

  # Print menu items
  for item_string in "${menu_items[@]}"; do
    # Parse the comma-separated string
    IFS=',' read -r index desc api script <<< "$item_string"
    printf "%-${max_index_width}s | %-${max_desc_width}s | %-${max_api_width}s | %-${max_script_width}s\n" "${index})" "$desc" "$api" "$script"
  done

  echo "--------------------------------------------------------------------------------------------------------------------------------------------"
  echo " L) Change Log Level (Current: $LOG_LEVEL)"
  echo " 0) Exit"
  echo "============================================================================================================================================"

  # The menu_items array is now global
}

# Function to change log level
change_log_level() {
  echo "--------------------------------------------------------------------------------------------------------------------------------------------"
  echo " Select Log Level:"
  echo " 1) DEBUG    - Detailed information, useful for diagnosis"
  echo " 2) INFO     - Confirmation that things are working as expected"
  echo " 3) WARNING  - Something unexpected happened, but software is still working"
  echo " 4) ERROR    - Software failed to perform a function due to a problem"
  echo " 5) CRITICAL - Serious error, program may be unable to continue"
  echo "--------------------------------------------------------------------------------------------------------------------------------------------"
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
  local running_comment="" # Variable to hold the comment for the 'Running:' line

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

  # Handle scripts requiring history_hours (Test cases 10, 11, 12, and 13)
  if [[ "$script_name" == "src_helix/test_lpr_images_api_all_cameras.py" || \
        "$script_name" == "src_helix/test_lpr_lpoi_match_api.py" || \
        "$script_name" == "src_helix/test_lpr_non_lpoi_report_api.py" || \
        "$script_name" == "src_helix/test_lpr_hourly_report_api.py" ]]; then
    # Set default to 24 hours for the hourly report, 1 hour for others
    local default_hours=1
    if [[ "$script_name" == "src_helix/test_lpr_hourly_report_api.py" ]]; then
        default_hours=24
    fi
    read -p "Enter history_hours (default: $default_hours): " history_hours
    history_hours=${history_hours:-$default_hours} # Set default
    if ! [[ "$history_hours" =~ ^[0-9]+$ ]]; then
        echo "Invalid input. Using default history_hours=$default_hours."
        history_hours=$default_hours
    fi
    extra_args+=("--history_hours" "$history_hours")
  fi


  # Handle script requiring user_index (Test 2: test_user_details_api.py)
  if [[ "$script_name" == "src_helix/test_user_details_api.py" ]]; then
    echo "Fetching list of access users..."
    # Fetch and list users using test_users_list_api.py as a module with --list-for-selection
    # Capture both stdout and stderr
    # Use python -m to ensure imports within test_users_list_api work correctly
    # Cache the output for potential reuse (though not strictly necessary with current logic)
    USER_LIST_CACHE=$(python -m src_helix.test_users_list_api --log_level "$LOG_LEVEL" --list-for-selection 2>&1)
    script_exit_code=$? # Capture exit code

    if [ "$LOG_LEVEL" == "DEBUG" ]; then
        echo "--- Raw output from test_users_list_api.py ---"
        echo "$USER_LIST_CACHE"
        echo "--- End raw output ---"
    fi

    # Extract only the user list lines after the marker using awk
    # Set flag=1 when marker is found, skip marker line (next), print lines when flag is 1
    user_list_output=$(echo "$USER_LIST_CACHE" | awk '/---START_USER_LIST---/{flag=1; next} flag')

    if [ "$LOG_LEVEL" == "DEBUG" ]; then
        echo "--- Filtered user list output ---"
        echo "$user_list_output"
        echo "--- End filtered output ---"
    fi

    # Check if the script failed or returned an empty list
    if [ $script_exit_code -ne 0 ]; then
      echo "Failed to fetch user list (exit code $script_exit_code). Aborting."
      echo "Please check the 'users_list_api_debug.log' file for details."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    elif [ -z "$user_list_output" ]; then
      # Script exited successfully (0), but no users were listed after the marker
      echo "The API call was successful, but no access users were returned."
      echo "Please check the 'users_list_api_debug.log' file for details if you expected users."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi

    # Build user selection menu (only if list is not empty and script succeeded)
    echo "--------------------------------------------------------------------------------------------------------------------------------------------"
    echo " Select a user for details test:"
    echo "--------------------------------------------------------------------------------------------------------------------------------------------"
    user_options=() # Array to store user_id
    user_display_options=() # Array to store display string (index)
    user_names=() # Array to store user_name for display confirmation
    # user_display_strings=() # Array to store the full display string for passing to script - REMOVED

    # Now pipe the filtered output to the while loop
    while IFS=',' read -r index user_id user_name; do
      # The filtering should ensure we only get valid lines, but keep the check for safety
      if [ -n "$index" ] && [ -n "$user_id" ] && [ -n "$user_name" ]; then
        local display_string="${index}) $user_name (ID: ${user_id:0:5}...)"
        echo " $display_string" # Display user name and truncated ID
        user_options+=("$user_id") # Store user_id in an array
        user_display_options+=("$index") # Store the display index
        user_names+=("$user_name") # Store user name
        # user_display_strings+=("$display_string") # Store the full display string - REMOVED
      fi
    done <<< "$user_list_output" # Use the filtered output

    # This check should technically be redundant now due to the check above,
    # but keeping it doesn't hurt.
    if [ ${#user_options[@]} -eq 0 ]; then
        echo "No users were found or parsed from the list after successful API call."
        echo "This is unexpected. Please check the 'users_list_api_debug.log' file."
        read -n 1 -s -r -p "Press any key to return to the menu..."
        echo
        return
    fi

    echo "--------------------------------------------------------------------------------------------------------------------------------------------"
    echo " 0) Cancel"
    echo "--------------------------------------------------------------------------------------------------------------------------------------------"

    read -p "Enter your choice: " user_choice

    # --- Start of fix for empty input ---
    if [ -z "$user_choice" ]; then
      echo "Invalid choice. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi
    # --- End of fix for empty input ---

    if [ "$user_choice" -eq 0 ]; then
      echo "Operation cancelled."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    # Validate choice and get the corresponding 0-based index
    # Find the index in user_display_options that matches the user_choice
    selected_index=-1
    for i in "${!user_display_options[@]}"; do
        if [[ "${user_display_options[$i]}" == "$user_choice" ]]; then
            selected_index=$i
            break
        fi
    done

    if [ "$selected_index" -eq -1 ]; then
      echo "Invalid choice. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    # Pass the 0-based index and the 1-based user number to the script
    # Print a confirmation message using the user's choice and the selected user's name/ID
    echo "Selected choice $user_choice: ${user_names[$selected_index]} (ID: ${user_options[$selected_index]:0:5}...)"

    # Add arguments for user index (0-based) and user number (1-based)
    extra_args+=("--user_index" "$selected_index")
    extra_args+=("--user_number" "$user_choice")
    # Removed --user_display_string argument

    # Set the running comment for this specific script
    # The comment is no longer needed as --user_number is explicit
    # running_comment="# corresponds to user number $user_choice"
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
    echo "--------------------------------------------------------------------------------------------------------------------------------------------"
    echo " Select a camera for LPR timestamps test:"
    echo " (Choose an LPR-enabled camera)"
    echo "--------------------------------------------------------------------------------------------------------------------------------------------"
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

    echo "--------------------------------------------------------------------------------------------------------------------------------------------"
    echo " 0) Cancel"
    echo "--------------------------------------------------------------------------------------------------------------------------------------------"

    read -p "Enter your choice: " camera_choice

    # --- Start of fix for empty input ---
    if [ -z "$camera_choice" ]; then
      echo "Invalid choice. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi
    # --- End of fix for empty input ---

    if [ "$camera_choice" -eq 0 ]; then
      echo "Operation cancelled."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    # Validate choice and get camera_id
    # The check below now assumes camera_choice is not empty due to the check above
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

  # Conditionally add the --log_level argument. Omit if the selected level is ERROR,
  # as the Python scripts' default will be changed to ERROR.
  local log_level_arg=""
  if [ "$LOG_LEVEL" != "ERROR" ]; then
      log_level_arg="--log_level $LOG_LEVEL"
  fi

  echo "--------------------------------------------------------------------------------------------------------------------------------------------"
  # Append the running_comment if it's set - REMOVED "$running_comment"
  echo "Running: python -m $module_path $log_level_arg ${extra_args[@]}"
  echo "--------------------------------------------------------------------------------------------------------------------------------------------"
  # Execute the script as a module
  python -m "$module_path" $log_level_arg "${extra_args[@]}"
  echo "--------------------------------------------------------------------------------------------------------------------------------------------"
  read -n 1 -s -r -p "Press any key to return to the menu..."
  echo # Add a newline after the key press
}

# Main loop
while true; do
  clear # Clear screen for better readability
  show_menu
  read -p "Enter your choice [0-13 or L] (default: 0): " choice

  # Set default choice to 0 (Exit) if empty
  choice=${choice:-0}

  # Find the selected script file based on the choice and the menu_items array
  # Removed 'local' keyword to avoid "local: can only be used in a function" error
  selected_script=""
  if [[ "$choice" =~ ^[0-9]+$ ]]; then
      # Iterate through the menu_items array to find the matching index
      for item_string in "${menu_items[@]}"; do
          # Parse the comma-separated string
          IFS=',' read -r index desc api script <<< "$item_string"
          if [[ "$index" == "$choice" ]]; then
              selected_script="$script"
              break
          fi
      done
  fi


  case $choice in
    [Ll]) change_log_level ;;
    0) echo "Exiting."; exit 0 ;;
    *)
      if [ -n "$selected_script" ]; then
          run_test "$selected_script"
      else
          echo "Invalid choice. Please try again."
          read -n 1 -s -r -p "Press any key to return to the menu..."
          echo
      fi
      ;;
  esac
  echo # Add a newline for spacing before next menu display
done
