# Project: Verkada API Monitor for Community

This project provides different implementations for interacting with the Verkada API and monitoring events:

1.  **Helix API Test Scripts (`src_helix`):** A collection of Python scripts and a shell runner for testing various Verkada API endpoints.
2.  **AWS Lambda Implementation (not yet tested):** A serverless approach using AWS Lambda and API Gateway for scalability and reduced management. Located in `src_aws/`.
3.  **Original Flask Implementation (tested):** A standalone Python Flask application suitable for local testing or environments where a persistent server is preferred. Located in `src_flask/`.

---

## Helix API Test Scripts (`src_helix/`)

**Goal:** Provide a set of command-line Python scripts and a menu-driven shell script to easily test specific Verkada API endpoints, fetch data, and generate JSON templates of the responses.

**Functionality:**
*   Fetch a short-lived API token using a provided API key.
*   Test various API endpoints (e.g., Access Users List, User Details, Access Events, Camera List, LPR Images, LPR Timestamps, LPOI).
*   Display the raw JSON response from successful API calls.
*   Generate and save JSON template files based on the structure of successful responses.
*   Provide a menu-driven shell script (`runtest.sh`) for interactive selection and execution of tests.
*   Include options for controlling logging verbosity.
*   Implement interactive selection menus for tests requiring specific parameters (like user or camera selection).

**Technology Stack:**
*   Python 3.x
*   `requests` (for making API calls)
*   `argparse` (for command-line arguments)
*   `logging` (for structured output and debugging)
*   `os`, `sys`, `json`, `time`, `datetime`, `traceback` (standard libraries)
*   Bash shell script (`runtest.sh`) for the interactive menu.

---

