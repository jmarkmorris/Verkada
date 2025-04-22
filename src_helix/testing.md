1,2,3 pass. Forbidden after that.

---

Here are the command lines to test each of the API scripts:

1. To test the Token API:
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_token_api.py --log_level INFO
```

2. To test the License Plates of Interest API:
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_lpoi_api.py --log_level INFO
```

3. To test the Cameras API:
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_cameras_api.py --log_level INFO
```

4. To test the LPR Images API (with default 7 days of history):
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_lpr_images_api.py --log_level INFO
```

5. To test the LPR Images API with a custom history period (e.g., 3 days):
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_lpr_images_api.py --history_days 3 --log_level INFO
```

6. To test the Alerts API (with default 7 days of history):
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_alerts_api.py --log_level INFO
```

7. To test the Alerts API with a custom history period (e.g., 14 days):
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_alerts_api.py --history_days 14 --log_level INFO
```

8. To test the Users List API:
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_users_list_api.py --log_level INFO
```

9. To test the User Details API (fetching details for the first user in the list):
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_user_details_api.py --log_level INFO
```

10. To test the User Details API for a specific user index (e.g., the third user, index 2):
```bash
export API_KEY="your_verkada_api_key"
python src_helix/test_user_details_api.py --user_index 2 --log_level INFO
```

For more detailed logging, you can change `--log_level INFO` to `--log_level DEBUG` in any of these commands.
