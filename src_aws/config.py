import os
import logging
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError

# Configure logging
logger = logging.getLogger(__name__)

# Global variable to cache the secret after the first successful fetch
_cached_secret = None

def get_webhook_secret() -> str | None:
    """
    Retrieves the Verkada webhook secret from AWS Systems Manager Parameter Store.

    The name of the parameter is read from the 'SECRET_PARAMETER_NAME' environment variable.
    The secret is cached in memory after the first successful retrieval.

    Returns:
        The webhook secret string if successful, None otherwise. Logs errors.
    """
    global _cached_secret
    if _cached_secret:
        logger.debug("Returning cached webhook secret.")
        return _cached_secret

    parameter_name = os.environ.get('SECRET_PARAMETER_NAME')
    if not parameter_name:
        logger.critical("Environment variable 'SECRET_PARAMETER_NAME' is not set.")
        return None

    logger.info(f"Attempting to retrieve secret from SSM Parameter Store: {parameter_name}")

    try:
        # Use the default session (picks up credentials from environment, EC2 instance profile, etc.)
        ssm_client = boto3.client('ssm')
        response = ssm_client.get_parameter(
            Name=parameter_name,
            WithDecryption=True  # Required for SecureString parameters
        )
        secret_value = response['Parameter']['Value']
        _cached_secret = secret_value # Cache the secret
        logger.info("Successfully retrieved webhook secret from SSM.")
        return secret_value

    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.critical(f"AWS credentials not found or incomplete: {e}")
        return None
    except ClientError as e:
        error_code = e.response.get('Error', {}).get('Code')
        if error_code == 'ParameterNotFound':
            logger.critical(f"SSM Parameter '{parameter_name}' not found.")
        elif error_code == 'AccessDeniedException':
             logger.critical(f"Access denied when trying to retrieve SSM Parameter '{parameter_name}'. Check IAM permissions.")
        else:
            logger.critical(f"Failed to retrieve secret from SSM Parameter Store: {e}")
        return None
    except Exception as e:
        # Catch any other unexpected errors
        logger.critical(f"An unexpected error occurred while retrieving the secret: {e}", exc_info=True)
        return None

# --- Deprecated Flask/dotenv Configuration ---
# The following code related to .env files is no longer used for the AWS Lambda implementation.
# It's kept here commented out for reference during transition if needed, but should be removed later.
#
# from dotenv import load_dotenv
#
# # --- Specify the path to the .env file ---
# # The .env file is stored outside the project repository for security.
# # Update this path if the location changes.
# dotenv_path = os.path.join(os.path.expanduser("~"), ".env")
#
# # Load environment variables from the specified .env file path
# load_dotenv(dotenv_path=dotenv_path)
#
# # --- Verkada Configuration ---
# # Retrieve the webhook secret required for validating incoming webhook requests.
# # This MUST be set in your .env file located at the path specified above.
# VERKADA_WEBHOOK_SECRET_OLD = os.getenv("VERKADA_WEBHOOK_SECRET") # Renamed to avoid conflict
#
# if not VERKADA_WEBHOOK_SECRET_OLD:
#     # In a real application, you might want to raise an error or log a critical warning.
#     print(f"WARNING: VERKADA_WEBHOOK_SECRET is not set in the environment variables.")
#     print(f"Attempted to load from: {dotenv_path}")
#     # For now, we'll let it proceed, but validation will likely fail.
#
# # --- Flask Configuration (Example) ---
# # You can load other configuration variables similarly
# # FLASK_ENV = os.getenv("FLASK_ENV", "production") # Default to production if not set
# # FLASK_RUN_PORT = int(os.getenv("FLASK_RUN_PORT", 5000))
# # FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
#
# # Add other configuration variables as needed for future phases
# # VERKADA_API_KEY = os.getenv("VERKADA_API_KEY") # Example for Phase 2+

