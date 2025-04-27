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

# Check if jq is installed
if ! command -v jq &> /dev/null
then
    echo "Error: jq is not installed."
    echo "jq is required to parse JSON output from helper scripts."
    echo "Please install jq (e.g., 'brew install jq' on macOS, 'sudo apt-get install jq' on Debian/Ubuntu)."
    exit 1
fi


# Default log level - Changed to ERROR
LOG_LEVEL="ERROR"

# Variable to store the captured user list for selection (used by test_user_details_api.py)
# USER_LIST_CACHE="" # No longer needed with direct JSON parsing

# Define menu items as an array of strings: "index|description|api_endpoint|script_file"
# Using '|' as a delimiter instead of ',' to handle commas in descriptions/paths.
# Defined globally so it's accessible in the main loop
# Order: /token first, then others sorted alphabetically by API Endpoint
menu_items=(
  "1|Get API Token|/token|src_helix/test_token_api.py"
  "2|Access Users List|/access/v1/access_users|src_helix/test_users_list_api.py"
  "3|Access User Details|/access/v1/access_users/user|src_helix/test_user_details_api.py"
  "4|Camera Notifications|/cameras/v1/alerts|src_helix/test_notifications_api.py"
  "5|LPR Events (All LPR Cams)|/cameras/v1/analytics/lpr/images|src_helix/test_lpr_images_api_all_cameras.py"
  "6|LPR Events (LPOI Match)|/cameras/v1/analytics/lpr/images|src_helix/test_lpr_lpoi_match_api.py"
  "7|LPR Events (Non-LPOI)|/cameras/v1/analytics/lpr/images|src_helix/test_lpr_non_lpoi_report_api.py"
  "8|LPR Events (Hourly Report)|/cameras/v1/analytics/lpr/images|src_helix/test_lpr_hourly_report_api.py"
  "9|LPOI List|/cameras/v1/analytics/lpr/license_plate_of_interest|src_helix/test_lpoi_api.py"
  "10|LPR Timestamps (Plate/Cam)|/cameras/v1/analytics/lpr/timestamps|src_helix/test_lpr_timestamps_api.py"
  "11|Camera List|/cameras/v1/devices|src_helix/test_cameras_api.py"
  "12|Access Events|/events/v1/access|src_helix/test_access_events_api.py"
)

# Define a fixed width for separators outside the main menu table
FIXED_SEPARATOR_WIDTH=120

# Function to display the menu
show_menu() {
  # Calculate column widths
  local max_index_width=0
  local max_desc_width=0
  local max_api_width=0
  local max_script_display_width=0 # New variable for displayed script name width

  for item_string in "${menu_items[@]}"; do
    # Parse the pipe-separated string
    IFS='|' read -r index desc api script <<< "$item_string"

    # Get the script filename without the path for display
    local script_display_name=$(basename "$script")

    # Use printf %s to handle potential special characters in strings
    local index_len=$(printf "%s" "$index" | wc -m)
    local desc_len=$(printf "%s" "$desc" | wc -m)
    local api_len=$(printf "%s" "$api" | wc -m)
    local script_display_len=$(printf "%s" "$script_display_name" | wc -m) # Use display name length

    if (( index_len > max_index_width )); then max_index_width=$index_len; fi
    if (( desc_len > max_desc_width )); then max_desc_width=$desc_len; fi
    if (( api_len > max_api_width )); then max_api_width=$api_len; fi
    if (( script_display_len > max_script_display_width )); then max_script_display_width=$script_display_len; fi # Use display width
  done

  # Add some padding
  max_index_width=$((max_index_width + 2))
  max_desc_width=$((max_desc_width + 2))
  max_api_width=$((max_api_width + 2))
  max_script_display_width=$((max_script_display_width + 2)) # Use display width

  # Calculate the total width of the menu table including separators and padding
  # 4 columns + 3 separators (' | ')
  local total_menu_width=$((max_index_width + max_desc_width + max_api_width + max_script_display_width + (3 * 3)))


  # Print header using calculated width
  printf "%*s\n" "$total_menu_width" | tr ' ' '=' # Top separator line (===)
  echo " Verkada API Test Script Runner"
  printf "%*s\n" "$total_menu_width" | tr ' ' '=' # Separator line (===)
  echo " Select a test to run:"
  printf "%*s\n" "$total_menu_width" | tr ' ' '=' # Separator line (===)

  # Print table header
  printf "%-${max_index_width}s | %-${max_desc_width}s | %-${max_api_width}s | %-${max_script_display_width}s\n" "Test" "Description" "API Endpoint" "Script File" # Use display width in header

  # Print header separator line (---)
  printf "%*s\n" "$total_menu_width" | tr ' ' '-' # Header separator line (---)

  # Print menu items
  for item_string in "${menu_items[@]}"; do
    # Parse the pipe-separated string
    IFS='|' read -r index desc api script <<< "$item_string"
    # Get the script filename without the path for display
    local script_display_name=$(basename "$script")
    printf "%-${max_index_width}s | %-${max_desc_width}s | %-${max_api_width}s | %-${max_script_display_width}s\n" "${index})" "$desc" "$api" "$script_display_name" # Print display name
  done

  # Print bottom separator line (---)
  printf "%*s\n" "$total_menu_width" | tr ' ' '-' # Bottom separator line (---)

  echo " L) Change Log Level (Current: $LOG_LEVEL)"
  echo " 0) Exit"
  printf "%*s\n" "$total_menu_width" | tr ' ' '=' # Bottom separator line (===)

  # The menu_items array is now global
}

