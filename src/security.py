
import hmac
import hashlib
import time
import logging

# Import the secret from the configuration module
from src.config import VERKADA_WEBHOOK_SECRET

# Define the tolerance for timestamp validation (in seconds)
TIMESTAMP_TOLERANCE = 300  # 5 minutes

def validate_signature(request) -> bool:
    """
    Validates the Verkada webhook signature.

    Args:
        request: The Flask request object.

    Returns:
        True if the signature is valid, False otherwise.
    """
    if not VERKADA_WEBHOOK_SECRET:
        logging.critical("Webhook secret is not configured. Cannot validate signature.")
        return False

    # 1. Retrieve headers
    verkada_signature = request.headers.get('X-Verkada-Signature')
    verkada_timestamp = request.headers.get('X-Verkada-Timestamp')

    if not verkada_signature:
        logging.error("Missing X-Verkada-Signature header.")
        return False
    if not verkada_timestamp:
        logging.error("Missing X-Verkada-Timestamp header.")
        return False

    # 2. Check timestamp tolerance
    try:
        timestamp_int = int(verkada_timestamp)
        current_time = int(time.time())
        if abs(current_time - timestamp_int) > TIMESTAMP_TOLERANCE:
            logging.warning(f"Timestamp {verkada_timestamp} is outside the tolerance window ({TIMESTAMP_TOLERANCE}s). Current time: {current_time}")
            return False
    except ValueError:
        logging.error(f"Invalid timestamp format: {verkada_timestamp}")
        return False

    # 3. Get raw request body
    raw_body = request.get_data() # Returns bytes

    # 4. Construct the message string to sign
    # Verkada format: "timestamp:body"
    timestamp_bytes = verkada_timestamp.encode('utf-8')
    message = timestamp_bytes + b":" + raw_body

    # 5. Calculate the expected signature
    try:
        secret_bytes = VERKADA_WEBHOOK_SECRET.encode('utf-8')
        calculated_signature = hmac.new(secret_bytes, message, hashlib.sha256).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating HMAC signature: {e}")
        return False

    # 6. Compare signatures using hmac.compare_digest for timing attack resistance
    try:
        is_valid = hmac.compare_digest(calculated_signature, verkada_signature)
    except Exception as e:
        # Handle potential errors during comparison (e.g., type mismatches if something went wrong)
        logging.error(f"Error comparing signatures: {e}")
        is_valid = False

    if not is_valid:
        logging.warning(f"Signature mismatch. Calculated: {calculated_signature}, Received: {verkada_signature}")
    # No need to log success here, app.py already logs it if this returns True

    return is_valid
