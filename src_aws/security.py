import hmac
import hashlib
import time
import logging
from typing import Dict, Optional

# Import the function to get the secret from the configuration module
from .config import get_webhook_secret

# Configure logging
# Use standard Python logging; level will be configured in lambda_function.py
logger = logging.getLogger(__name__)

# Define the tolerance for timestamp validation (in seconds)
# Increased to 600 (10 min) to handle observed clock skew. Best practice is to fix system clock.
TIMESTAMP_TOLERANCE = 600

def validate_signature(headers: Dict[str, str], raw_body: bytes) -> bool:
    """
    Validates the Verkada webhook signature using headers and raw body
    provided by the AWS API Gateway event.

    Args:
        headers (Dict[str, str]): A dictionary of request headers (keys should be
                                   normalized to lowercase by the caller).
        raw_body (bytes): The raw byte string of the request body.

    Returns:
        True if the signature is valid, False otherwise.
    """
    # 1. Retrieve the webhook secret from configuration (e.g., SSM)
    webhook_secret = get_webhook_secret()
    if not webhook_secret:
        # Critical error already logged by get_webhook_secret()
        logger.error("Signature validation failed: Webhook secret could not be retrieved.")
        return False

    # 2. Retrieve the combined Verkada-Signature header (case-insensitive)
    # Caller (lambda_handler) is expected to provide lowercase header keys
    verkada_combined_signature = headers.get('verkada-signature')

    if not verkada_combined_signature:
        # Log keys received if the expected one is missing
        logger.error(f"Missing 'verkada-signature' header. Received header keys: {list(headers.keys())}")
        return False

    # 3. Split the header into timestamp and received signature hash
    try:
        timestamp_str, received_signature = verkada_combined_signature.split('|', 1)
    except ValueError:
        logger.error(f"Invalid Verkada-Signature format. Expected 'timestamp|signature', got: {verkada_combined_signature}")
        return False

    # 4. Check timestamp tolerance
    try:
        timestamp_int = int(timestamp_str)
        current_time = int(time.time())
        if abs(current_time - timestamp_int) > TIMESTAMP_TOLERANCE:
            logger.warning(f"Timestamp {timestamp_str} is outside the tolerance window ({TIMESTAMP_TOLERANCE}s). Current time: {current_time}")
            return False
    except ValueError:
        logger.error(f"Invalid timestamp format in Verkada-Signature: {timestamp_str}")
        return False

    # 5. Construct the message string to sign
    # Format: body + b"|" + timestamp_bytes
    timestamp_bytes = timestamp_str.encode('utf-8')
    # raw_body is already bytes, ensure it's not None
    message = (raw_body or b'') + b"|" + timestamp_bytes

    # 6. Calculate the expected signature
    try:
        secret_bytes = webhook_secret.encode('utf-8')
        calculated_signature = hmac.new(secret_bytes, message, hashlib.sha256).hexdigest()
    except Exception as e:
        logger.error(f"Error calculating HMAC signature: {e}", exc_info=True)
        return False

    # 7. Compare signatures using hmac.compare_digest for timing attack resistance
    try:
        is_valid = hmac.compare_digest(calculated_signature, received_signature)
    except TypeError as e:
        logger.error(f"Type error comparing signatures: {e}. Calculated type: {type(calculated_signature)}, Received type: {type(received_signature)}")
        is_valid = False
    except Exception as e:
        logger.error(f"Error comparing signatures: {e}", exc_info=True)
        is_valid = False

    if not is_valid:
        # Log detailed info only on failure for security/noise reduction
        logger.warning(f"Signature mismatch. Calculated: {calculated_signature}, Received: {received_signature}")
        # Avoid logging raw body or full message in production unless debugging requires it.
        # logger.debug(f"Failed validation for message: {message!r}") # Example debug log

    # No need to log success here, the calling function (lambda_handler) can log it.
    return is_valid