### Helix Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    # Replace <your-repo-url> with the actual repository URL
    cd Verkada # Assuming project root is Verkada
    ```

2.  **Create and activate a virtual environment:**
    *   It's recommended to create a separate environment for the Helix scripts:
        ```bash
        python3 -m venv venv_helix
        ```
    *   Activate it:
        ```bash
        # On macOS/Linux:
        source venv_helix/bin/activate
        # On Windows:
        # venv_helix\Scripts\activate
        ```
    *   Your terminal prompt should now be prefixed (e.g., `(venv_helix)`).

3.  **Install dependencies:**
    ```bash
    pip install -r src_helix/requirements.txt
    ```

4.  **Set API Key Environment Variable:**
    *   The scripts require your Verkada API key to be set as an environment variable named `API_KEY`.
    *   Obtain your API key from Verkada Command (**Admin** -> **API**).
    *   Set the environment variable in your terminal session *before* running the scripts:
        ```bash
        export API_KEY="your_verkada_api_key"
        ```
    *   **Security Note:** Be cautious with your API key. Avoid hardcoding it directly in scripts or committing it to version control. Using environment variables is a standard practice. For persistent environments, consider using a secrets manager.

---

### Helix Usage

The primary way to run the Helix tests is using the `runtest.sh` script, which provides an interactive menu.

1.  **Activate Virtual Environment:** Ensure your Helix virtual environment is activated (e.g., `source venv_helix/bin/activate`).
2.  **Set API Key:** Ensure the `API_KEY` environment variable is set in your current terminal session.
3.  **Run the Menu Script:**
    *   Navigate to the project's root directory (`Verkada`) in your terminal.
    *   Execute the script:
        ```bash
        ./src_helix/runtest.sh
        ```
    *   The script will display a menu of available tests.
    *   Enter the number corresponding to the test you want to run, or 'L' to change the log level, or '0' to exit.
    *   Some tests (like User Details or LPR Timestamps) will prompt you for additional input (e.g., selecting a user or camera/plate).

4.  **Direct Script Execution (Advanced):**
    *   You can also run individual Python scripts directly from the command line.
    *   Navigate to the project root.
    *   Use `python -m <module_path>` to run the script as a module.
    *   Use `--help` to see available arguments for each script.
    *   Example:
        ```bash
        python -m src_helix.test_token_api --log_level DEBUG
        python -m src_helix.test_user_details_api --user_index 5 --log_level INFO
        ```

5.  **Monitor Output and Logs:**
    *   API responses and script output will be printed to your terminal.
    *   Detailed debug logs for each script are saved in the `src_helix/` directory (e.g., `token_api_debug.log`, `users_list_api_debug.log`). Check these files for more information, especially if a test fails.
    *   JSON template files (e.g., `test_token_api.json`, `test_users_list_api.json`) are generated in the `src_helix/` directory upon successful API calls that return data.

---
---

## AWS Lambda Implementation (`src_aws/`)

**Goal:** Provide a scalable, serverless solution using AWS services to monitor events from a Verkada security system deployed in a neighborhood.

**Functionality:**
*   Receive real-time events via Verkada Webhooks triggered through AWS API Gateway.
*   Validate incoming webhooks using signature verification.
*   Parse event payloads (JSON).
*   Log essential event information (Plate/Credential, Door, User, Time) to AWS CloudWatch Logs.
*   Control logging verbosity via Lambda environment variables.

**Technology Stack:**
*   Python 3.x
*   AWS Lambda
*   AWS API Gateway (HTTP API or REST API)
*   AWS Systems Manager (SSM) Parameter Store (for webhook secret)
*   AWS CloudWatch Logs (for monitoring)
*   AWS IAM (for permissions)
*   Boto3 (AWS SDK for Python)

---

### AWS Setup and Deployment

Refer to `plan.md` (Steps 7-10) for detailed instructions. The general steps are:

1.  **Prerequisites:**
    *   AWS Account
    *   AWS CLI configured (optional, can use console)
    *   Python 3.x and `pip`

2.  **Store Secret:**
    *   Store your `VERKADA_WEBHOOK_SECRET` securely in AWS Systems Manager Parameter Store (as a `SecureString`). Note the parameter name (e.g., `/verkada/webhook/secret`).

3.  **Create IAM Role:**
    *   Create an IAM role for the Lambda function.
    *   Attach the `AWSLambdaBasicExecutionRole` managed policy (for CloudWatch Logs).
    *   Add an inline policy granting `ssm:GetParameter` permission specifically for the secret parameter created above.

4.  **Package the Code:**
    *   Create a deployment package (`.zip` file) containing the contents of `src_aws/` and the dependencies from `src_aws/requirements.txt`.
        ```bash
        # Example packaging steps:
        # Ensure you are in the project root directory
        mkdir package
        pip install -r src_aws/requirements.txt -t ./package
        # Copy Python files from src_aws into the package directory
        cp src_aws/__init__.py src_aws/config.py src_aws/handlers.py src_aws/lambda_function.py src_aws/security.py ./package/
        # Zip the contents of the package directory
        cd package
        zip -r ../lambda_deployment_package.zip .
        cd ..
        # Clean up temporary directory
        rm -rf package
        ```
    *   Alternatively, use AWS SAM or Serverless Framework for more robust packaging and deployment.

5.  **Create Lambda Function:**
    *   In the AWS Lambda console, create a new function.
    *   Choose the Python runtime (e.g., Python 3.9+).
    *   Upload the `lambda_deployment_package.zip`.
    *   Assign the created IAM role.
    *   Set the Handler to `lambda_function.lambda_handler`.
    *   Configure Environment Variables:
        *   `SECRET_PARAMETER_NAME`: The name of the SSM Parameter storing the secret (e.g., `/verkada/webhook/secret`).
        *   `LOG_LEVEL`: `INFO` (default) or `DEBUG` for more verbose logging.
    *   Adjust memory/timeout as needed (start with defaults).

6.  **Create API Gateway:**
    *   In the AWS API Gateway console, create an HTTP API (recommended for simplicity) or REST API.
    *   Configure a `POST` route (e.g., `/webhook`).
    *   Set the integration target to the created Lambda function (using Lambda proxy integration).
    *   Deploy the API stage (e.g., `prod`). Note the **Invoke URL**.

---

### AWS Usage

1.  **Configure Verkada Webhook:**
    *   In Verkada Command (**Admin** -> **Integrations** -> **Webhooks**), create or update a webhook.
    *   **URL:** Use the **Invoke URL** from the deployed API Gateway stage.
    *   **Secret:** Ensure the secret configured here matches the value stored in SSM Parameter Store.
    *   **Event Types:** Select desired events (e.g., `License Plate Read`, `Door Access`).
    *   Save the webhook.

2.  **Trigger Events:** Perform actions in Verkada that match the configured event types.

3.  **Monitor Output:**
    *   Go to the AWS CloudWatch console.
    *   Navigate to Log groups.
    *   Find the log group associated with your Lambda function (e.g., `/aws/lambda/<your-function-name>`).
    *   View the log streams to see the output logged by the `handlers.py` module.

---

### AWS Architecture and Design

The AWS implementation leverages serverless components for handling webhooks:

*   **API Gateway:** Acts as the public HTTPS endpoint, receiving POST requests from Verkada. It validates the request method and forwards the entire request payload (headers, body) to the Lambda function via proxy integration.
*   **AWS Lambda (`src_aws/lambda_function.py`):** The core compute service. The `lambda_handler` function serves as the entry point.
    *   It parses the incoming `event` object from API Gateway.
    *   Normalizes headers and decodes the body if necessary.
    *   Calls `security.validate_signature` for webhook validation.
    *   Parses the JSON payload.
    *   Dispatches the payload to `handlers.handle_event`.
    *   Returns the appropriate HTTP status code to API Gateway.
*   **Configuration (`src_aws/config.py`):** Uses `boto3` to fetch the `VERKADA_WEBHOOK_SECRET` from AWS SSM Parameter Store based on the `SECRET_PARAMETER_NAME` environment variable. Caches the secret in memory for the lifetime of the Lambda execution environment instance.
*   **Signature Validation (`src_aws/security.py`):** The `validate_signature` function is adapted to work with headers and body provided by the Lambda event, rather than a Flask request object. It retrieves the secret via `config.get_webhook_secret()`.
*   **Event Handling (`src_aws/handlers.py`):** The logic remains similar to the Flask version, but uses the standard `logging` module to output formatted event information, which is automatically captured by CloudWatch Logs.
*   **Logging:** Standard Python `logging` is configured in `lambda_function.py`, with the level controlled by the `LOG_LEVEL` environment variable. All logs are sent to CloudWatch.

---
---

## Original Flask Implementation (`src_flask/`)

**Goal:** Develop a Python application (using Flask) to monitor events from a Verkada security system deployed in a neighborhood, suitable for local execution or environments where a persistent server is managed.

**Functionality:**
*   Receive real-time events via Verkada Webhooks (primarily LPR and Access Control events).
*   Validate incoming webhooks using signature verification.
*   Parse event payloads (JSON).
*   Display essential event information (Plate/Credential, Door, User, Time) as formatted, fixed-width text messages to the console.
*   Provide a `--verbose` option for more detailed logging.

**Technology Stack:**
*   Python 3.x
*   Flask (for webhook receiver)
*   `python-dotenv` (for configuration management)
*   Standard libraries: `hmac`, `hashlib`, `time`, `datetime`, `logging`, `argparse`

---

### Flask Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    # Replace <your-repo-url> with the actual repository URL
    cd Verkada # Assuming project root is Verkada
    ```

