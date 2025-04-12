import logging

# Placeholder functions for processing specific event types

def process_lpr_event(payload):
    """
    Processes a License Plate Recognition event payload.
    Extracts relevant information and prints it.
    """
    try:
        # Extract relevant fields - adjust keys based on actual Verkada payload structure
        # The timestamp seems to be in the 'data' sub-dictionary for LPR
        event_data = payload.get('data', {})
        timestamp = event_data.get('created', payload.get('created_at', 'N/A')) # Prefer 'created' in data, fallback to top-level
        camera_name = event_data.get('camera_name', event_data.get('camera_id', 'N/A')) # Prefer name, fallback to ID
        plate_number = event_data.get('license_plate_number', 'N/A')
        org_id = payload.get('org_id', 'N/A') # Example of accessing other potential fields

        output = (
            f"[LPR Event] Timestamp: {timestamp}, "
            f"Camera: {camera_name}, "
            f"Plate: {plate_number}, "
            f"OrgID: {org_id}"
        )
        print(output) # Print to console as per Phase 1 requirement
        logging.info(output)
    except KeyError as e:
        logging.error(f"Missing expected key in LPR payload: {e}")
    except Exception as e:
        logging.error(f"Error processing LPR event: {e}", exc_info=True)


def process_access_event(payload):
    """
    Processes an Access Control event payload (potentially wrapped in a 'notification').
    Extracts relevant information and prints it.
    """
    try:
        # Data might be nested under 'data' if it's a 'notification' type
        event_data = payload.get('data', payload) # Use top-level payload if 'data' key doesn't exist

        timestamp = event_data.get('created', payload.get('created_at', 'N/A')) # Prefer 'created' in data, fallback to top-level
        # Determine event type - might be 'notification_type' or 'event_type'
        event_type = event_data.get('notification_type', event_data.get('event_type', 'N/A'))

        # Door info might be nested further
        door_info = event_data.get('door_info', {})
        door_name = door_info.get('name', event_data.get('door_name', event_data.get('door_id', 'N/A')))

        # User info might be nested
        user_info = event_data.get('user_info', {})
        user_desc = user_info.get('name', event_data.get('user_description', event_data.get('person_id', 'N/A')))

        # Credential info might be at the event_data level
        credential_type = event_data.get('credential_type', 'N/A') # e.g., "Card", "PIN", "BLE"
        # Input value might contain the credential identifier for some notification types
        credential_identifier = event_data.get('input_value', event_data.get('credential_identifier', 'N/A'))

        org_id = payload.get('org_id', 'N/A') # Org ID is likely at the top level

        output = (
            f"[Access Event] Timestamp: {timestamp}, "
            f"Type: {event_type}, "
            f"Door: {door_name}, "
            f"User: {user_desc}, "
            f"Credential: {credential_type} ({credential_identifier}), "
            f"OrgID: {org_id}"
        )
        print(output) # Print to console as per Phase 1 requirement
        logging.info(output)
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
        logging.info(f"Dispatching LPR event...")
        process_lpr_event(payload)
    elif webhook_type == 'notification':
        # Notifications often wrap other event types, check nested data
        notification_type = payload.get('data', {}).get('notification_type', '')
        logging.info(f"Dispatching Notification event (Type: {notification_type})...")
        # Assuming 'notification' types related to access control should use process_access_event
        # This might need refinement based on different notification_types
        if 'door' in notification_type:
             process_access_event(payload)
        else:
             logging.warning(f"Received unhandled notification type: {notification_type}")
    elif webhook_type == 'access_event': # Handle direct access events if they exist
         logging.info(f"Dispatching Access event...")
         process_access_event(payload)
    # Fallback check using keys if webhook_type is missing (less reliable)
    elif 'license_plate_number' in payload.get('data', {}):
        logging.info(f"Dispatching LPR event (detected by key)...")
        process_lpr_event(payload)
    elif 'door_id' in payload.get('data', {}):
        logging.info(f"Dispatching Access event (detected by key)...")
        process_access_event(payload)
    else:
        # Fallback if type is unknown or keys don't match
        logging.warning(f"Received unknown or unsupported event type. Webhook Type Field: '{webhook_type}'. Keys: {list(payload.keys())}")

