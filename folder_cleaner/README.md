# Recursive Empty Folder Cleaner

This project contains scripts in various programming languages for recursively removing empty folders and subdirectories from a given root path.

## Scripts

### Python Script (auto_clicker.py)

#### Dependencies
- `pyautogui`
- `pynput`

#### Usage
1. Install dependencies: `pip install pyautogui pynput`
2. Run the script: `python auto_clicker.py`

### Bash Script (auto_clicker.sh)

#### Dependencies
- None

#### Usage
1. Make the script executable: `chmod +x auto_clicker.sh`
2. Run the script: `./auto_clicker.sh`

### C++ Script (auto_clicker.cpp)

#### Dependencies
- C++17 or later

#### Usage
1. Compile the script: `g++ -o auto_clicker auto_clicker.cpp -std=c++17`
2. Run the compiled executable: `./auto_clicker`

## How It Works

- The scripts prompt the user to input the desired path and whether to remove the root folder if all subdirectories are empty.
- The scripts then recursively traverse the directory structure, removing empty folders and subdirectories.
- Progress is printed to the console when the `verbose` option is enabled.

## Notes

- Use caution when running these scripts, as they will permanently delete empty folders.
- Always ensure that you have a backup of important data before using this tool.
