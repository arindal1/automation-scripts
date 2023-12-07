import pyautogui
from pynput.keyboard import Key, Listener
import tkinter as tk
from tkinter import messagebox, simpledialog

# ======== Controls ========
start_or_pause_key = Key.f1
exit_key = Key.esc
default_delay = 1  # seconds

# ==== Global variables ====
pause = True
running = True
delay = default_delay


def display_controls():
    messagebox.showinfo("Controls", "F1 = Start / Pause\nESC = Exit")


def choose_delay():
    global delay
    delay_str = simpledialog.askstring("Input", "Enter wanted delay (seconds):", parent=root)
    try:
        delay = float(delay_str) if delay_str else default_delay
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Using default delay.")
        delay = default_delay


def key_press(key):
    global running, pause

    if key == start_or_pause_key:
        pause = not pause
        print("< Pause >") if pause else print("< Start >")
        if not pause:
            click_periodically()
    elif key == exit_key:
        running = False
        print("< Exit >")
        root.destroy()


def click_periodically():
    if not pause and running:
        pyautogui.click(pyautogui.position())
        root.after(int(delay * 1000), click_periodically)


def on_start_button_click():
    global delay
    choose_delay()
    delay_label.config(text=f"Delay: {delay} sec")
    display_controls()
    listener = Listener(on_press=key_press)
    listener.start()


def on_exit_button_click():
    global running
    running = False
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("Auto Clicker")

# Create and configure widgets
delay_label = tk.Label(root, text=f"Delay: {default_delay} sec")
start_button = tk.Button(root, text="Start", command=on_start_button_click)
exit_button = tk.Button(root, text="Exit", command=on_exit_button_click)

# Place widgets in the window
delay_label.pack()
start_button.pack()
exit_button.pack()

# Start the GUI event loop
root.mainloop()