# Function to change log level
change_log_level() {
  printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
  echo " Select Log Level:"
  echo " 1) DEBUG    - Detailed information, useful for diagnosis"
  echo " 2) INFO     - Confirmation that things are working as expected"
  echo " 3) WARNING  - Something unexpected happened, but software is still working"
  echo " 4) ERROR    - Software failed to perform a function due to a problem"
  echo " 5) CRITICAL - Serious error, program may be unable to continue"
  printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
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

# Function to get time-based arguments based on script name
get_time_args() {
    local script_name="$1"
    local args=()

    case "$script_name" in
        src_helix/test_notifications_api.py|src_helix/test_access_events_api.py)
            # Scripts requiring history_days (Test 4, 12)
            read -p "Enter history_days (default: 7): " history_days
            history_days=${history_days:-7} # Set default if empty
            if ! [[ "$history_days" =~ ^[0-9]+$ ]]; then
                echo "Invalid input. Using default history_days=7."
                history_days=7
            fi
            args+=("--history_days" "$history_days")
            ;;
        src_helix/test_lpr_timestamps_api.py)
             # Script requiring history_days (Test 10) - also needs camera_id and license_plate
             # history_days prompt is handled here, camera/plate selection is handled later in run_test
            read -p "Enter history_days (default: 7): " history_days
            history_days=${history_days:-7} # Set default if empty
            if ! [[ "$history_days" =~ ^[0-9]+$ ]]; then
                echo "Invalid input. Using default history_days=7."
                history_days=7
            fi
            args+=("--history_days" "$history_days")
            ;;
        src_helix/test_lpr_images_api_all_cameras.py|src_helix/test_lpr_lpoi_match_api.py|src_helix/test_lpr_non_lpoi_report_api.py|src_helix/test_lpr_hourly_report_api.py)
            # Scripts requiring history_hours (Test 5, 6, 7, 8)
            local default_hours=1
            if [[ "$script_name" == "src_helix/test_lpr_hourly_report_api.py" ]]; then
                default_hours=24 # Default to 24 hours for the hourly report
            fi
            read -p "Enter history_hours (default: $default_hours): " history_hours
            history_hours=${history_hours:-$default_hours} # Set default
            if ! [[ "$history_hours" =~ ^[0-9]+$ ]]; then
                echo "Invalid input. Using default history_hours=$default_hours."
                history_hours=$default_hours
            fi
            args+=("--history_hours" "$history_hours")
            ;;
        *)
            # No time-based arguments needed for other scripts
            ;;
    esac

    echo "${args[@]}" # Return the arguments as a space-separated string
}


