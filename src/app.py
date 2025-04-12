import logging
from flask import Flask, request, abort

# Import configuration and handlers/security functions
from src import config
from src.security import validate_signature
from src.handlers import handle_event # Placeholder for event processing logic

# Basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def verkada_webhook():
    """
    Receives webhook events from Verkada.
    Validates the signature and passes the payload to the handler.
    """
    # Check if the secret is configured. Validation itself happens in validate_signature.
    if not config.VERKADA_WEBHOOK_SECRET:
        logging.error("Webhook secret is not configured. Aborting.")
        abort(500, description="Webhook secret not configured on server.")

    # 1. Validate the signature
    if not validate_signature(request):
        logging.warning("Webhook signature validation failed.")
        abort(401, description="Invalid webhook signature.") # Unauthorized
    else:
        logging.info("Webhook signature validated successfully.")

    # 2. Get the JSON payload
    try:
        data = request.get_json()
        if data is None:
            logging.warning("Received webhook with empty or non-JSON payload.")
            abort(400, description="Request body must be JSON.") # Bad Request
    except Exception as e:
        logging.error(f"Error parsing JSON payload: {e}")
        abort(400, description="Invalid JSON payload.") # Bad Request

    logging.info(f"Received valid webhook payload.") # Consider logging type if available: data.get('event_type')

    # 3. Pass the payload to the event handler
    try:
        handle_event(data)
    except Exception as e:
        # Log exceptions during handling but still acknowledge receipt to Verkada
        logging.error(f"Error handling webhook event: {e}", exc_info=True)
        # Depending on requirements, you might want to return a 500 here,
        # but often it's better to acknowledge the webhook (2xx) and handle errors internally.

    # 4. Return a success response
    # 204 No Content is appropriate as we don't need to send a body back.
    return '', 204

# Example: Add a simple root route for testing if the server is up
@app.route('/', methods=['GET'])
def index():
    return "Verkada Webhook Receiver is running.", 200

if __name__ == '__main__':
    # Note: Use a production WSGI server (like Gunicorn or uWSGI) for deployment
    logging.info("Starting Flask development server.")
    app.run(host='0.0.0.0', port=5000, debug=False) # Set debug=True for development debugging output
