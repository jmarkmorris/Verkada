# Plan: Migrate Verkada Webhook Receiver to AWS Lambda

**Goal:** Replace the Flask + ngrok setup with an AWS Lambda function fronted by API Gateway to handle Verkada webhooks.

**Current Architecture:**
*   Flask web server (`src/app.py`) listens on `/webhook`.
*   `ngrok` exposes the local Flask server to the internet.
*   Signature validation (`src/security.py`) uses Flask's `request` object.
*   Event processing (`src/handlers.py`) parses JSON and prints to console.
*   Configuration (`src/config.py`) loads secrets from a local `.env` file.
*   Logging is configured via `logging` and controlled by a `--verbose` CLI flag.

**Target Architecture:**
*   **API Gateway:** Provides a public HTTPS endpoint (e.g., `https://<api-id>.execute-api.<region>.amazonaws.com/prod/webhook`).
*   **AWS Lambda:** Executes the core Python logic triggered by API Gateway.
*   **AWS Systems Manager Parameter Store (or Secrets Manager):** Securely stores `VERKADA_WEBHOOK_SECRET`.
*   **CloudWatch Logs:** Captures logs (stdout/stderr) from the Lambda function.
*   **IAM Role:** Grants Lambda permissions to access CloudWatch Logs and Parameter Store/Secrets Manager.

**Step-by-Step Implementation Plan:**

1.  **Refactor Configuration (`src/config.py`):**
    *   Remove dependency on `python-dotenv` and local `.env` file loading.
    *   Add `boto3` to dependencies (`requirements.txt`).
    *   Implement logic to fetch `VERKADA_WEBHOOK_SECRET` from AWS Systems Manager Parameter Store (or Secrets Manager) using `boto3`. The parameter name should be configurable (e.g., via a Lambda environment variable).
    *   Handle potential errors during secret retrieval (e.g., missing parameter, insufficient permissions).

2.  **Adapt Signature Validation (`src/security.py`):**
    *   Modify `validate_signature` function signature to accept `headers` (dict) and `raw_body` (bytes or string) as arguments instead of the Flask `request` object.
    *   Update the function logic to extract the `Verkada-Signature` header from the passed `headers` dictionary.
    *   Use the passed `raw_body` directly for HMAC calculation.
    *   Keep the core timestamp and HMAC logic the same.

3.  **Create Lambda Handler (`src/lambda_function.py` or similar):**
    *   Create a new file (e.g., `src/lambda_function.py`) to contain the Lambda entry point.
    *   Define the main handler function (e.g., `lambda_handler(event, context)`).
    *   **Parse Input:** Extract headers (specifically `Verkada-Signature`), raw request body, and HTTP method from the API Gateway `event` object. Note: The structure of `event` depends on the API Gateway integration type (Proxy vs. Non-Proxy). Assume Lambda Proxy integration for simplicity.
        *   Headers: `event['headers']` (case might vary, normalize keys to lowercase).
        *   Body: `event['body']` (might be base64 encoded depending on API Gateway config, decode if necessary).
        *   Method: `event['httpMethod']`.
    *   **Method Check:** Ensure the request method is `POST`. Return 405 Method Not Allowed if not.
    *   **Signature Validation:** Call the refactored `validate_signature` function from `src.security`, passing the extracted headers and raw body. Return 401 Unauthorized if validation fails.
    *   **JSON Parsing:** Parse the request body (`event['body']`) into a Python dictionary. Return 400 Bad Request if parsing fails.
    *   **Event Dispatching:** Call `handle_event` from `src.handlers`, passing the parsed JSON payload.
    *   **Return Response:** Return a dictionary formatted according to API Gateway Lambda Proxy integration requirements (e.g., `{'statusCode': 204, 'body': ''}`). Handle internal errors by returning a 500 status code.

4.  **Adapt Event Handling (`src/handlers.py`):**
    *   The core logic of `process_lpr_event` and `process_access_event` (extracting data, formatting) should remain largely the same.
    *   Ensure all output uses `print()` or standard `logging`, as this will be captured by CloudWatch Logs.
    *   The `handle_event` dispatcher logic remains the same.

5.  **Update Logging:**
    *   Remove the `argparse` logic and `--verbose` flag from `src/app.py` (it will be removed/replaced).
    *   Configure standard Python `logging` at the beginning of `lambda_handler`.
    *   Control the logging level (e.g., `INFO` vs. `WARNING`) using a Lambda environment variable (e.g., `LOG_LEVEL`). Set the root logger level based on this variable.
    *   Ensure logs include relevant information for debugging in CloudWatch.

6.  **Remove Flask Application (`src/app.py`):**
    *   Delete or significantly refactor `src/app.py` as Flask is no longer needed. The core logic moves to `src/lambda_function.py`.

7.  **Update Dependencies (`requirements.txt`):**
    *   Remove `Flask`.
    *   Add `boto3` (if not already present in the target Lambda runtime environment, it's usually included).
    *   Keep other necessary dependencies (`python-dotenv` can be removed).

8.  **Packaging for Deployment:**
    *   Create a deployment package (ZIP file) containing:
        *   `src/` directory (with `lambda_function.py`, `handlers.py`, `security.py`, `config.py`, `__init__.py`).
        *   Any dependencies listed in `requirements.txt` (installed in the package root). Use `pip install -r requirements.txt -t .` to install dependencies locally for packaging.
    *   Alternatively, use AWS SAM or Serverless Framework which handle packaging.

9.  **AWS Infrastructure Setup (Manual or IaC):**
    *   **IAM Role:** Create an IAM execution role for the Lambda function with:
        *   `AWSLambdaBasicExecutionRole` policy (for CloudWatch Logs).
        *   Permissions to read the specific parameter from SSM Parameter Store (e.g., `ssm:GetParameter`) or secret from Secrets Manager.
    *   **SSM Parameter/Secret:** Store the `VERKADA_WEBHOOK_SECRET` securely in Parameter Store (Standard or Advanced tier) or Secrets Manager.
    *   **Lambda Function:**
        *   Create the Lambda function using the packaged code (ZIP upload).
        *   Select an appropriate Python runtime (e.g., Python 3.9+).
        *   Assign the created IAM role.
        *   Configure environment variables (e.g., `SECRET_PARAMETER_NAME`, `LOG_LEVEL`).
        *   Set the handler to `src.lambda_function.lambda_handler` (or adjusted path/name).
        *   Configure memory and timeout settings appropriately.
    *   **API Gateway:**
        *   Create an API Gateway (HTTP API recommended for simplicity and cost).
        *   Define a route (e.g., `POST /webhook`).
        *   Configure an integration to trigger the created Lambda function (Lambda Proxy integration).
        *   Deploy the API Gateway stage. Note the public Invoke URL.

10. **Update Verkada Webhook Configuration:**
    *   In Verkada Command, update the webhook URL to point to the deployed API Gateway Invoke URL (e.g., `https://<api-id>.execute-api.<region>.amazonaws.com/prod/webhook`).
    *   Ensure the secret configured in Verkada matches the value stored in SSM Parameter Store/Secrets Manager.

11. **Testing and Monitoring:**
    *   Trigger events in Verkada.
    *   Monitor API Gateway logs and metrics.
    *   Monitor Lambda function logs in CloudWatch Logs for output and errors.
    *   Verify events are processed and logged as expected.

