# Project: Verkada API Monitor for Gated Community

**Goal:** Develop a Python application to monitor events from a Verkada security system deployed in a gated neighborhood. The system includes cameras at entry gates (capturing LPR and access code usage) and other locations.

**Initial Functionality (Phase 1):**
*   Receive real-time events via Verkada Webhooks (primarily LPR and Access Control events).
*   Validate incoming webhooks using signature verification.
*   Parse event payloads (JSON).
*   Display essential event information (Plate/Credential, Door, User, Time) as formatted, fixed-width text messages to the console.
*   Provide a `--verbose` option for more detailed logging.

**Technology Stack (Initial):**
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
    *   Create a file named `.env` in the following location: `/Users/markmorris/Documents/Verkada-code-base/.env` (Adjust path if necessary).
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
2.  **Verify Configuration:** Make sure the `.env` file exists at the configured path (`/Users/markmorris/Documents/Verkada-code-base/.env`) and contains the correct `VERKADA_WEBHOOK_SECRET`.
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
    *   In Verkada Command (**Admin** -> **Integrations** -> **Webhooks**), create a **New Webhook**. (Editing existing webhooks, especially the secret, may not be possible or reliable).
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

## Development Challenges & Solutions

Several challenges were encountered during the development and testing of Phase 1:

1.  **Signature Validation Discrepancies:**
    *   **Initial Issue:** The application initially failed validation, logging errors about missing `X-Verkada-Signature` and `X-Verkada-Timestamp` headers.
    *   **Debugging:** Inspecting the actual incoming request headers using the `ngrok` web interface (`http://127.0.0.1:4040`) revealed that Verkada was sending a single combined header named `Verkada-Signature` with the format `timestamp|signature_hash`.
    *   **Documentation Mismatch:** The specific documentation page ([https://apidocs.verkada.com/reference/securing-webhooks](https://apidocs.verkada.com/reference/securing-webhooks)) provided sample code showing a different message construction (`body|timestamp`) than initially assumed (`timestamp:body`).
    *   **Solution:** The `src/security.py` module was updated to:
        *   Look for the correct `Verkada-Signature` header.
        *   Split the header value by `|` to extract the timestamp and hash.
        *   Construct the message for HMAC calculation using the documented `raw_body + b"|" + timestamp_bytes` format.
    *   **Secret Mismatch:** After fixing the header/message format, "Signature mismatch" errors occurred, indicating the secret stored locally in `.env` did not exactly match the secret configured in the active Verkada webhook. This required careful verification and recreation of the webhook in Verkada Command.

2.  **Timestamp Tolerance / Clock Skew:**
    *   **Issue:** Validation failed with warnings indicating the received timestamp was outside the allowed tolerance window (initially 300 seconds / 5 minutes).
    *   **Cause:** The system clock on the local development machine was out of sync with Verkada's servers by more than the tolerance window.
    *   **Solution:** The primary fix is to ensure the local system clock is synchronized using NTP (e.g., via OS settings). As a temporary workaround during development, the `TIMESTAMP_TOLERANCE` constant in `src/security.py` was increased to 600 seconds (10 minutes).

3.  **Python Module Imports:**
    *   **Issue:** Running the application directly via `python src/app.py` resulted in `ModuleNotFoundError` or `ImportError: attempted relative import with no known parent package` because Python didn't recognize `src` as a package in that context.
    *   **Solution:** The application must be run as a module from the project root directory (`Verkada`) using `python -m src.app`. This allows Python to correctly resolve the relative imports (e.g., `from . import config`) within the `src` package. Running instructions were updated accordingly.

4.  **Virtual Environment Corruption:**
    *   **Issue:** The `pip` command within the activated virtual environment became corrupted, leading to `ModuleNotFoundError: No module named 'pip._internal.build_env'` when trying to install dependencies. Attempts to repair with `ensurepip` failed.
    *   **Solution:** The corrupted virtual environment directory was deleted, and a new one was created and activated. Dependencies were then successfully reinstalled using `pip install -r requirements.txt`.

5.  **`ngrok` Temporary URLs:**
    *   **Issue:** Using the free tier of `ngrok` for local testing generates a new random public URL each time `ngrok` is started.
    *   **Impact:** This requires manually updating the webhook URL in Verkada Command every time `ngrok` is restarted, which can be inconvenient during development.
    *   **Solution/Mitigation:** For short testing sessions, leave `ngrok` running. For more frequent development, consider a paid `ngrok` plan with static subdomains or deploy the application to a server with a permanent URL.

---

**Future Enhancements (Phase 2+):**
*   Persistent storage of events (e.g., database).
*   More robust event correlation (linking LPR and subsequent Access events).
*   Fetching and displaying video thumbnails or links via Verkada API calls.
*   Web-based or GUI for event viewing and filtering.
*   Polling API endpoints as a supplement to webhooks for certain data.
*   More sophisticated error handling and alerting.
*   Unit and integration tests.
