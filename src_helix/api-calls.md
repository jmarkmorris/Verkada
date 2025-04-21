# Verkada API Query Script (`src_helix/`)

**Goal:** Provide a command-line script to query various Verkada API endpoints, specifically focusing on retrieving License Plate Recognition (LPR) data.

**Functionality:**
*   Authenticates with the Verkada API using a two-step process (API Key to get API Token).
*   Supports querying different API endpoints via command-line flags.
*   Currently implements fetching License Plates of Interest (LPOIs) and LPR events.
*   Handles pagination for LPR events.
*   Allows specifying the history duration for LPR event queries.

**Technology Stack:**
*   Python 3.x
*   `requests` (for making HTTP requests)
*   `argparse` (for command-line arguments)
*   Standard libraries: `os`, `sys`, `logging`, `datetime`, `time`

---

## API Endpoints Used

The `src_helix/lpoi.py` script interacts with the following Verkada API endpoints:

1.  **Get API Token (`POST /token`)**: Used to exchange a long-lived API Key for a short-lived API Token (valid for 30 minutes). This is the first step in authenticating API requests.
    *   *Documentation:* [API Login](https://apidocs.verkada.com/reference/postloginapikeyviewv2)

2.  **Get All License Plates of Interest (`GET /cameras/v1/analytics/lpr/license_plate_of_interest`)**: Retrieves a list of all configured License Plates of Interest in the organization.
    *   *Documentation:* [Get All License Plates of Interest](https://apidocs.verkada.com/reference/getlicenseplateofinterestviewv1)

3.  **Get Camera Data (`GET /cameras/v1/devices`)**: Retrieves a list of cameras in the organization. This is used to get camera IDs for querying LPR events.
    *   *Documentation:* (Implicitly covered in Camera API section)
    *   *Note on Issue:* We initially encountered an issue where the script expected camera IDs under the key `'id'` based on a common pattern, but the API response for this endpoint uses the key `'camera_id'`. This was corrected in the script.

4.  **Get seen license plates (`GET /cameras/v1/analytics/lpr/imagesview`)**: Retrieves a list of LPR detection events within a specified time range. This endpoint provides the license plate, camera ID, and timestamp for each detection. This is the primary endpoint used to find LPR events for LPOIs.
    *   *Documentation:* [Get seen license plates](https://apidocs.verkada.com/reference/getlprimagesview)
    *   *Note on Approach:* This endpoint was chosen over `/cameras/v1/analytics/lpr/timestamps` because it allows fetching all events in a range and filtering locally, which is more efficient than querying timestamps for each LPOI on each camera individually. The script implements basic pagination for this endpoint to retrieve all available events within the time range.
    *   *Note on Issue:* Accessing this endpoint requires specific API Key permissions (Camera API Read access), which resulted in a `403 Forbidden` error until the key's permissions were correctly configured in Verkada Command.

---

## API Rate Limiting

When fetching large amounts of data, particularly when paginating through results from endpoints like `/cameras/v1/analytics/lpr/imagesview`, you may encounter API rate limits. If you receive `429 Too Many Requests` errors, consider adding a small delay (e.g., `time.sleep(0.1)`) between API calls, especially between fetching subsequent pages of results.

---

## Verkada API Authentication

The script follows the recommended two-factor authentication flow:

1.  A long-lived **API Key** (stored securely as an environment variable `API_KEY`) is used to request a short-lived **API Token** from the `/token` endpoint.
2.  The **API Token** is then used in the `x-verkada-auth` header for subsequent calls to other API endpoints (like fetching LPOIs or LPR events).

Ensure your `API_KEY` environment variable is set correctly and that the corresponding API Key in Verkada Command has the necessary permissions for the endpoints being queried (at least "Read-only access" for the Camera API for the current functionality).

---

## Script Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    # Replace <your-repo-url> with the actual repository URL
    cd Verkada # Assuming project root is Verkada
    ```

2.  **Create and activate a virtual environment:**
    *   It's recommended to create a separate environment for the script:
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
    pip install -r requirements.md # Assuming requirements.md lists 'requests'
    ```
    *   *Note:* The `requirements.md` file should contain the necessary dependencies, including `requests`. If not, you might need to manually install `requests` (`pip install requests`).

4.  **Set Environment Variable (`API_KEY`):**
    *   Obtain your Verkada API Key from Verkada Command (**Admin** -> **Integrations** -> **API**).
    *   Set the `API_KEY` environment variable in your terminal session:
        ```bash
        export API_KEY="YOUR_VERKADA_API_KEY"
        ```
    *   *Note:* For persistent environment variables, consult your operating system's documentation (e.g., add to `.bashrc`, `.zshrc`, or system environment variables).

---

## Script Usage

The script is run from the command line, specifying the API to query and other options.

1.  **Activate Virtual Environment:** Ensure your `venv_helix` virtual environment is activated.
2.  **Run the Script:**
    *   Navigate to the project's root directory (`Verkada`) in your terminal.
    *   Execute the script using the `src_helix` module, specifying the API:
        ```bash
        # Example: Fetch LPR events for LPOIs with 7 days of history
        python -m src_helix.lpoi --api lpr_events --history_days 7 --log_level INFO
        ```
    *   Replace `lpr_events` with the desired API name if more handlers are added to `src_helix/lpoi.py`.
    *   Adjust `--history_days` to specify the time range for LPR event queries.
    *   Adjust `--log_level` (DEBUG, INFO, WARNING, ERROR, CRITICAL) for desired logging verbosity. Use `DEBUG` to see detailed request/response information.

