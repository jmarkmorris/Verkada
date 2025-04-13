# Plan: Migrate Verkada Webhook Receiver to AWS Lambda

**Goal:** Create an AWS Lambda function fronted by API Gateway to handle Verkada webhooks, as an alternative implementation to the original Flask version. The original Flask implementation will be kept in `src_flask/` for reference.

**Original Architecture (`src_flask/`):**
*   Flask web server (`src_flask/app.py`) listens on `/webhook`.
*   `ngrok` exposes the local Flask server to the internet.
*   Signature validation (`src_flask/security.py`) uses Flask's `request` object.
*   Event processing (`src_flask/handlers.py`) parses JSON and prints to console.
*   Configuration (`src_flask/config.py`) loads secrets from a local `.env` file.
*   Logging is configured via `logging` and controlled by a `--verbose` CLI flag.
*   Dependencies managed in `src_flask/requirements.txt` (or a root-level file).

**Target Architecture (`src_aws/`):**
*   **API Gateway:** Provides a public HTTPS endpoint (e.g., `https://<api-id>.execute-api.<region>.amazonaws.com/prod/webhook`).
*   **AWS Lambda:** Executes the core Python logic (located in `src_aws/`) triggered by API Gateway.
*   **AWS Systems Manager Parameter Store (or Secrets Manager):** Securely stores `VERKADA_WEBHOOK_SECRET`.
*   **CloudWatch Logs:** Captures logs (stdout/stderr) from the Lambda function.
*   **IAM Role:** Grants Lambda permissions to access CloudWatch Logs and Parameter Store/Secrets Manager.
*   Dependencies managed in `src_aws/requirements.txt`.

**Step-by-Step Implementation Plan:**

1.  **Create `src_aws/` Directory Structure:**
    *   Create the `src_aws/` directory.
    *   Copy `handlers.py`, `security.py`, `config.py`, and `__init__.py` from `src_flask/` into `src_aws/`. These will be modified in subsequent steps.
    *   Create an empty `src_aws/requirements.txt` file.

2.  **Refactor Configuration (`src_aws/config.py`):**
    *   Modify `src_aws/config.py`.
    *   Remove dependency on `python-dotenv` and local `.env` file loading.
    *   Add `boto3` to `src_aws/requirements.txt`.
    *   Implement logic within `src_aws/config.py` to fetch `VERKADA_WEBHOOK_SECRET` from AWS Systems Manager Parameter Store (or Secrets Manager) using `boto3`. The parameter name should be configurable (e.g., via a Lambda environment variable `SECRET_PARAMETER_NAME`).
    *   Handle potential errors during secret retrieval (e.g., missing parameter, insufficient permissions).

3.  **Adapt Signature Validation (`src_aws/security.py`):**
    *   Modify `src_aws/security.py`.
    *   Modify the `validate_signature` function signature to accept `headers` (dict) and `raw_body` (bytes or string) as arguments instead of the Flask `request` object.
    *   Update the function logic to extract the `Verkada-Signature` header from the passed `headers` dictionary (handle potential case differences, e.g., normalize keys to lowercase).
    *   Use the passed `raw_body` directly for HMAC calculation.
    *   Keep the core timestamp and HMAC logic the same.

4.  **Create Lambda Handler (`src_aws/lambda_function.py`):**
    *   Create a new file `src_aws/lambda_function.py`.
    *   Define the main handler function (e.g., `lambda_handler(event, context)`).
    *   Import necessary modules from `.config`, `.security`, and `.handlers`.
    *   **Configure Logging:** Set up standard Python `logging` at the beginning of the file or handler. Control the logging level (e.g., `INFO` vs. `WARNING`) using a Lambda environment variable (e.g., `LOG_LEVEL`).
    *   **Parse Input:** Inside `lambda_handler`, extract headers (specifically `Verkada-Signature`), raw request body, and HTTP method from the API Gateway `event` object (assuming Lambda Proxy integration).
        *   Headers: `event['headers']` (normalize keys to lowercase).
        *   Body: `event['body']` (check if base64 encoded via `event['isBase64Encoded']` and decode if necessary).
        *   Method: `event['httpMethod']`.
    *   **Method Check:** Ensure the request method is `POST`. Return `{'statusCode': 405, 'body': 'Method Not Allowed'}` if not.
    *   **Fetch Secret:** Call the function in `src_aws.config` to get the webhook secret from SSM/Secrets Manager. Handle errors appropriately (return 500).
    *   **Signature Validation:** Call the refactored `validate_signature` function from `src_aws.security`, passing the extracted headers, raw body, and the fetched secret. Return `{'statusCode': 401, 'body': 'Unauthorized'}` if validation fails.
    *   **JSON Parsing:** Parse the decoded request body into a Python dictionary. Use a try-except block. Return `{'statusCode': 400, 'body': 'Bad Request: Invalid JSON'}` if parsing fails.
    *   **Event Dispatching:** Call `handle_event` from `src_aws.handlers`, passing the parsed JSON payload.
    *   **Return Response:** Return `{'statusCode': 204, 'body': ''}` on success. Handle internal errors during event dispatching by returning a 500 status code with an appropriate message.