2.  **Create and activate a virtual environment:**
    *   It's recommended to create a separate environment for the Flask app:
        ```bash
        python3 -m venv venv_flask
        ```
    *   Activate it:
        ```bash
        # On macOS/Linux:
        source venv_flask/bin/activate
        # On Windows:
        # venv_flask\Scripts\activate
        ```
    *   Your terminal prompt should now be prefixed (e.g., `(venv_flask)`).

3.  **Install dependencies:**
    ```bash
    pip install -r src_flask/requirements.txt
    ```

4.  **Create Configuration File (`.env`):**
    *   **Important:** For security, the `.env` file containing secrets is stored *outside* the project directory. The Flask app is configured (in `src_flask/config.py`) to look for it in `$HOME/.env`.
    *   Create a file named `.env` in your home directory (`~/.env` on Linux/macOS).
    *   Copy the contents from the example `.env` template below into your new `$HOME/.env` file.
    *   **Crucially:** Obtain the `VERKADA_WEBHOOK_SECRET` from Verkada Command (**Admin** -> **Integrations** -> **Webhooks** -> **Add Webhook** -> **Secret**) and paste it into your `$HOME/.env` file, replacing `"YOUR_VERKADA_WEBHOOK_SECRET"`.

    **.env Template (for `$HOME/.env`):**
    ```dotenv
    # Verkada Configuration
    VERKADA_WEBHOOK_SECRET="YOUR_VERKADA_WEBHOOK_SECRET"

    # Optional: Add Org ID if needed for future API calls
    # VERKADA_ORG_ID="YOUR_ORGANIZATION_ID_HERE"
    ```
    *   **Security Note:** Ensure the `$HOME/.env` file has appropriate permissions and is not accidentally committed anywhere.

