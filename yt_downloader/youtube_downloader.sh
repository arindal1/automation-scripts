#!/bin/bash

# Prompt the user for a YouTube URL
read -p "Enter YouTube URL: " video_url

# Prompt the user for a save location
read -p "Enter Save Location: " save_dir

# Use youtube-dl to download the video
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' --merge-output-format mp4 -o "${save_dir}/%(title)s.%(ext)s" "$video_url"

# Check the exit status of the last command
if [ $? -eq 0 ]; then
  echo "Video downloaded successfully!"
else
  echo "An error occurred during download."
fi
