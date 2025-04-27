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


# Default log level for automated tests - INFO is a good balance
LOG_LEVEL="INFO"

# Define the list of tests to run automatically.
# Excludes tests that require specific, non-automatable user input (like LPR timestamps).
# Includes tests that can be run with default or programmatically determined parameters.
# Format: "Description|script_file"
test_list=(
  "Get API Token|src_helix/test_token_api.py"
  "Access Users List|src_helix/test_users_list_api.py"
  "Access User Details|src_helix/test_user_details_api.py" # Handled specially below
  "Camera Notifications|src_helix/test_notifications_api.py"
  "LPR Events (All LPR Cams)|src_helix/test_lpr_images_api_all_cameras.py"
  "LPR Events (LPOI Match)|src_helix/test_lpr_lpoi_match_api.py"
  "LPR Events (Non-LPOI)|src_helix/test_lpr_non_lpoi_report_api.py"
  "LPR Events (Hourly Report)|src_helix/test_lpr_hourly_report_api.py"
  "LPOI List|src_helix/test_lpoi_api.py"
  "Camera List|src_helix/test_cameras_api.py"
  "Access Events|src_helix/test_access_events_api.py"
)

# Define tests that will be skipped
skipped_tests=(
  "LPR Timestamps (Plate/Cam)|src_helix/test_lpr_timestamps_api.py" # Requires specific plate/cam input
)

