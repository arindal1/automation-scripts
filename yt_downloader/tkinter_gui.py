# Import necessary libraries
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to download the video from the provided URL to the specified directory
def download_video(url, save_path):
    try:
        # Create a YouTube object from the given URL
        yt = YouTube(url)
        
        # Filter available video streams to include only those that are progressive and in mp4 format
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        
        # Get the highest resolution stream
        highest_res_stream = streams.get_highest_resolution()
        
        # Download the video to the specified directory
        highest_res_stream.download(output_path=save_path)
        
        # Show a success message to the user
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        # Show an error message if an exception occurs during the download process
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open a file dialog for selecting a directory
def open_file_dialog():
    # Ask the user to select a directory and return the selected folder path
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

# Function to start the video download process
def start_download():
    # Get the video URL from the entry widget
    video_url = url_entry.get()
    
    # Open a file dialog to select the download directory
    save_dir = open_file_dialog()

    # If a valid directory is selected, initiate the video download
    if save_dir:
        download_video(video_url, save_dir)

# Create the main window
root = tk.Tk()

# Set the title of the GUI window
root.title("YouTube Video Downloader")

# Set the initial size of the GUI window
root.geometry("500x200")  # Set the width to 500 pixels and height to 200 pixels

# Create and place widgets in the GUI window
tk.Label(root, text="YouTube URL:").pack(pady=10)  # Label for the URL entry
url_entry = tk.Entry(root, width=40)  # Entry widget to input the YouTube URL
url_entry.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=open_file_dialog)  # Button to browse and select download directory
browse_button.pack(pady=10)

download_button = tk.Button(root, text="Download", command=start_download)  # Button to initiate the download process
download_button.pack(pady=20)

# Run the GUI
root.mainloop()
