# Network Speed Tester

This is a simple Streamlit application that measures your network's download and upload speeds using the Speedtest library. The results are displayed in real-time, and the logs are saved to a file.

## How to Use

1. Make sure you have Python installed on your system.

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run speed_test_app.py
    ```

4. The application will display the current download and upload speeds. It will refresh every second.

## Requirements

- `streamlit` for creating the web application.
- `speedtest` for measuring network speeds.
- `time` for handling time-related operations.

## Logs

The results of each speed test, as well as any errors encountered, will be logged to the `speed_test_log.txt` file.
