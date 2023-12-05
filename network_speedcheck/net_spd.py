import streamlit as st
import speedtest
import time
from speedtest import ConfigRetrievalError

def get_speed_test_results(log_file="speed_test_log.txt"):
    try:
        st.text("Running speed test...")
        
        stt = speedtest.Speedtest()
        stt.get_best_server()

        download_speed = stt.download() / 1_000_000  # Convert to Mbps
        upload_speed = stt.upload() / 1_000_000  # Convert to Mbps

        st.write(f"**Download Speed:** {download_speed:.2f} Mbps")
        st.write(f"**Upload Speed:** {upload_speed:.2f} Mbps")

        # Log results to a file
        log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps\n"
        with open(log_file, "a") as log_file:
            log_file.write(log_entry)

        return download_speed, upload_speed
    except Exception as e:
        st.error(f"Error: {e}. Check your network connection.")
        # Log errors to a file
        error_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Error: {str(e)}\n"
        with open(log_file, "a") as log_file:
            log_file.write(error_entry)
        return None, None

if __name__ == "__main__":
    st.title("Network Speed Tester")
    st.warning("This may take a moment.")

    while True:
        with st.spinner("Testing..."):
            download_speed, upload_speed = get_speed_test_results()

        # Update every second
        time.sleep(1)

        # Clear previous results
        st.empty()  # Clear the "Running speed test..." message
        st.empty()  # Clear the previous results
