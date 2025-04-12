# Phase 1 Implementation Plan: Verkada API Monitor

This plan outlines the steps to implement Phase 1 functionality as described in `README.md`.

**Phase 1 Goal:** Connect to Verkada API, receive and validate webhook events (LPR, Access Control), parse payloads, and display relevant event metadata to the console.

**Technology Stack:**
*   Python 3.x
*   Flask (Chosen for simplicity for a single webhook endpoint, FastAPI is also suitable)
*   `requests` (Potentially for future API calls, not strictly needed for webhook *receiving* in Phase 1)
*   `python-dotenv` (For configuration)

---

## Detailed Steps:

1.  **Project Setup:**
    *   [x] Create a `requirements.txt` file.
    *   [x] Add initial dependencies to `requirements.txt`:
        ```
        Flask>=2.0
        python-dotenv>=0.19
        requests>=2.25 # Include for potential future use or helper scripts
        ```
    *   [x] Create basic project directory structure:
        ```
        .
        ├── .gitignore
        ├── LICENSE
        ├── README.md
        ├── plan.md
        ├── requirements.txt
        ├── src/
        │   ├── __init__.py
        │   ├── app.py         # Flask application
        │   ├── config.py      # Configuration loading
        │   ├── handlers.py    # Event processing logic
        │   └── security.py    # Webhook validation logic
        └── venv/            # Virtual environment
        ```
    *   [x] Ensure `.env` is added to `.gitignore`.

2.  **Configuration Management (`.env` and `src/config.py`):**
    *   [x] Create the `.env` file. (Note: Moved to `/Users/markmorris/Documents/Verkada-code-base/.env` for security).
    *   [x] Define necessary environment variables in `.env`:
        ```dotenv
        # Verkada Configuration
        VERKADA_WEBHOOK_SECRET="YOUR_VERKADA_WEBHOOK_SECRET" # Obtain from Verkada Command when setting up the webhook
        VERKADA_ORG_ID="YOUR_ORGANIZATION_ID_HERE" # Optional for Phase 1, added by user

        # Flask Configuration (Optional, Flask defaults are often fine initially)
        FLASK_APP=src.app
        FLASK_ENV=development # Or production
        # FLASK_RUN_PORT=5000
        # FLASK_RUN_HOST=0.0.0.0
        ```
    *   [x] Create `src/config.py` to load these variables using `python-dotenv` and `os.getenv`. (Note: Updated `load_dotenv` call to use specific path).
        ```python
        # src/config.py
        import os
        from dotenv import load_dotenv

        dotenv_path = '/Users/markmorris/Documents/Verkada-code-base/.env'
        load_dotenv(dotenv_path=dotenv_path) # Load variables from specific .env file path

        VERKADA_WEBHOOK_SECRET = os.getenv("VERKADA_WEBHOOK_SECRET")
        VERKADA_ORG_ID = os.getenv("VERKADA_ORG_ID") # Loaded but not used in Phase 1 code yet
        # Add other config variables as needed
        ```
    *   [x] **Important:** Add instructions to `README.md` on how to obtain the `VERKADA_WEBHOOK_SECRET` from the Verkada Command platform during webhook setup and where to store the `.env` file.

3.  **Webhook Receiver Implementation (`src/app.py`):**
    *   [x] Import `Flask`, `request`, `abort` from `flask`.
    *   [x] Import validation function from `src.security`.
    *   [x] Import event handling functions from `src.handlers`.
    *   [x] Import configuration from `src.config`.
    *   [x] Initialize Flask app: `app = Flask(__name__)`.
    *   [x] Define a route (e.g., `/webhook`) that accepts POST requests.
    *   [x] Inside the route:
        *   [x] Call the webhook signature validation function. If validation fails, `abort(401)` (Unauthorized) or `abort(400)` (Bad Request).
        *   [x] Get the JSON payload: `data = request.get_json()`. Handle potential JSON decoding errors.
        *   [x] Pass the payload to an event dispatcher function in `src/handlers.py`.
        *   [x] Return an appropriate HTTP response (e.g., `200 OK` or `204 No Content`) to acknowledge receipt.
    *   [x] Add `if __name__ == '__main__':` block to run the Flask development server.