5.  **Adapt Event Handling (`src_aws/handlers.py`):**
    *   Modify `src_aws/handlers.py`.
    *   Ensure all output intended for monitoring uses standard Python `logging` (e.g., `logging.info(...)`, `logging.warning(...)`) instead of `print()`, as `logging` provides more control and integrates better with CloudWatch Logs.
    *   The core logic of `process_lpr_event` and `process_access_event` (extracting data, formatting) should remain largely the same, but replace `print` with `logging`.
    *   The `handle_event` dispatcher logic remains the same.

6.  **Update Dependencies (`src_aws/requirements.txt`):**
    *   Add `boto3` (required for interacting with AWS services like SSM/Secrets Manager). Note: `boto3` is usually included in the standard AWS Lambda Python runtime, but explicitly listing it is good practice, especially if using layers or custom runtimes.
    *   Ensure any other non-standard library dependencies used by `handlers.py`, `security.py`, or `config.py` are listed.
    *   Remove dependencies specific to the Flask version (like `Flask`, `python-dotenv`) if they were copied over.

7.  **Packaging for Deployment:**
    *   Create a deployment package (ZIP file).
    *   The ZIP file should contain the contents of the `src_aws/` directory at the root level (e.g., `lambda_function.py`, `handlers.py`, etc.).
    *   Install dependencies from `src_aws/requirements.txt` into the *root* of the packaging directory before zipping: `pip install -r src_aws/requirements.txt -t ./package_temp_dir`. Then zip the contents of `package_temp_dir`.
    *   Alternatively, use AWS SAM (`template.yaml`, `sam build`, `sam deploy`) or the Serverless Framework (`serverless.yml`) to manage dependencies, packaging, and deployment.

8.  **AWS Infrastructure Setup (Manual or IaC):**
    *   **IAM Role:** Create an IAM execution role for the Lambda function with:
        *   `AWSLambdaBasicExecutionRole` policy (for CloudWatch Logs).
        *   Permissions to read the specific parameter from SSM Parameter Store (e.g., `ssm:GetParameter` on the specific parameter ARN) or secret from Secrets Manager (`secretsmanager:GetSecretValue`).
    *   **SSM Parameter/Secret:** Store the `VERKADA_WEBHOOK_SECRET` securely in Parameter Store (Standard or Advanced tier, ensure encryption is considered) or Secrets Manager. Note the ARN or name.
    *   **Lambda Function:**
        *   Create the Lambda function using the packaged code (ZIP upload or via SAM/Serverless).
        *   Select an appropriate Python runtime (e.g., Python 3.9+).
        *   Assign the created IAM role.
        *   Configure environment variables:
            *   `SECRET_PARAMETER_NAME`: The name or ARN of the SSM Parameter/Secret.
            *   `LOG_LEVEL`: e.g., `INFO` or `WARNING`.
        *   Set the handler to `lambda_function.lambda_handler` (assuming the file is `lambda_function.py` and the function is `lambda_handler`).
        *   Configure memory and timeout settings appropriately (start with defaults, adjust based on testing).
    *   **API Gateway:**
        *   Create an API Gateway (HTTP API recommended for simplicity and cost, or REST API if more features are needed).
        *   Define a route: `POST /webhook`.
        *   Configure an integration to trigger the created Lambda function (use Lambda Proxy integration).
        *   Deploy the API Gateway stage (e.g., `prod`). Note the public Invoke URL.

9.  **Update Verkada Webhook Configuration:**
    *   In Verkada Command, update the webhook URL to point to the deployed API Gateway Invoke URL (e.g., `https://<api-id>.execute-api.<region>.amazonaws.com/prod/webhook`).
    *   Ensure the secret configured in Verkada matches the value stored in SSM Parameter Store/Secrets Manager.

10. **Testing and Monitoring:**
    *   Trigger events in Verkada.
    *   Monitor API Gateway logs and metrics in CloudWatch.
    *   Monitor Lambda function logs in CloudWatch Logs for output from the `logging` statements and any errors.
    *   Verify events are processed and logged as expected.

