<div align="center">
  <h1>YouTube Downloader using Python</h1>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/2560px-YouTube_Logo_2017.svg.png" alt="header image"><br>
</div>

## GUI using 'tkinter'

- Used `tkinter` to create a window with entry fields and buttons for the user to input the URL and choose the save location.

### How to run?

Run command:
```
python tkinter_gui.py
```
Run the above command in your terminal. You can replace `tkinter_gui` with you desired file name.


## GUI using StreamLit

- Used Streamlit to create a web-based user interface. Streamlit is a Python library for creating web applications with minimal effort.

### How to run?

Run command:
```
steamlit run streamlit_gui.py
```
Run the above command in your terminal. You can replace `streamlit_gui` with you desired file name.

### For the bash script:

Make the script `youtube_downloader.sh` executable by running:

```bash
chmod +x youtube_downloader.sh
```

Then, you can run the script:

```bash
./youtube_downloader.sh
```

This script uses `youtube-dl` to download the video in the best quality available. It extracts both video and audio and merges them into a single MP4 file. Make sure you have `youtube-dl` installed on your system. You can install it using the package manager for your operating system (e.g., `sudo apt-get install youtube-dl` on Debian-based systems).
