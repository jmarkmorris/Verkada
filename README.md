# Project: Verkada API Monitor for Gated Community

**Goal:** Develop a Python application to monitor events from a Verkada security system deployed in a gated neighborhood. The system includes cameras at entry gates (capturing LPR and access code usage) and other locations.

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

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    # Replace <your-repo-url> with the actual repository URL
    cd Verkada
    ```

2.  **Create and activate a virtual environment:**
    *   It's recommended to create the environment within the project directory:
        ```bash
        python3 -m venv venv
        ```
    *   Activate it:
        ```bash
        # On macOS/Linux:
        source venv/bin/activate
        # On Windows:
        # venv\Scripts\activate
        ```
    *   Your terminal prompt should now be prefixed (e.g., `(venv)`).

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create Configuration File (`.env`):**
    *   **Important:** For security, the `.env` file containing secrets is stored *outside* the project directory.
    *   Create a file named `.env` in the following location: `$HOME/.env` (Adjust path if necessary).
    *   Copy the contents from the example `.env` template below into your new `.env` file.
    *   **Crucially:** You need to obtain the `VERKADA_WEBHOOK_SECRET`.
        *   Log in to your Verkada Command account.
        *   Navigate to **Admin** -> **Integrations** -> **Webhooks**.
        *   Click **Add Webhook**.
        *   Configure the webhook (URL details below in Usage/Testing).
        *   Under the **Secret** section, generate or copy the secret value. **Ensure you copy the exact value.**
        *   Paste this value into your `.env` file (located at the path specified above), replacing `"YOUR_VERKADA_WEBHOOK_SECRET"`.

    **.env Template:**
    ```dotenv
    # Verkada Configuration
    # Obtain this secret from the Verkada Command platform when setting up the webhook.
    # Go to Admin -> Integrations -> Webhooks -> Add Webhook -> Secret
    VERKADA_WEBHOOK_SECRET="YOUR_VERKADA_WEBHOOK_SECRET"

    # Optional: Add Org ID if needed for future API calls
    # VERKADA_ORG_ID="YOUR_ORGANIZATION_ID_HERE"

    # Flask Configuration (Optional, Flask defaults are often fine initially)
    # FLASK_APP=src.app
    # FLASK_ENV=development
    # FLASK_RUN_PORT=5000
    # FLASK_RUN_HOST=0.0.0.0
    ```
    *   **Security Note:** Ensure the directory containing the `.env` file has appropriate permissions set and is not accidentally committed to any version control system. The project's `.gitignore` file prevents committing `.env` files located within the project directory itself.

---

## Usage

This application runs as a web server that listens for incoming webhook POST requests from Verkada.

1.  **Activate Virtual Environment:** Ensure your virtual environment is activated (e.g., `source venv/bin/activate`).
2.  **Verify Configuration:** Make sure the `.env` file exists at the configured path (`$HOME/.env`) and contains the correct `VERKADA_WEBHOOK_SECRET`.
3.  **Run the Application:**
    *   Navigate to the project's root directory (`Verkada`) in your terminal.
    *   Execute the application as a module:
        ```bash
        # Standard output (minimal logging)
        python -m src.app

        # Verbose output (includes INFO level logs for validation, dispatching etc.)
        python -m src.app --verbose
        ```
    *   The server will start, typically listening on `http://0.0.0.0:5000/`. The webhook endpoint will be `/webhook`. Keep this terminal running.

4.  **Expose Local Server (for Testing):**
    *   Since Verkada needs a public URL, use `ngrok` (or a similar tool) in a separate terminal window while the application is running:
        ```bash
        ngrok http 5000
        ```
    *   Note the public `https` URL provided by `ngrok` (e.g., `https://<random-string>.ngrok-free.app`).

5.  **Configure Verkada Webhook:**
    *   In Verkada Command (**Admin** -> **Integrations** -> **Webhooks**), create a **New Webhook**. (Editing existing webhooks may not be possible).
    *   **URL:** Enter the `ngrok` `https` URL from the previous step, appending `/webhook` (e.g., `https://<random-string>.ngrok-free.app/webhook`).
    *   **Secret:** Paste the **exact** secret from your `.env` file.
    *   **Event Types:** Select the events you want to monitor (e.g., `License Plate Read`, `Door Access`).
    *   Save the new webhook.
    *   **Note:** If using free `ngrok`, you must update the URL in Verkada Command each time you restart `ngrok`, as the public URL will change.

6.  **Trigger Events:** Perform actions in Verkada (e.g., LPR read, door access) that match the configured event types.

7.  **Observe Output:** Watch the terminal where `python -m src.app` is running. You should see formatted output lines for each successfully received and validated event. If running with `--verbose`, you will see additional logging information.

---

## Architecture and Design

The application follows a simple, modular design suitable for receiving and processing webhooks.

*   **Web Server (Flask):** `src/app.py` uses the Flask microframework to create a lightweight web server. Flask was chosen for its simplicity in handling a single primary endpoint.
*   **Webhook Endpoint (`/webhook`):** Defined in `src/app.py`, this route listens for incoming `POST` requests from Verkada.
*   **Configuration (`.env`, `src/config.py`):** Sensitive configuration (like the webhook secret) is stored in an external `.env` file (path specified in `src/config.py`). The `python-dotenv` library is used within `src/config.py` to load these variables into the environment securely, keeping secrets out of the source code.
*   **Signature Validation (`src/security.py`):** The `validate_signature` function implements Verkada's webhook security protocol. It extracts the `Verkada-Signature` header, parses the timestamp and hash, checks the timestamp tolerance, reconstructs the message payload (`body|timestamp`), calculates the expected HMAC-SHA256 hash using the shared secret, and performs a constant-time comparison against the received hash.
*   **Event Handling (`src/handlers.py`):**
    *   **Dispatcher (`handle_event`):** Receives the validated JSON payload from `app.py`. It inspects the `webhook_type` and `notification_type` fields to determine the event category and calls the appropriate processing function.
    *   **Processors (`process_lpr_event`, `process_access_event`):** These functions are responsible for extracting the relevant data points from the specific event payload structure (handling nested dictionaries like `data`, `door_info`, `user_info`). They format the extracted data into the desired fixed-width string using f-string formatting and print it to the console.
    *   **Timestamp Formatting:** A helper function converts the Unix epoch timestamps provided by Verkada into human-readable date/time strings adjusted for the local timezone.
*   **Command-Line Interface (`argparse`):** `src/app.py` uses `argparse` to handle command-line arguments, specifically the `--verbose` flag to control the logging verbosity.
*   **Logging:** The standard `logging` module is used throughout the application. The logging level is set based on the `--verbose` flag (defaulting to `WARNING`, changing to `INFO` if `--verbose` is used), allowing for detailed debugging information when needed while keeping the default output clean.

---
