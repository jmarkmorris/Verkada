# Issue: `Handler function not found or not callable` for `handle_alerts_api`

**Date:** 2025-04-21

**Problem Description:**

When attempting to run the `src_helix/lpoi.py` script with the `--api alerts` command-line flag, the script fails with a `TypeError: Handler function not found or not callable for API: alerts (handle_alerts_api)`.

This occurs despite the `alerts` option being correctly added to the `API_ENDPOINTS` dictionary and the `argparse` choices. The error indicates that the script cannot find or execute the `handle_alerts_api` function.

We have attempted to uncomment the `handle_alerts_api` function definition in `src_helix/lpoi.py` multiple times using `SEARCH/REPLACE` blocks, but the error persists, suggesting the function is still not correctly defined or is commented out in the file being executed.

The expected behavior is that the script should find and execute the `handle_alerts_api` function when `--api alerts` is used.

**Problematic Code Snippet (as it appears when the error occurs):**

The `handle_alerts_api` function definition appears to be commented out, preventing the script from finding it:

````python
# def handle_alerts_api(api_token: str, history_days: int) -> None:
#     """
#     Fetches alerts using the /notificationsviewv1 endpoint within the specified history days.
#     This is a potential workaround to find LPR events if /imagesview is inaccessible.
#
#     Args:
#         api_token: The short-lived Verkada API Token.
#         history_days: The number of days of history to query for alerts.
#     """
#     try:
#         # Calculate start and end time based on history_days
#         end_time = int(time.time())
#         start_time = end_time - (history_days * 24 * 60 * 60)
#         logger.info(f"Querying alerts for the last {history_days} days (from {datetime.datetime.fromtimestamp(start_time)} to {datetime.datetime.fromtimestamp(end_time)})")
#
#         all_alerts = []
#         page_token = None
#         alerts_endpoint = ALERTS_ENDPOINT
#
#         logger.info(f"Fetching alerts from {alerts_endpoint}...")
#
#         while True:
#             alerts_params = {
#                 "start_time": start_time,
#                 "end_time": end_time,
#                 "page_size": 200 # Max page size for this endpoint
#             }
#             if page_token:
#                 alerts_params["page_token"] = page_token
#
#             alerts_data = fetch_api_data(api_token, alerts_endpoint, params=alerts_params)
#
#             if 'notifications' not in alerts_data or not isinstance(alerts_data['notifications'], list):
#                  logger.warning(f"Unexpected API response format for alerts from {alerts_endpoint}: missing or invalid 'notifications' list. Raw data: {alerts_data}. Stopping pagination.")
#                  break # Stop fetching if the format is unexpected
#
#             alerts_page = alerts_data['notifications']
#             all_alerts.extend(alerts_page)
#
#             page_token = alerts_data.get('next_page_token')
#             if not page_token:
#                 break # Stop if there are no more pages
#
#             logger.info(f"Fetched {len(alerts_page)} alerts, fetching next page with token: {page_token}")
#             # Consider adding a small delay here to avoid hitting rate limits, especially with many pages
#             # time.sleep(0.1)
#
#         logger.info(f"Fetched a total of {len(all_alerts)} alerts within the specified time range.")
#
#         if not all_alerts:
#             logger.info(f"No alerts found in the last {history_days} days.")
#             return
#
#         # Print details of alerts - you will need to inspect the output to see
#         # if LPR event details are included in the alert object structure.
#         print("\n--- All Alerts ---")
#         for alert in all_alerts:
#             # Print the full alert object for inspection
#             print(f"  Alert: {alert}")
#             print("-" * 20)
#
#         logger.info("Please inspect the alert objects above to see if they contain LPR event details (e.g., license plate, camera ID, timestamp).")
#
#
#     except (requests.exceptions.RequestException, ValueError) as e:
#         logger.error(f"Failed during alerts processing: {e}", exc_info=True)
#         raise # Re-raise to be caught by the main error handler
````

**Next Steps:**

The primary task is to ensure the `handle_alerts_api` function is correctly uncommented in `src_helix/lpoi.py`. Once that is confirmed, running the script with `--api alerts` should execute the function and print the raw alert data for inspection.
