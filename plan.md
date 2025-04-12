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
        ├── .env             # Configuration (add to .gitignore)
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
    *   [ ] Import `hmac`, `hashlib`, `time`.
    *   [ ] Import `VERKADA_WEBHOOK_SECRET` from `src.config`.
    *   [ ] Create a function `validate_signature(request)`:
        *   [ ] Retrieve the `X-Verkada-Signature` header from the `request.headers`.
        *   [ ] Retrieve the `X-Verkada-Timestamp` header.
        *   [ ] Check if the timestamp is within an acceptable tolerance (e.g., 5 minutes) to prevent replay attacks. `abs(time.time() - int(timestamp)) > 300`.
        *   [ ] Get the raw request body: `request.get_data()`.
        *   [ ] Construct the message string to sign: `timestamp + b":" + raw_body`.
        *   [ ] Calculate the HMAC-SHA256 signature using `VERKADA_WEBHOOK_SECRET.encode('utf-8')` as the key and the message string.
        *   [ ] Compare the calculated signature (hex digest) with the received `X-Verkada-Signature` header using `hmac.compare_digest`.
        *   [ ] Return `True` if valid, `False` otherwise.
    *   [ ] Handle cases where headers are missing.

5.  **Event Payload Parsing and Handling (`src/handlers.py`):**
    *   [ ] Create a main dispatch function `handle_event(payload)`:
        *   [ ] Check the payload structure or a specific field (e.g., `event_type`, if present in Verkada's payload) to determine the event type (LPR, Access Control, etc.). Refer to Verkada Webhook Models documentation.
        *   [ ] Call specific processing functions based on the type (e.g., `process_lpr_event(payload)`, `process_access_event(payload)`).
        *   [ ] Include basic logging for received event types.
    *   [ ] Create `process_lpr_event(payload)`:
        *   [ ] Extract relevant fields: `timestamp`, `camera_name` (or `camera_id`), `license_plate_number`. Access nested fields as needed based on the [LPR Webhook Object](/reference/lpr) structure.
        *   [ ] Format the extracted data into a string.
        *   [ ] Print the formatted string to the console.
    *   [ ] Create `process_access_event(payload)`:
        *   [ ] Extract relevant fields: `timestamp`, `event_type` (e.g., "Door Accessed", "Access Denied"), `door_name` (or `door_id`), `user_description` (or `user_id`, `credential_type`, `credential_identifier` like code used or card number). Refer to [Access Events Webhooks](/reference/access-events-webhooks).
        *   [ ] Format the extracted data into a string.
        *   [ ] Print the formatted string to the console.
    *   [ ] Add handling for unknown or unsupported event types (e.g., log a warning).

6.  **Error Handling and Logging:**
    *   [x] Implement `try...except` blocks in `app.py` for JSON decoding errors. (Added in Step 3)
    *   [ ] Implement `try...except` blocks in `handlers.py` for potential `KeyError` when accessing payload fields. Log errors appropriately.
    *   [x] Use Python's built-in `logging` module for basic logging (e.g., received webhook, validation success/failure, event processing start/end, errors). Configure basic logging in `app.py`. (Added basic config in Step 3)

7.  **Testing (Manual):**
    *   [ ] Run the Flask application.
    *   [ ] Configure a webhook in the Verkada Command platform pointing to the application's public URL (use `ngrok` or similar for local development).
    *   [ ] Trigger LPR and Access Control events in the Verkada system.
    *   [ ] Verify that the application receives the webhooks, validates them, and prints the correctly formatted information to the console.
    *   [ ] Test with invalid signatures (if possible to simulate) or old timestamps to ensure validation fails correctly.

8.  **Documentation (`README.md`):**
    *   [x] Update `README.md` with:
        *   [x] Detailed setup instructions (virtual env, install requirements).
        *   [x] Instructions on setting up the `.env` file and obtaining the `VERKADA_WEBHOOK_SECRET`.
        *   [ ] How to run the application (`flask run`).
        *   [ ] Explanation of the console output format.
        *   [ ] Instructions on using `ngrok` or similar for local testing.

---
**Future Considerations (Beyond Phase 1):**
*   Asynchronous processing (if webhook volume is high).
*   More robust error handling and alerting.
*   Data validation for payload fields.
*   Unit and integration tests.
*   Persistent storage (Phase 2).
*   Using the Verkada API Key for active polling or fetching additional details (Phase 2+).
