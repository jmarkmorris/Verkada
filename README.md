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
    *   Create a file named `.env` in the root directory of the project.
    *   Copy the contents from the example `.env` file (or the template provided below) into your new `.env` file.
    *   **Crucially:** You need to obtain the `VERKADA_WEBHOOK_SECRET`.
        *   Log in to your Verkada Command account.
        *   Navigate to **Admin** -> **Integrations** -> **Webhooks**.
        *   Click **Add Webhook**.
        *   Configure the webhook (you'll need the URL where this application will be running later).
        *   Under the **Secret** section, generate or copy the secret value.
        *   Paste this value into your `.env` file, replacing `"YOUR_VERKADA_WEBHOOK_SECRET"`.

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
    *   **Security Note:** The `.env` file is listed in `.gitignore` and should **never** be committed to version control.

---

**Future Enhancements (Phase 2+):**
*   Persistent storage of events.
*   Fetching and displaying video thumbnails or links.
*   Web-based or GUI for event viewing and filtering.
*   Polling API endpoints as a supplement to webhooks.
