import os
import logging
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError

# Configure logging
# Use standard Python logging; level will be configured in lambda_function.py
logger = logging.getLogger(__name__)

# Global variable to cache the secret after the first successful fetch
_cached_secret = None

def get_webhook_secret() -> str | None:
    """
    Retrieves the Verkada webhook secret from AWS Systems Manager Parameter Store.

    The name of the parameter is read from the 'SECRET_PARAMETER_NAME' environment variable.
    The secret is cached in memory after the first successful retrieval to optimize
    subsequent invocations within the same Lambda execution environment.

    Returns:
        The webhook secret string if successful, None otherwise. Logs errors.
    """
    global _cached_secret
    if _cached_secret:
        logger.debug("Returning cached webhook secret.")
        return _cached_secret

    parameter_name = os.environ.get('SECRET_PARAMETER_NAME')
    if not parameter_name:
        # Use CRITICAL level as this is a fatal configuration error for the function
        logger.critical("Environment variable 'SECRET_PARAMETER_NAME' is not set.")
        return None

    logger.info(f"Attempting to retrieve secret from SSM Parameter Store: {parameter_name}")

    try:
        # Use the default session (picks up credentials from environment, EC2 instance profile, etc.)
        # In Lambda, this will use the execution role's credentials.
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
        logger.critical(f"AWS credentials not found or incomplete when accessing SSM: {e}")
        return None
    except ClientError as e:
        error_code = e.response.get('Error', {}).get('Code')
        if error_code == 'ParameterNotFound':
            logger.critical(f"SSM Parameter '{parameter_name}' not found.")
        elif error_code == 'AccessDeniedException':
             logger.critical(f"Access denied when trying to retrieve SSM Parameter '{parameter_name}'. Check Lambda IAM role permissions.")
        else:
            # Log the specific Boto3 ClientError
            logger.critical(f"Failed to retrieve secret from SSM Parameter Store ({error_code}): {e}")
        return None
    except Exception as e:
        # Catch any other unexpected errors during SSM interaction
        logger.critical(f"An unexpected error occurred while retrieving the secret from SSM: {e}", exc_info=True)
        return None

# --- Deprecated Flask/dotenv Configuration ---
# The original code using python-dotenv is removed as it's not needed for the AWS Lambda implementation.
# Keeping it commented out is unnecessary clutter for the final Lambda code.
