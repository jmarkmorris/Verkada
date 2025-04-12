import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

# --- Verkada Configuration ---
# Retrieve the webhook secret required for validating incoming webhook requests.
# This MUST be set in your .env file.
VERKADA_WEBHOOK_SECRET = os.getenv("VERKADA_WEBHOOK_SECRET")

if not VERKADA_WEBHOOK_SECRET:
    # In a real application, you might want to raise an error or log a critical warning.
    print("WARNING: VERKADA_WEBHOOK_SECRET is not set in the environment variables.")
    # For now, we'll let it proceed, but validation will likely fail.

# --- Flask Configuration (Example) ---
# You can load other configuration variables similarly
# FLASK_ENV = os.getenv("FLASK_ENV", "production") # Default to production if not set
# FLASK_RUN_PORT = int(os.getenv("FLASK_RUN_PORT", 5000))
# FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST", "127.0.0.1")

# Add other configuration variables as needed for future phases
# VERKADA_API_KEY = os.getenv("VERKADA_API_KEY") # Example for Phase 2+