4.  **Webhook Signature Validation (`src/security.py`):**
    *   **Prerequisites (Manual Steps):**
        *   [x] Ensure you have obtained your `VERKADA_WEBHOOK_SECRET` from Verkada Command.
        *   [x] Ensure the secret is correctly placed in the external `.env` file (`/Users/markmorris/Documents/Verkada-code-base/.env`) as `VERKADA_WEBHOOK_SECRET="YOUR_SECRET_HERE"`. This step is crucial for validation to work.
    *   [x] Import `hmac`, `hashlib`, `time`. (Note: These are standard Python libraries, no `pip install` needed).
    *   [x] Import `VERKADA_WEBHOOK_SECRET` from `src.config`. (Note: We import from `config` to keep configuration loading separate from the security logic).
    *   [x] Create a function `validate_signature(request)`:
        *   [x] Retrieve the `X-Verkada-Signature` header from the `request.headers`.
        *   [x] Retrieve the `X-Verkada-Timestamp` header.
        *   [x] Handle cases where headers are missing (return `False`).
        *   [x] Check if the timestamp is within an acceptable tolerance (e.g., 5 minutes) to prevent replay attacks. `abs(time.time() - int(timestamp)) > 300`. Return `False` if outside tolerance.
        *   [x] Get the raw request body: `request.get_data()`.
        *   [x] Construct the message string to sign: `timestamp_bytes + b":" + raw_body`. (Ensure timestamp is bytes).
        *   [x] Calculate the HMAC-SHA256 signature using `VERKADA_WEBHOOK_SECRET.encode('utf-8')` as the key and the message string.
        *   [x] Compare the calculated signature (hex digest) with the received `X-Verkada-Signature` header using `hmac.compare_digest` (important for timing attack resistance).
        *   [x] Return `True` if valid, `False` otherwise.

