import os
from dotenv import load_dotenv

# --- Specify the path to the .env file ---
# The .env file is stored outside the project repository for security.
# Update this path if the location changes.
dotenv_path = '/Users/markmorris/Documents/Verkada-code-base/.env'

# Load environment variables from the specified .env file path
load_dotenv(dotenv_path=dotenv_path)

# --- Verkada Configuration ---
# Retrieve the webhook secret required for validating incoming webhook requests.
# This MUST be set in your .env file located at the path specified above.
VERKADA_WEBHOOK_SECRET = os.getenv("VERKADA_WEBHOOK_SECRET")

if not VERKADA_WEBHOOK_SECRET:
    # In a real application, you might want to raise an error or log a critical warning.
    print(f"WARNING: VERKADA_WEBHOOK_SECRET is not set in the environment variables.")
    print(f"Attempted to load from: {dotenv_path}")
    # For now, we'll let it proceed, but validation will likely fail.

# --- Flask Configuration (Example) ---
# You can load other configuration variables similarly
# FLASK_ENV = os.getenv("FLASK_ENV", "production") # Default to production if not set
# FLASK_RUN_PORT = int(os.getenv("FLASK_RUN_PORT", 5000))
# FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST", "127.0.0.1")

# Add other configuration variables as needed for future phases
# VERKADA_API_KEY = os.getenv("VERKADA_API_KEY") # Example for Phase 2+
