import logging
from datetime import datetime, timezone

# Configure logging for this module
# The level will be set by the root logger configuration in lambda_function.py
logger = logging.getLogger(__name__)

# Helper function to format timestamp
def format_timestamp(unix_timestamp):
    """Converts a Unix epoch timestamp to a readable string."""
    if not isinstance(unix_timestamp, (int, float)):
        logger.debug(f"Timestamp '{unix_timestamp}' is not a number, returning as string.")
        return str(unix_timestamp) # Return as is if not a valid number
    try:
        # Assume UTC timestamp from Verkada, convert to local timezone display
        dt_object = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc).astimezone()
        # Format: YYYY-MM-DD HH:MM:SS ZZZ (e.g., 2025-04-12 17:30:20 EDT) - needs ~24 chars
        return dt_object.strftime('%Y-%m-%d %H:%M:%S %Z')
    except Exception as e:
        # Use warning level as this indicates a potential issue with timestamp data
        logger.warning(f"Could not format timestamp {unix_timestamp}: {e}")
        return str(unix_timestamp) # Fallback to original string

# Functions for processing specific event types

def process_lpr_event(payload):
    """
    Processes a License Plate Recognition event payload.
    Extracts key information and logs it.
    """
    try:
        # Extract relevant fields
        event_data = payload.get('data', {})
        timestamp_unix = event_data.get('created', payload.get('created_at')) # Get Unix timestamp
        plate_number = event_data.get('license_plate_number', '') # Default to empty string if missing

        # Format timestamp
        formatted_time = format_timestamp(timestamp_unix)
        # Prepare plate string (first 10 chars)
        plate_str = (plate_number or '')[:10]

        # Log the processed event information using INFO level
        # Format: Plate/Cred (12), Door (20), User (35), Time (25)
        log_message = f"LPR Event: {plate_str:<12} {'':<20} {'':<35} {formatted_time:<25}"
        logger.info(log_message) # Replaced print with logger.info

    except KeyError as e:
        logger.error(f"Missing expected key in LPR payload: {e}")
    except Exception as e:
        logger.error(f"Error processing LPR event: {e}", exc_info=True)


def process_access_event(payload):
    """
    Processes an Access Control event payload (potentially wrapped in a 'notification').
    Extracts key information and logs it.
    """
    try:
        # Data might be nested under 'data' if it's a 'notification' type
        event_data = payload.get('data', payload) # Use top-level payload if 'data' key doesn't exist

        timestamp_unix = event_data.get('created', payload.get('created_at')) # Get Unix timestamp
        formatted_time = format_timestamp(timestamp_unix)

        # Door info might be nested further
        door_info = event_data.get('door_info', {})
        if door_info is None: door_info = {}
        door_name = door_info.get('name', event_data.get('door_name', event_data.get('door_id', ''))) # Default to empty

        # User info might be nested
        user_info = event_data.get('user_info', {})
        if user_info is None: user_info = {}
        user_desc = user_info.get('name', event_data.get('user_description', event_data.get('person_id', ''))) # Default to empty

        # Input value might contain the credential identifier for some notification types
        credential_identifier = event_data.get('input_value', event_data.get('credential_identifier', '')) # Default to empty

        # Prepare strings for logging, handling None and length limits
        cred_str = (credential_identifier or '')[:10]
        door_str = (door_name or '')
        user_str = (user_desc or '')

        # Log the processed event information using INFO level
        # Format: Plate/Cred (12), Door (20), User (35), Time (25)
        log_message = f"Access Event: {cred_str:<12} {door_str:<20} {user_str:<35} {formatted_time:<25}"
        logger.info(log_message) # Replaced print with logger.info

    except KeyError as e:
        logger.error(f"Missing expected key in Access payload: {e}")
    except Exception as e:
        logger.error(f"Error processing Access event: {e}", exc_info=True)


# Main event handler/dispatcher called by lambda_function.py

def handle_event(payload):
    """
    Determines the type of webhook event and calls the appropriate handler.

    Args:
        payload (dict): The JSON payload received from the webhook.
    """
    logger.debug(f"Handling event payload: {payload}") # Log full payload only at DEBUG level

    # --- Determine Event Type ---
    webhook_type = payload.get('webhook_type') # Explicit type field from Verkada

    if webhook_type == 'lpr':
        logger.info(f"Dispatching LPR event...")
        process_lpr_event(payload)
    elif webhook_type == 'notification':
        # Notifications often wrap other event types, check nested data
        notification_type = payload.get('data', {}).get('notification_type', '')
        logger.info(f"Dispatching Notification event (Type: {notification_type})...")
        # Assuming 'notification' types related to access control should use process_access_event
        if 'door' in notification_type:
             process_access_event(payload)
        elif notification_type == 'license_plate_of_interest':
             # Log that we received it, but don't process further for Phase 1 unless requested
             logger.info(f"Received 'license_plate_of_interest' notification. No specific action defined.")
             # Optionally, you could call process_lpr_event if the structure is similar enough
             # process_lpr_event(payload)
        else:
             # Use warning level for unhandled types
             logger.warning(f"Received unhandled notification type: {notification_type}")
    elif webhook_type == 'access_event': # Handle direct access events if they exist
         logger.info(f"Dispatching Access event...")
         process_access_event(payload)
    # Fallback check using keys if webhook_type is missing (less reliable)
    elif 'license_plate_number' in payload.get('data', {}):
        logger.info(f"Dispatching LPR event (detected by key)...")
        process_lpr_event(payload)
    elif 'door_id' in payload.get('data', {}):
        logger.info(f"Dispatching Access event (detected by key)...")
        process_access_event(payload)
    else:
        # Fallback if type is unknown or keys don't match
        # Use warning level for unknown/unsupported types
        logger.warning(f"Received unknown or unsupported event type. Webhook Type Field: '{webhook_type}'. Keys: {list(payload.keys())}")
