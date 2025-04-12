import logging
from datetime import datetime, timezone

# Helper function to format timestamp
def format_timestamp(unix_timestamp):
    """Converts a Unix epoch timestamp to a readable string."""
    if not isinstance(unix_timestamp, (int, float)):
        return str(unix_timestamp) # Return as is if not a valid number
    try:
        # Assume UTC timestamp from Verkada, convert to local timezone display
        dt_object = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc).astimezone()
        return dt_object.strftime('%Y-%m-%d %H:%M:%S %Z') # e.g., 2025-04-12 17:30:20 EDT
    except Exception as e:
        logging.warning(f"Could not format timestamp {unix_timestamp}: {e}")
        return str(unix_timestamp) # Fallback to original string

# Placeholder functions for processing specific event types

def process_lpr_event(payload):
    """
    Processes a License Plate Recognition event payload.
    Extracts key information and prints it.
    """
    try:
        # Extract relevant fields
        event_data = payload.get('data', {})
        timestamp_unix = event_data.get('created', payload.get('created_at')) # Get Unix timestamp
        plate_number = event_data.get('license_plate_number', 'N/A')

        # Format timestamp
        formatted_time = format_timestamp(timestamp_unix)

        output = (
            f"Plate: {plate_number}, Time: {formatted_time}"
        )
        print(output) # Print essential info to console always
        # logging.info(output) # Log only if verbose (handled by level setting in app.py)
    except KeyError as e:
        logging.error(f"Missing expected key in LPR payload: {e}")
    except Exception as e:
        logging.error(f"Error processing LPR event: {e}", exc_info=True)


def process_access_event(payload):
    """
    Processes an Access Control event payload (potentially wrapped in a 'notification').
    Extracts key information and prints it.
    """
    try:
        # Data might be nested under 'data' if it's a 'notification' type
        event_data = payload.get('data', payload) # Use top-level payload if 'data' key doesn't exist

        timestamp_unix = event_data.get('created', payload.get('created_at')) # Get Unix timestamp

        # Door info might be nested further
        door_info = event_data.get('door_info', {})
        door_name = door_info.get('name', event_data.get('door_name', event_data.get('door_id', 'N/A')))

        # User info might be nested
        user_info = event_data.get('user_info', {})
        user_desc = user_info.get('name', event_data.get('user_description', event_data.get('person_id', 'N/A')))

        # Input value might contain the credential identifier for some notification types
        credential_identifier = event_data.get('input_value', event_data.get('credential_identifier', 'N/A'))

        # Format timestamp
        formatted_time = format_timestamp(timestamp_unix)

        output = (
            f"Door: {door_name}, User: {user_desc}, Credential ID: {credential_identifier}, Time: {formatted_time}"
        )
        print(output) # Print essential info to console always
        # logging.info(output) # Log only if verbose (handled by level setting in app.py)
    except KeyError as e:
        logging.error(f"Missing expected key in Access payload: {e}")
    except Exception as e:
        logging.error(f"Error processing Access event: {e}", exc_info=True)


# Main event handler/dispatcher called by app.py

def handle_event(payload):
    """
    Determines the type of webhook event and calls the appropriate handler.

    Args:
        payload (dict): The JSON payload received from the webhook.
    """
    # logging.debug(f"Handling event payload: {payload}") # Avoid logging full payload unless necessary

    # --- Determine Event Type ---
    webhook_type = payload.get('webhook_type') # Explicit type field from Verkada

    if webhook_type == 'lpr':
        logging.info(f"Dispatching LPR event...") # Shows only if verbose
        process_lpr_event(payload)
    elif webhook_type == 'notification':
        # Notifications often wrap other event types, check nested data
        notification_type = payload.get('data', {}).get('notification_type', '')
        logging.info(f"Dispatching Notification event (Type: {notification_type})...") # Shows only if verbose
        # Assuming 'notification' types related to access control should use process_access_event
        if 'door' in notification_type:
             process_access_event(payload)
        elif notification_type == 'license_plate_of_interest':
             # Log that we received it, but don't process further for Phase 1 unless requested
             logging.info(f"Received 'license_plate_of_interest' notification. No specific action defined for Phase 1.") # Shows only if verbose
             # Optionally, you could call process_lpr_event if the structure is similar enough
             # process_lpr_event(payload)
        else:
             logging.warning(f"Received unhandled notification type: {notification_type}") # Always shows
    elif webhook_type == 'access_event': # Handle direct access events if they exist
         logging.info(f"Dispatching Access event...") # Shows only if verbose
         process_access_event(payload)
    # Fallback check using keys if webhook_type is missing (less reliable)
    elif 'license_plate_number' in payload.get('data', {}):
        logging.info(f"Dispatching LPR event (detected by key)...") # Shows only if verbose
        process_lpr_event(payload)
    elif 'door_id' in payload.get('data', {}):
        logging.info(f"Dispatching Access event (detected by key)...") # Shows only if verbose
        process_access_event(payload)
    else:
        # Fallback if type is unknown or keys don't match
        logging.warning(f"Received unknown or unsupported event type. Webhook Type Field: '{webhook_type}'. Keys: {list(payload.keys())}") # Always shows