# Counters
total_tests_to_attempt=${#test_list[@]} # Total tests we attempt to run
passed_count=0
failed_count=0
design_skipped_count=${#skipped_tests[@]} # Initialize with count of explicitly skipped tests
# Removed runtime_skipped_count

# Fixed width for separators
SEPARATOR_WIDTH=80

# Function to print a separator line
print_separator() {
  printf "%*s\n" "$SEPARATOR_WIDTH" | tr ' ' "$1"
}

echo "================================================================================"
echo " Running Verkada API Automated Tests"
echo " Log Level: $LOG_LEVEL"
echo "================================================================================"
echo ""

# Run the defined tests
for test_item in "${test_list[@]}"; do
  # Parse the pipe-separated string
  IFS='|' read -r description script_file <<< "$test_item"

  print_separator "-"
  echo "Running Test: $description"
  echo "Script: $(basename "$script_file")"
  print_separator "-"

  extra_args=()
  skip_current_test=false # Flag to skip the current test if setup fails

  # Add log level argument (only if not default ERROR)
  log_level_arg=""
  if [ "$LOG_LEVEL" != "ERROR" ]; then
      log_level_arg="--log_level $LOG_LEVEL"
  fi

  # --- Handle specific tests requiring parameters ---
  case "$script_file" in
    src_helix/test_notifications_api.py|src_helix/test_access_events_api.py)
      # These tests accept --history_days, use a default value
      extra_args+=("--history_days" "1") # Use 1 day for quick run
      echo "  -> Using default history_days=1"
      ;;
    src_helix/test_lpr_images_api_all_cameras.py|src_helix/test_lpr_lpoi_match_api.py|src_helix/test_lpr_non_lpoi_report_api.py|src_helix/test_lpr_hourly_report_api.py)
      # These tests accept --history_hours, use a default value
      default_hours=1
      if [[ "$script_file" == "src_helix/test_lpr_hourly_report_api.py" ]]; then
          default_hours=1 # Use 1 hour for quick run of hourly report
      fi
      extra_args+=("--history_hours" "$default_hours")
      echo "  -> Using default history_hours=$default_hours"
      ;;
    src_helix/test_user_details_api.py)
      # This test requires a user_id. We need to fetch the user list and pick the first one.
      echo "  -> Fetching user list to select first user..."
      # Call list_items.py to get the full user list as JSON
      # Direct stderr to /dev/null to keep output clean, unless LOG_LEVEL is DEBUG
      # Removed 'local' from list_output declaration
      list_output=""
      if [ "$LOG_LEVEL" == "DEBUG" ]; then
          list_output=$(python -m src_helix.list_items --type users --log_level DEBUG)
          list_exit_code=$?
      else
          list_output=$(python -m src_helix.list_items --type users --log_level ERROR 2>/dev/null)
          list_exit_code=$?
      fi

      if [ $list_exit_code -ne 0 ]; then
        echo "  -> Failed to fetch user list (exit code $list_exit_code). Cannot run user details test."
        echo "     Check logs for list_items.py for details."
        skip_current_test=true
      else
        # Parse the JSON output using jq to get the first user's user_id and full_name
        # .[0] gets the first object in the array
        first_user_id=$(echo "$list_output" | jq -r '.[0].user_id')
        first_user_name=$(echo "$list_output" | jq -r '.[0].full_name')

        if [ "$first_user_id" == "null" ] || [ -z "$first_user_id" ]; then
          echo "  -> User list is empty or first user has no user_id. Cannot run user details test."
          skip_current_test=true
        else
          # Handle potential null or empty full_name
          if [ "$first_user_name" == "null" ] || [ -z "$first_user_name" ]; then
              first_user_name="Unnamed User"
          fi
          # Pass the user_id to the script (assuming test_user_details_api.py is updated)
          extra_args+=("--user_id" "$first_user_id")
          echo "  -> Selected first user: ${first_user_name} (ID: ${first_user_id:0:5}...)"
        fi
      fi
      ;;
    # src_helix/test_lpr_timestamps_api.py is intentionally skipped
  esac
  # --- End specific test handling ---

  if [ "$skip_current_test" = true ]; then
    echo "FAIL: $description (Runtime Setup Failed)" # Changed from SKIP to FAIL
    # Increment failed_count for tests skipped due to setup failure
    failed_count=$((failed_count + 1)) # Changed from runtime_skipped_count
  else
    # Convert script path to module path (e.g., src_helix/test_script.py -> src_helix.test_script)
    module_path=$(echo "$script_file" | sed 's/\.py$//' | sed 's/\//./g')

    # Conditionally add the --log_level argument. Omit if the selected level is ERROR,
    # as the Python scripts' default will be changed to ERROR.
    # log_level_arg is already declared above without local

    printf "%*s\n" "$SEPARATOR_WIDTH" | tr ' ' "-"
    echo "Running: python -m $module_path $log_level_arg ${extra_args[@]}"
    printf "%*s\n" "$SEPARATOR_WIDTH" | tr ' ' "-"
    # Execute the script as a module
    # Use set -o pipefail to ensure the exit code of the python command is captured
    # even if it's piped (though not currently piping stdout here)
    set -o pipefail
    python -m "$module_path" $log_level_arg "${extra_args[@]}"
    exit_code=$?
    set +o pipefail # Turn pipefail off

    if [ $exit_code -eq 0 ]; then
      echo "PASS: $description"
      passed_count=$((passed_count + 1))
    else
      echo "FAIL: $description (Exit Code: $exit_code)"
      failed_count=$((failed_count + 1))
    fi
  fi

  echo "" # Blank line after each test result
done

# Report explicitly skipped tests
if [ ${#skipped_tests[@]} -gt 0 ]; then
  print_separator "-"
  echo "Tests Skipped by Design:"
  print_separator "-"
  for skipped_item in "${skipped_tests[@]}"; do
    IFS='|' read -r description script_file <<< "$skipped_item"
    echo "SKIP: $description ($(basename "$script_file"))"
  done
  echo ""
fi


# Final Summary
echo "================================================================================"
echo " Test Summary"
echo "================================================================================"
# Calculate total defined tests (attempted + skipped by design)
total_defined=$((total_tests_to_attempt + design_skipped_count))
echo " Total Tests Defined: $total_defined"
echo " Tests Attempted: $total_tests_to_attempt"
echo " Passed: $passed_count"
echo " Failed: $failed_count" # Now includes runtime setup failures
echo " Skipped (by design): $design_skipped_count" # Only shows design skips
# Removed runtime skipped count line
echo "================================================================================"

# Exit with a non-zero status if any tests failed
if [ $failed_count -gt 0 ]; then
  exit 1
else
  exit 0
fi