---

### Flask Usage

This application runs as a web server that listens for incoming webhook POST requests from Verkada.

1.  **Activate Virtual Environment:** Ensure your Flask virtual environment is activated (e.g., `source venv_flask/bin/activate`).
2.  **Verify Configuration:** Make sure the `.env` file exists at `$HOME/.env` and contains the correct `VERKADA_WEBHOOK_SECRET`.
3.  **Run the Application:**
    *   Navigate to the project's root directory (`Verkada`) in your terminal.
    *   Execute the application using the `src_flask` module:
        ```bash
        # Standard output (minimal logging)
        python -m src_flask.app

        # Verbose output (includes INFO level logs for validation, dispatching etc.)
        python -m src_flask.app --verbose
        ```
    *   The server will start, typically listening on `http://127.0.0.1:5000/`. The webhook endpoint will be `/webhook`. Keep this terminal running.

4.  **Expose Local Server (for Testing):**
    *   Since Verkada needs a public URL, use `ngrok` (or a similar tool) in a separate terminal window while the application is running:
        ```bash
        ngrok http 5000
        ```
    *   Note the public `https` URL provided by `ngrok` (e.g., `https://<random-string>.ngrok-free.app`).

5.  **Configure Verkada Webhook:**
    *   In Verkada Command (**Admin** -> **Integrations** -> **Webhooks**), create a **New Webhook**.
    *   **URL:** Enter the `ngrok` `https` URL from the previous step, appending `/webhook` (e.g., `https://<random-string>.ngrok-free.app/webhook`).
    *   **Secret:** Paste the **exact** secret from your `$HOME/.env` file.
    *   **Event Types:** Select the events you want to monitor (e.g., `License Plate Read`, `Door Access`).
    *   Save the new webhook.
    *   **Note:** If using free `ngrok`, you must update the URL in Verkada Command each time you restart `ngrok`.

6.  **Trigger Events:** Perform actions in Verkada (e.g., LPR read, door access) that match the configured event types.

7.  **Observe Output:** Watch the terminal where `python -m src_flask.app` is running. You should see formatted output lines for each successfully received and validated event. If running with `--verbose`, you will see additional logging information.

---

### Flask Architecture and Design

The Flask application follows a simple, modular design:

*   **Web Server (Flask):** `src_flask/app.py` uses the Flask microframework.
*   **Webhook Endpoint (`/webhook`):** Defined in `src_flask/app.py`, listens for `POST` requests.
*   **Configuration (`.env`, `src_flask/config.py`):** Loads the secret from `$HOME/.env` using `python-dotenv`.
*   **Signature Validation (`src_flask/security.py`):** Implements Verkada's webhook security using the Flask `request` object.
*   **Event Handling (`src_flask/handlers.py`):** Parses payloads and prints formatted output to the console.
*   **Command-Line Interface (`argparse`):** `src_flask/app.py` handles the `--verbose` flag.
*   **Logging:** Standard `logging` module, level controlled by `--verbose`.

---
