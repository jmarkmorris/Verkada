# Project: Verkada API Monitor for Gated Community

**Goal:** Develop a Python application to monitor events from a Verkada security system deployed in a gated neighborhood. The system includes cameras at entry gates (capturing LPR and access code usage) and other locations.

**Initial Functionality (Phase 1):**
*   Connect to the Verkada API using API keys.
*   Receive real-time events via Verkada Webhooks (primarily LPR and Access Control events).
*   Validate incoming webhooks using signature verification.
*   Parse event payloads (JSON).
*   Display event information as formatted text messages to the console.
*   For events associated with video (like LPR reads or motion detection), display relevant metadata (e.g., camera name, timestamp, license plate number) as text, without fetching or showing the actual video footage.

**Technology Stack (Initial):**
*   Python
*   `requests` library (for API communication)
*   `Flask` or `FastAPI` (for webhook receiver)
*   `python-dotenv` or YAML for configuration management

---

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <repo-directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create Configuration File (`.env`):**
    *   **Important:** For security, the `.env` file containing secrets is stored *outside* the project directory.
    *   Create a file named `.env` in the following location: `/Users/markmorris/Documents/Verkada-code-base/.env`
    *   Copy the contents from the example `.env` template below into your new `.env` file.
    *   **Crucially:** You need to obtain the `VERKADA_WEBHOOK_SECRET`.
        *   Log in to your Verkada Command account.
        *   Navigate to **Admin** -> **Integrations** -> **Webhooks**.
        *   Click **Add Webhook**.
        *   Configure the webhook (you'll need the URL where this application will be running later).
        *   Under the **Secret** section, generate or copy the secret value.
        *   Paste this value into your `.env` file (located at `/Users/markmorris/Documents/Verkada-code-base/.env`), replacing `"YOUR_VERKADA_WEBHOOK_SECRET"`.

    **.env Template:**
    ```dotenv
    # Verkada Configuration
    # Obtain this secret from the Verkada Command platform when setting up the webhook.
    # Go to Admin -> Integrations -> Webhooks -> Add Webhook -> Secret
    VERKADA_WEBHOOK_SECRET="YOUR_VERKADA_WEBHOOK_SECRET"

    # Flask Configuration (Optional, Flask defaults are often fine initially)
    # FLASK_APP=src.app
    # FLASK_ENV=development
    # FLASK_RUN_PORT=5000
    # FLASK_RUN_HOST=0.0.0.0
    ```
    *   **Security Note:** Ensure the directory `/Users/markmorris/Documents/Verkada-code-base/` and the `.env` file within it have appropriate permissions set and are not accidentally committed to any version control system.

---

## Running the Application

1.  Ensure your virtual environment is activated (`source venv/bin/activate` or `venv\Scripts\activate`).
2.  Make sure you have created the `.env` file at `/Users/markmorris/Documents/Verkada-code-base/.env` and added your `VERKADA_WEBHOOK_SECRET`.
3.  **From the project root directory (`Verkada`)**, run the application as a module:
    ```bash
    # Default (less verbose logging)
    python -m src.app

    # OR Verbose (more detailed logging including INFO messages)
    python -m src.app --verbose
    ```
    The server will start, typically listening on `http://0.0.0.0:5000/`. You should see log output indicating it has started (only if using `--verbose`). The `/webhook` endpoint will be available at `http://<your-ip-address>:5000/webhook`.

---

## Expected Output

When the application receives and successfully validates a webhook event from Verkada, it will **always print** a formatted message to the console where you ran the application:

*   **LPR Event:**
    ```
    Plate: <plate_number>, Time: <formatted_time>
    ```
*   **Access Event:**
    ```
    Door: <door_name>, User: <user_desc>, Credential ID: <credential_identifier>, Time: <formatted_time>
    ```

If you run with the `--verbose` flag, you will **also** see additional `INFO` level log messages in the console, such as:
