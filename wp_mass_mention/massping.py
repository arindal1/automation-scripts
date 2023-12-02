import pyautogui
import time

def mention_all(group_size):
    for i in range(1, group_size + 1):
        pyautogui.typewrite("@")
        press_down_key(i)
        pyautogui.press("enter")
        pyautogui.hotkey("shift", "enter")
        time.sleep(0.5)  # Add a small delay between iterations

def press_down_key(times):
    for _ in range(times):
        pyautogui.press("down")

if __name__ == "__main__":
    try:
        group_size = int(input("Enter the size of the group: "))
        time.sleep(2)  # Delay before starting
        mention_all(group_size)
    except ValueError:
        print("Please enter a valid integer for the group size.")

