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

**Future Enhancements (Phase 2+):**
*   Persistent storage of events.
*   Fetching and displaying video thumbnails or links.
*   Web-based or GUI for event viewing and filtering.
*   Polling API endpoints as a supplement to webhooks.