# Function to run a test script
run_test() {
  local script_name="$1"
  local extra_args=()

  # Get time-based arguments using the new function
  # Read the space-separated string into the extra_args array
  read -r -a time_args <<< "$(get_time_args "$script_name")"
  extra_args+=("${time_args[@]}")


  # Handle script requiring user_index (Test 3: test_user_details_api.py)
  if [[ "$script_name" == "src_helix/test_user_details_api.py" ]]; then
    echo "Fetching list of access users..."
    # Call list_items.py to get the full user list as JSON
    # Direct stderr to /dev/null to keep output clean, unless LOG_LEVEL is DEBUG
    local list_output
    if [ "$LOG_LEVEL" == "DEBUG" ]; then
        list_output=$(python -m src_helix.list_items --type users --log_level DEBUG)
        list_exit_code=$?
    else
        list_output=$(python -m src_helix.list_items --type users --log_level ERROR 2>/dev/null)
        list_exit_code=$?
    fi


    if [ $list_exit_code -ne 0 ]; then
      echo "Failed to fetch user list (exit code $list_exit_code). Cannot run user details test."
      echo "Check logs for list_items.py for details."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi

    # Parse the JSON output using jq to get an array of objects with index, user_id, and full_name
    # jq filter: .[] | {index: (. | input_line_number), user_id: .user_id, full_name: .full_name}
    # This creates an array of objects like [{"index": 1, "user_id": "...", "full_name": "..."}, ...]
    # Then we iterate over this array in bash
    local user_list_json=$(echo "$list_output" | jq -c '.[] | {user_id: .user_id, full_name: .full_name}')

    if [ -z "$user_list_json" ]; then
      echo "User list is empty or could not be parsed. Cannot run user details test."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi

    # Build user selection menu from the parsed JSON
    printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
    echo " Select a user for details test:"
    printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
    user_options=() # Array to store user_id
    user_names=() # Array to store user_name for display confirmation

    local i=0
    while IFS= read -r user_obj; do
        local user_id=$(echo "$user_obj" | jq -r '.user_id')
        local full_name=$(echo "$user_obj" | jq -r '.full_name')
        local display_index=$((i + 1))

        # Handle potential null or empty full_name
        if [ "$full_name" == "null" ] || [ -z "$full_name" ]; then
            full_name="Unnamed User"
        fi

        # Handle potential null or empty user_id
        if [ "$user_id" == "null" ] || [ -z "$user_id" ]; then
            echo "Skipping user entry with missing user_id." >&2 # Log to stderr
            continue # Skip this entry
        fi

        local display_string="${display_index}) $full_name (ID: ${user_id:0:5}...)"
        echo " $display_string" # Display user name and truncated ID

        user_options+=("$user_id") # Store user_id in an array
        user_names+=("$full_name") # Store user name
        i=$((i + 1))
    done <<< "$user_list_json"


    if [ ${#user_options[@]} -eq 0 ]; then
        echo "No valid users were found or parsed from the list."
        echo "Please check the list_items_debug.log file."
        read -n 1 -s -r -p "Press any key to return to the menu..."
        echo
        return
    fi

    printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
    echo " 0) Cancel"
    printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)

    read -p "Enter your choice: " user_choice

    if [ -z "$user_choice" ]; then
      echo "Invalid choice. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi

    if [ "$user_choice" -eq 0 ]; then
      echo "Operation cancelled."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    # Validate choice and get the corresponding 0-based index
    local selected_index=$((user_choice - 1))

    if [ "$selected_index" -lt 0 ] || [ "$selected_index" -ge ${#user_options[@]} ]; then
      echo "Invalid choice. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    local user_id_to_fetch="${user_options[$selected_index]}"
    local selected_user_name="${user_names[$selected_index]}"

    # Print a confirmation message using the user's choice and the selected user's name/ID
    echo "Selected choice $user_choice: ${selected_user_name} (ID: ${user_id_to_fetch:0:5}...)"

    # Add arguments for user index (0-based) and user number (1-based)
    # The script test_user_details_api.py still expects --user_index and --user_number
    # based on the *original* list order from the API, not the filtered/displayed list.
    # We need to pass the *original* index from the full list.
    # Let's re-think this. The script test_user_details_api.py only needs the user_id.
    # The --user_index and --user_number arguments were remnants of the old parsing logic.
    # Let's simplify test_user_details_api.py to only require --user_id.

    # --- Re-evaluating test_user_details_api.py arguments ---
    # The script test_user_details_api.py currently takes --user_index and --user_number.
    # It uses --user_index to get the user_id from a *silently fetched* list.
    # This is still coupled. Let's change test_user_details_api.py to take --user_id directly.

    # --- Revised Plan for Test 3 ---
    # 1. Modify test_user_details_api.py to accept --user_id instead of --user_index/--user_number.
    # 2. In runtest.sh, after selecting the user, pass the selected user_id to test_user_details_api.py.
    # 3. Remove the silent fetch and index logic from test_user_details_api.py main function.

    # Let's implement step 2 here first, assuming step 1 will be done in test_user_details_api.py.
    extra_args+=("--user_id" "$user_id_to_fetch")

  fi

  # Handle script requiring license_plate and camera_id (via selection menu)
  # Test 10: test_lpr_timestamps_api.py
  if [[ "$script_name" == "src_helix/test_lpr_timestamps_api.py" ]]; then
    echo "Fetching list of all cameras..."
    # Call list_items.py to get the full camera list as JSON
    # Direct stderr to /dev/null to keep output clean, unless LOG_LEVEL is DEBUG
    local list_output
    if [ "$LOG_LEVEL" == "DEBUG" ]; then
        list_output=$(python -m src_helix.list_items --type cameras --log_level DEBUG)
        list_exit_code=$?
    else
        list_output=$(python -m src_helix.list_items --type cameras --log_level ERROR 2>/dev/null)
        list_exit_code=$?
    fi

    if [ $list_exit_code -ne 0 ]; then
      echo "Failed to fetch camera list (exit code $list_exit_code). Cannot run LPR timestamps test."
      echo "Check logs for list_items.py for details."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi

    # Parse the JSON output using jq to get an array of objects with index, camera_id, and name
    local camera_list_json=$(echo "$list_output" | jq -c '.[] | {camera_id: .camera_id, name: .name}')

    if [ -z "$camera_list_json" ]; then
      echo "Camera list is empty or could not be parsed. Cannot run LPR timestamps test."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi

    # Build camera selection menu
    printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
    echo " Select a camera for LPR timestamps test:"
    echo " (Choose an LPR-enabled camera if possible)"
    printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
    camera_options=() # Array to store camera_id
    camera_names=() # Array to store camera_name for display confirmation

    local i=0
    while IFS= read -r camera_obj; do
        local camera_id=$(echo "$camera_obj" | jq -r '.camera_id')
        local camera_name=$(echo "$camera_obj" | jq -r '.name')
        local display_index=$((i + 1))

        # Handle potential null or empty name
        if [ "$camera_name" == "null" ] || [ -z "$camera_name" ]; then
            camera_name="Unnamed Camera"
        fi

        # Handle potential null or empty camera_id
        if [ "$camera_id" == "null" ] || [ -z "$camera_id" ]; then
            echo "Skipping camera entry with missing camera_id." >&2 # Log to stderr
            continue # Skip this entry
        fi

        local display_string="${display_index}) $camera_name (ID: ${camera_id:0:5}...)"
        echo " $display_string" # Display camera name and truncated ID

        camera_options+=("$camera_id") # Store camera_id in an array
        camera_names+=("$camera_name") # Store camera name
        i=$((i + 1))
    done <<< "$camera_list_json"


    if [ ${#camera_options[@]} -eq 0 ]; then
        echo "No valid cameras were found or parsed from the list."
        echo "Please check the list_items_debug.log file."
        read -n 1 -s -r -p "Press any key to return to the menu..."
        echo
        return
    fi


    printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
    echo " 0) Cancel"
    printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)

    read -p "Enter your choice: " camera_choice

    if [ -z "$camera_choice" ]; then
      echo "Invalid choice. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return # Exit the run_test function
    fi

    if [ "$camera_choice" -eq 0 ]; then
      echo "Operation cancelled."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    # Validate choice and get camera_id
    local selected_index=$((camera_choice - 1))

    if [ "$selected_index" -lt 0 ] || [ "$selected_index" -ge ${#camera_options[@]} ]; then
      echo "Invalid choice. Aborting."
      read -n 1 -s -r -p "Press any key to return to the menu..."
      echo
      return
    fi

    local selected_camera_id="${camera_options[$selected_index]}"
    local selected_camera_name="${camera_names[$selected_index]}"

    echo "Selected camera: ${selected_camera_name} (ID: ${selected_camera_id:0:5}...)"
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

  printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
  echo "Running: python -m $module_path $log_level_arg ${extra_args[@]}"
  printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
  # Execute the script as a module
  python -m "$module_path" $log_level_arg "${extra_args[@]}"
  printf "%*s\n" "$FIXED_SEPARATOR_WIDTH" | tr ' ' '-' # Separator line (---)
  read -n 1 -s -r -p "Press any key to return to the menu..."
  echo # Add a newline after the key press
}

# Main loop
while true; do
  clear # Clear screen for better readability
  show_menu
  # Updated prompt to reflect new number of tests (12)
  read -p "Enter your choice [0-12 or L] (default: 0): " choice

  # Set default choice to 0 (Exit) if empty
  choice=${choice:-0}

  # Find the selected script file based on the choice and the menu_items array
  # Removed 'local' keyword to avoid "local: can only be used in a function" error
  selected_script=""
  if [[ "$choice" =~ ^[0-9]+$ ]]; then
      # Iterate through the menu_items array to find the matching index
      for item_string in "${menu_items[@]}"; do
          # Parse the pipe-separated string
          IFS='|' read -r index desc api script <<< "$item_string"
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
          # Updated error message to reflect new number of tests
          echo "Invalid choice. Please try again. Enter a number between 0 and 12, or 'L'."
          read -n 1 -s -r -p "Press any key to return to the menu..."
          echo
      fi
      ;;
  esac
  echo # Add a newline for spacing before next menu display
done
