# Auto Clicker Script

This project contains scripts in various programming languages to implement a basic auto-clicker functionality. The auto-clicker can be controlled using keyboard shortcuts, allowing users to start/pause and exit the auto-clicker.

### Scripts

## Python Script (auto_clicker.py)

#### Dependencies
- `pyautogui`
- `pynput`

#### Usage
1. Install dependencies: `pip install pyautogui pynput`
2. Run the script: `python auto_clicker.py`

## Bash Script (auto_clicker.sh)

#### Dependencies
- `xdotool`

#### Usage
1. Install dependencies: `sudo apt-get install xdotool`
2. Make the script executable: `chmod +x auto_clicker.sh`
3. Run the script: `./auto_clicker.sh`

## C++ Script (auto_clicker.cpp)

#### Dependencies
- `SDL2` library

#### Usage
1. Install SDL2 library (on Debian/Ubuntu): `sudo apt-get install libsdl2-dev`
2. Compile the script: `g++ -o auto_clicker auto_clicker.cpp -lSDL2`
3. Run the compiled executable: `./auto_clicker`

## C# Script (AutoClickerApp)

#### Dependencies
- .NET Framework
- Visual Studio (for development)

#### Usage
1. Open the project in Visual Studio.
2. Build and run the application.

## Controls

- **F1:** Start / Pause auto-clicking.
- **Esc:** Exit the auto-clicker.

## Notes
- The delay can be configured in each script to control the clicking interval.

