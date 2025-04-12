import hmac
import hashlib
import time
import logging

# Import the secret from the configuration module using relative import
from .config import VERKADA_WEBHOOK_SECRET

# Define the tolerance for timestamp validation (in seconds)
TIMESTAMP_TOLERANCE = 300  # 5 minutes

def validate_signature(request) -> bool:
    """
    Validates the Verkada webhook signature based on the combined
    'Verkada-Signature: timestamp|signature_hash' header format.

    Args:
        request: The Flask request object.

    Returns:
        True if the signature is valid, False otherwise.
    """
    if not VERKADA_WEBHOOK_SECRET:
        logging.critical("Webhook secret is not configured. Cannot validate signature.")
        return False

    # 1. Retrieve the combined Verkada-Signature header
    verkada_combined_signature = request.headers.get('Verkada-Signature')

    if not verkada_combined_signature:
        # Log the actual headers received for debugging if the expected one is missing
        logging.error(f"Missing Verkada-Signature header. Received headers: {dict(request.headers)}")
        return False

    # 2. Split the header into timestamp and received signature hash
    try:
        timestamp_str, received_signature = verkada_combined_signature.split('|', 1)
    except ValueError:
        logging.error(f"Invalid Verkada-Signature format. Expected 'timestamp|signature', got: {verkada_combined_signature}")
        return False

    # 3. Check timestamp tolerance
    try:
        timestamp_int = int(timestamp_str)
        current_time = int(time.time())
        if abs(current_time - timestamp_int) > TIMESTAMP_TOLERANCE:
            logging.warning(f"Timestamp {timestamp_str} is outside the tolerance window ({TIMESTAMP_TOLERANCE}s). Current time: {current_time}")
            return False
    except ValueError:
        logging.error(f"Invalid timestamp format in Verkada-Signature: {timestamp_str}")
        return False

    # 4. Get raw request body
    raw_body = request.get_data() # Returns bytes

    # 5. Construct the message string to sign
    # Verkada format seems to be: "timestamp:body" based on general practice,
    # using the timestamp string from the header.
    timestamp_bytes = timestamp_str.encode('utf-8')
    message = timestamp_bytes + b":" + raw_body

    # --- DEBUGGING: Log components just before hashing ---
    # Log partial secret to confirm it's loaded without exposing the whole thing
    secret_preview = f"{VERKADA_WEBHOOK_SECRET[:5]}...{VERKADA_WEBHOOK_SECRET[-5:]}" if len(VERKADA_WEBHOOK_SECRET) > 10 else VERKADA_WEBHOOK_SECRET
    logging.debug(f"Secret loaded (preview): {secret_preview}")
    # Log the exact message bytes being signed
    logging.debug(f"Message bytes for HMAC: {message}")
    # --- END DEBUGGING ---

    # 6. Calculate the expected signature
    try:
        secret_bytes = VERKADA_WEBHOOK_SECRET.encode('utf-8')
        calculated_signature = hmac.new(secret_bytes, message, hashlib.sha256).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating HMAC signature: {e}")
        return False

    # 7. Compare signatures using hmac.compare_digest for timing attack resistance
    try:
        is_valid = hmac.compare_digest(calculated_signature, received_signature)
    except Exception as e:
        # Handle potential errors during comparison (e.g., type mismatches if something went wrong)
        logging.error(f"Error comparing signatures: {e}")
        is_valid = False

    if not is_valid:
        logging.warning(f"Signature mismatch. Calculated: {calculated_signature}, Received: {received_signature}")
    # No need to log success here, app.py already logs it if this returns True

    return is_valid
