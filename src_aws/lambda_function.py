import json
import logging
import os
import base64
from typing import Dict, Any

# Import local modules using relative imports
from . import config
from . import security
from . import handlers

# --- Logging Setup ---
# Configure logging level based on environment variable
log_level_name = os.environ.get('LOG_LEVEL', 'INFO').upper()
log_level = getattr(logging, log_level_name, logging.INFO)

# Remove any existing handlers to avoid duplicate logs in Lambda
# (Lambda adds its own handler)
root_logger = logging.getLogger()
if root_logger.handlers:
    for handler in root_logger.handlers:
        root_logger.removeHandler(handler)

logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info(f"Logging configured with level: {log_level_name}")

# --- Lambda Handler ---

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler function triggered by API Gateway (Proxy Integration).

    Args:
        event (Dict[str, Any]): The event dictionary from API Gateway.
        context (Any): The Lambda context object (provides runtime info like request ID).

    Returns:
        Dict[str, Any]: The response dictionary formatted for API Gateway.
    """
    # Log basic invocation info, including request ID from context if available
    request_id = getattr(context, 'aws_request_id', 'N/A')
    logger.info(f"Received request (ID: {request_id})")
    logger.debug(f"Received event (ID: {request_id}): {json.dumps(event)}") # Log full event only at DEBUG level

    # 1. Extract required information from the API Gateway event
    try:
        http_method = event.get('httpMethod')
        headers = event.get('headers', {})
        body = event.get('body', '')
        is_base64_encoded = event.get('isBase64Encoded', False)

        # Normalize header keys to lowercase for consistent access
        normalized_headers = {k.lower(): v for k, v in headers.items()} if headers else {}

    except Exception as e:
        logger.error(f"Error extracting basic event data (ID: {request_id}): {e}", exc_info=True)
        return {'statusCode': 500, 'body': json.dumps({'error': 'Internal Server Error: Could not parse event structure'})}

    # 2. Check HTTP Method
    if http_method != 'POST':
        logger.warning(f"Received non-POST request (ID: {request_id}): {http_method}")
        return {'statusCode': 405, 'body': json.dumps({'error': 'Method Not Allowed'})}

    # 3. Decode body if necessary
    try:
        if is_base64_encoded and body:
            logger.debug(f"Decoding base64 encoded body (ID: {request_id}).")
            raw_body_bytes = base64.b64decode(body)
        elif body:
            # If not base64 encoded, assume it's a UTF-8 string and encode to bytes
            logger.debug(f"Encoding non-base64 body to bytes (ID: {request_id}).")
            raw_body_bytes = body.encode('utf-8')
        else:
            logger.debug(f"Body is empty (ID: {request_id}).")
            raw_body_bytes = b''
        # Keep the decoded string version for JSON parsing later
        decoded_body_str = raw_body_bytes.decode('utf-8')
    except (base64.B64DecodeError, UnicodeDecodeError) as e:
        logger.error(f"Error decoding request body (ID: {request_id}): {e}")
        return {'statusCode': 400, 'body': json.dumps({'error': 'Bad Request: Invalid body encoding'})}
    except Exception as e:
        logger.error(f"Unexpected error during body decoding (ID: {request_id}): {e}", exc_info=True)
        return {'statusCode': 500, 'body': json.dumps({'error': 'Internal Server Error: Body processing failed'})}

    # 4. Validate Signature (Requires secret fetched within validate_signature)
    # Pass normalized headers and the raw byte body
    logger.info(f"Attempting signature validation (ID: {request_id})...")
    if not security.validate_signature(normalized_headers, raw_body_bytes):
        # Specific logging is done within validate_signature
        logger.warning(f"Webhook signature validation failed (ID: {request_id}).")
        return {'statusCode': 401, 'body': json.dumps({'error': 'Unauthorized: Invalid signature'})}
    else:
        logger.info(f"Webhook signature validated successfully (ID: {request_id}).")

    # 5. Parse JSON payload from the decoded string body
    if not decoded_body_str:
         logger.warning(f"Received webhook with empty payload after decoding (ID: {request_id}).")
         # Treat as bad request as we expect JSON.
         return {'statusCode': 400, 'body': json.dumps({'error': 'Bad Request: Empty payload'})}

    try:
        logger.debug(f"Attempting to parse JSON payload (ID: {request_id})...")
        payload_data = json.loads(decoded_body_str)
        if not isinstance(payload_data, dict):
             logger.warning(f"Parsed JSON is not a dictionary (ID: {request_id}): {type(payload_data)}")
             return {'statusCode': 400, 'body': json.dumps({'error': 'Bad Request: Payload must be a JSON object'})}
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON payload (ID: {request_id}): {e}")
        # Log snippet of body for debugging if needed (be careful with sensitive data)
        logger.debug(f"Failed JSON body snippet (ID: {request_id}): {decoded_body_str[:100]}")
        return {'statusCode': 400, 'body': json.dumps({'error': 'Bad Request: Invalid JSON payload'})}
    except Exception as e:
        logger.error(f"Unexpected error during JSON parsing (ID: {request_id}): {e}", exc_info=True)
        return {'statusCode': 500, 'body': json.dumps({'error': 'Internal Server Error: JSON parsing failed'})}

    webhook_type = payload_data.get('webhook_type', 'Unknown')
    logger.info(f"Received valid webhook payload (Type: {webhook_type}, ID: {request_id}).")

    # 6. Pass the payload to the event handler
    try:
        logger.info(f"Dispatching event to handler (Type: {webhook_type}, ID: {request_id})...")
        handlers.handle_event(payload_data)
        logger.info(f"Webhook event handled successfully (ID: {request_id}).")
    except Exception as e:
        # Log exceptions during handling but still acknowledge receipt to Verkada
        logger.error(f"Error handling webhook event (ID: {request_id}): {e}", exc_info=True)
        # Return 500 to indicate internal processing failure
        return {'statusCode': 500, 'body': json.dumps({'error': 'Internal Server Error: Failed to process event'})}

    # 7. Return a success response (204 No Content)
    logger.info(f"Returning successful response (204) for request ID: {request_id}")
    return {'statusCode': 204, 'body': ''}

# Example of how to test locally (requires setting environment variables like SECRET_PARAMETER_NAME)
# if __name__ == '__main__':
#     # Create a sample event object similar to what API Gateway sends
#     sample_event = {
#         "httpMethod": "POST",
#         "headers": {
#             "Content-Type": "application/json",
#             "Verkada-Signature": "t=1678886400|signature_hash_here" # Replace with actual test data
#             # Add other relevant headers
#         },
#         "body": json.dumps({
#             "webhook_type": "lpr",
#             "data": {
#                 "created": 1678886400,
#                 "license_plate_number": "TESTPLATE"
#             }
#             # Add other payload data
#         }),
#         "isBase64Encoded": False
#     }
#     # Set environment variables needed (e.g., SECRET_PARAMETER_NAME, LOG_LEVEL)
#     os.environ['SECRET_PARAMETER_NAME'] = 'your-ssm-parameter-name' # Replace
#     os.environ['LOG_LEVEL'] = 'DEBUG'
#
#     # Mock context object
#     class MockContext:
#         aws_request_id = 'local-test-request-id'
#
#     # Call the handler
#     response = lambda_handler(sample_event, MockContext())
#     print(f"Lambda handler response: {response}")

