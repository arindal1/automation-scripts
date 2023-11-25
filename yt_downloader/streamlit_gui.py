import streamlit as st
from pytube import YouTube
import tempfile
import os
import shutil

# Function to download a YouTube video with a progress bar
def download_video(url, save_path, progress_bar):
    try:
        # Callback function for download progress
        def on_progress(stream, chunk, remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - remaining

            # Calculate download progress as a percentage
            progress = bytes_downloaded / total_size
            # Update the Streamlit progress bar
            progress_bar.progress(progress)

        # Create a YouTube object with the provided URL and set the progress callback
        yt = YouTube(url, on_progress_callback=on_progress)
        
        # Filter available video streams to include only those that are progressive and in mp4 format
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        
        # Get the highest resolution stream
        highest_res_stream = streams.get_highest_resolution()

        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()

        # Download the video to the temporary directory with the progress callback
        temp_file_path = highest_res_stream.download(output_path=temp_dir)

        # Move the downloaded file to the specified save location
        shutil.move(temp_file_path, save_path)

        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

        # Display success message using Streamlit
        st.success("Video downloaded successfully!")
    except Exception as e:
        # Display an error message using Streamlit if an exception occurs
        st.error(f"An error occurred: {str(e)}")

# Function for the main Streamlit application
def main():
    # Set the title of the Streamlit app
    st.title("YouTube Video Downloader   ▶️")

    # Get YouTube URL from user using a Streamlit text input widget
    video_url = st.text_input("Enter YouTube URL:")

    # Get save location from user using a Streamlit text input widget
    save_dir = st.text_input("Enter Save Location:")

    # Download button and progress bar
    if st.button("Download"):
        if video_url and save_dir:
            # Create a Streamlit progress bar
            progress_bar = st.progress(0)
            # Call the download_video function with the provided URL, save location, and progress bar
            download_video(video_url, save_dir, progress_bar)
        else:
            # Display a warning message if either the URL or save location is not provided
            st.warning("Please enter a valid YouTube URL and select or enter a save location.")

# Entry point for the Streamlit app
if __name__ == "__main__":
    # Call the main function to run the Streamlit app
    main()
