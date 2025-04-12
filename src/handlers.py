import logging

# Placeholder functions for processing specific event types

def process_lpr_event(payload):
    """
    Processes a License Plate Recognition event payload.
    Extracts relevant information and prints it.
    """
    try:
        # Extract relevant fields - adjust keys based on actual Verkada payload structure
        timestamp = payload.get('event_timestamp', 'N/A')
        camera_name = payload.get('camera_name', payload.get('camera_id', 'N/A')) # Prefer name, fallback to ID
        plate_number = payload.get('license_plate_number', 'N/A')
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
    Processes an Access Control event payload.
    Extracts relevant information and prints it.
    """
    try:
        # Extract relevant fields - adjust keys based on actual Verkada payload structure
        timestamp = payload.get('event_timestamp', 'N/A')
        event_type = payload.get('event_type', 'N/A') # e.g., "Door Accessed", "Access Denied"
        door_name = payload.get('door_name', payload.get('door_id', 'N/A')) # Prefer name, fallback to ID
        user_desc = payload.get('user_description', payload.get('person_id', 'N/A')) # Prefer description
        credential_type = payload.get('credential_type', 'N/A') # e.g., "Card", "PIN", "BLE"
        credential_identifier = payload.get('credential_identifier', 'N/A') # e.g., card number, code used
        org_id = payload.get('org_id', 'N/A')

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
    logging.debug(f"Handling event payload: {payload}") # Log full payload only if needed (can be verbose)

    # --- Determine Event Type ---
    # NOTE: The exact field indicating the webhook type needs verification.
    # It might be 'webhook_type', 'event_category', or determined by specific keys.
    webhook_type = payload.get('webhook_type', 'Unknown') # Placeholder guess

    if 'license_plate_number' in payload:
        logging.info(f"Dispatching LPR event...")
        process_lpr_event(payload)
    elif 'door_id' in payload or 'door_name' in payload:
        logging.info(f"Dispatching Access event...")
        process_access_event(payload)
    # Add elif conditions for other event types (Sensor, Alarm, etc.) if needed in the future
    # elif 'sensor_id' in payload:
    #     logging.info("Dispatching Sensor event...")
    #     # process_sensor_event(payload) # Implement this function if needed
    else:
        # Fallback if specific keys aren't found or webhook_type is generic
        logging.warning(f"Received unknown or unsupported event type. Webhook Type Field: '{webhook_type}'. Keys: {list(payload.keys())}")