5.  **Event Payload Parsing and Handling (`src/handlers.py`):**
    *   [x] Create a main dispatch function `handle_event(payload)`:
        *   [x] Check the payload structure or a specific field (e.g., `event_type`, if present in Verkada's payload) to determine the event type (LPR, Access Control, etc.). Refer to Verkada Webhook Models documentation. (Used key presence for now).
        *   [x] Call specific processing functions based on the type (e.g., `process_lpr_event(payload)`, `process_access_event(payload)`).
        *   [x] Include basic logging for received event types.
    *   [x] Create `process_lpr_event(payload)`:
        *   [x] Extract relevant fields: `timestamp`, `camera_name` (or `camera_id`), `license_plate_number`. Access nested fields as needed based on the [LPR Webhook Object](/reference/lpr) structure.
        *   [x] Format the extracted data into a string.
        *   [x] Print the formatted string to the console.
    *   [x] Create `process_access_event(payload)`:
        *   [x] Extract relevant fields: `timestamp`, `event_type` (e.g., "Door Accessed", "Access Denied"), `door_name` (or `door_id`), `user_description` (or `user_id`, `credential_type`, `credential_identifier` like code used or card number). Refer to [Access Events Webhooks](/reference/access-events-webhooks).
        *   [x] Format the extracted data into a string.
        *   [x] Print the formatted string to the console.
    *   [x] Add handling for unknown or unsupported event types (e.g., log a warning).

6.  **Error Handling and Logging:**
    *   [x] Implement `try...except` blocks in `app.py` for JSON decoding errors. (Added in Step 3)
    *   [x] Implement `try...except` blocks in `handlers.py` for potential `KeyError` when accessing payload fields. Log errors appropriately. (Added basic blocks in Step 5)
    *   [x] Use Python's built-in `logging` module for basic logging (e.g., received webhook, validation success/failure, event processing start/end, errors). Configure basic logging in `app.py`. (Added basic config in Step 3)

7.  **Testing (Manual):**
    *   [ ] **Run the Flask application:**
        *   Open your terminal.
        *   Navigate to the project's root directory (`verkada-api-monitor`).
        *   Activate the Python virtual environment:
            *   macOS/Linux: `source venv/bin/activate`
            *   Windows: `venv\Scripts\activate`
        *   Ensure your `.env` file exists at `/Users/markmorris/Documents/Verkada-code-base/.env` and contains the correct `VERKADA_WEBHOOK_SECRET`.
        *   Run the application: `python src/app.py`
        *   Observe the output. You should see a log message like `INFO: Starting Flask development server.` and `* Running on http://0.0.0.0:5000/`. Keep this terminal window open.
    *   [ ] **Configure a webhook in the Verkada Command platform pointing to the application's public URL (use `ngrok` or similar for local development):**
        *   **Start ngrok:** Open a *second* terminal window. Navigate to where you downloaded ngrok (or ensure it's in your system PATH). Run `ngrok http 5000`.
        *   **Copy ngrok URL:** ngrok will display forwarding URLs. Copy the `https` URL (e.g., `https://<random-string>.ngrok.io`).
        *   **Log in to Verkada Command:** Access your Verkada dashboard via a web browser.
        *   **Navigate to Webhooks:** Go to **Admin** -> **Integrations** -> **Webhooks**.
        *   **Add/Edit Webhook:** Click **Add Webhook** or edit an existing one.
        *   **Set URL:** Paste the `https` ngrok URL you copied, and append `/webhook` to the end. Example: `https://<random-string>.ngrok.io/webhook`.
        *   **Set Secret:** Ensure the **Secret** field contains the *exact same* secret string as the `VERKADA_WEBHOOK_SECRET` value in your `.env` file.
        *   **Select Event Types:** Choose the events you want to receive. For Phase 1, ensure **License Plate Read** (under Camera) and **Door Access** (under Access Control) events are selected. You might want to select specific cameras/doors if applicable.
        *   **Save:** Save the webhook configuration in Verkada Command.
    *   [ ] **Trigger LPR and Access Control events in the Verkada system:**
        *   Cause a vehicle with a visible license plate to pass by an LPR-enabled camera linked to the webhook.
        *   Use a valid (or invalid) credential (card, PIN, etc.) at an access-controlled door linked to the webhook.
    *   [ ] **Verify that the application receives the webhooks, validates them, and prints the correctly formatted information to the console:**
        *   Watch the terminal window where `python src/app.py` is running.
        *   You should see log messages indicating signature validation success and event dispatching.
        *   You should see the formatted `[LPR Event]` or `[Access Event]` messages printed to the console.
        *   Check the ngrok terminal window (`ngrok http 5000`) to see the incoming POST requests from Verkada (e.g., `POST /webhook 204 No Content`).
    *   [ ] **Test with invalid signatures (if possible to simulate) or old timestamps to ensure validation fails correctly:**
        *   (Difficult to simulate perfectly without modifying Verkada's sending).
        *   One way to test timestamp failure: Temporarily change `TIMESTAMP_TOLERANCE` in `src/security.py` to `1` (1 second), restart the app, and trigger an event. It's likely the request will arrive outside the 1-second window and fail validation. Remember to change it back to `300`.
        *   One way to test signature failure: Temporarily change a character in the `VERKADA_WEBHOOK_SECRET` in your `.env` file, restart the app (`python src/app.py`), and trigger an event. The signature validation should fail, and you should see a `401 Unauthorized` response in the ngrok terminal and corresponding error logs in the app terminal. Remember to change the secret back.

8.  **Documentation (`README.md`):**
    *   [x] Update `README.md` with:
        *   [x] Detailed setup instructions (virtual env, install requirements).
        *   [x] Instructions on setting up the `.env` file and obtaining the `VERKADA_WEBHOOK_SECRET`.
        *   [x] How to run the application (`python src/app.py`).
        *   [x] Explanation of the console output format.
        *   [x] Instructions on using `ngrok` or similar for local testing.

---
**Future Considerations (Beyond Phase 1):**
*   Asynchronous processing (if webhook volume is high).
*   More robust error handling and alerting.
*   Data validation for payload fields.
*   Unit and integration tests.
*   Persistent storage (Phase 2).
*   Using the Verkada API Key for active polling or fetching additional details (Phase 2+).
