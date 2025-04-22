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

For more detailed logging, you can change `--log_level INFO` to `--log_level DEBUG` in any of these commands.