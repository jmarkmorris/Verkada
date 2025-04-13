import hmac
import hashlib
import time
import logging

# Import the secret from the configuration module using relative import
from .config import VERKADA_WEBHOOK_SECRET

# Define the tolerance for timestamp validation (in seconds)
# Documentation sample uses 60, but 300 (5 min) is generally safer for clock skew
# Increased to 600 (10 min) to handle observed clock skew. Best practice is to fix system clock.
TIMESTAMP_TOLERANCE = 600

def validate_signature(request) -> bool:
    """
    Validates the Verkada webhook signature based on the combined
    'Verkada-Signature: timestamp|signature_hash' header format and
    documentation specifying 'body|timestamp' for hashing.

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
        # Using tolerance defined above (e.g., 600 seconds)
        if abs(current_time - timestamp_int) > TIMESTAMP_TOLERANCE:
            logging.warning(f"Timestamp {timestamp_str} is outside the tolerance window ({TIMESTAMP_TOLERANCE}s). Current time: {current_time}")
            # Note: Sample code uses 60s, which might be too strict.
            # if time.time() - timestamp_int > 60: # Direct check from sample code
            #     logging.warning(f"Timestamp {timestamp_str} is older than 60 seconds.")
            #     return False
            return False # Return false if outside our defined tolerance
    except ValueError:
        logging.error(f"Invalid timestamp format in Verkada-Signature: {timestamp_str}")
        return False

    # 4. Get raw request body
    raw_body = request.get_data() # Returns bytes

    # 5. Construct the message string to sign - CORRECTED based on documentation sample
    # Format: body + b"|" + timestamp_bytes
    timestamp_bytes = timestamp_str.encode('utf-8')
    # Ensure raw_body is bytes (it should be from get_data())
    message = (raw_body or b'') + b"|" + timestamp_bytes

    # 6. Calculate the expected signature
    try:
        secret_bytes = VERKADA_WEBHOOK_SECRET.encode('utf-8')
        calculated_signature = hmac.new(secret_bytes, message, hashlib.sha256).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating HMAC signature: {e}")
        return False

    # 7. Compare signatures using hmac.compare_digest for timing attack resistance
    try:
        # Ensure comparison happens with encoded values if necessary, though hexdigest should be str
        is_valid = hmac.compare_digest(calculated_signature, received_signature)
    except TypeError as e:
        # Example: If one is bytes and other is str
        logging.error(f"Type error comparing signatures: {e}. Calculated type: {type(calculated_signature)}, Received type: {type(received_signature)}")
        is_valid = False
    except Exception as e:
        # Handle potential errors during comparison
        logging.error(f"Error comparing signatures: {e}")
        is_valid = False

    if not is_valid:
        logging.warning(f"Signature mismatch. Calculated: {calculated_signature}, Received: {received_signature}")
    # No need to log success here, app.py already logs it if this returns True

    return is_valid
