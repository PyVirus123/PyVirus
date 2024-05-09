import os
import sys
import zipfile
import time
import platform
import ctypes
import shutil
import tkinter as tk
from tkinter import filedialog


def execute_script(script_path):
    # Get the absolute path of the other Python script
    abs_script_path = os.path.abspath(script_path)

    # Get the directory of the script being executed
    script_dir = os.path.dirname(abs_script_path)

    # Change the directory to the script directory
    os.chdir(script_dir)

    # Get the absolute path of the Python interpreter executable
    python_interpreter = sys.executable

    # Execute the script using the Python interpreter
    os.system(f"{python_interpreter} {abs_script_path}")


def extract_zip(zip_file, extract_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

def set_wallpaper(image_path):
    if platform.system() == 'Windows':
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(image_path), 3)
    elif platform.system() == 'Darwin':  # macOS
        os.system("osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + str(image_path) + "\"'")
    elif platform.system() == 'Linux':
        os.system("gsettings set org.gnome.desktop.background picture-uri file://" + str(image_path))
    else:
        print("Unsupported operating system")

def get_current_wallpaper():
    if platform.system() == 'Windows':
        SPI_GETDESKWALLPAPER = 0x73
        wallpaper_path = ctypes.create_unicode_buffer(512)
        ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 512, wallpaper_path, 0)
        return wallpaper_path.value
    elif platform.system() == 'Darwin':  # macOS
        wallpaper_path = os.path.expanduser("~/Library/Application Support/Dock/desktoppicture.db")
        if os.path.exists(wallpaper_path):
            with open(wallpaper_path, "r") as f:
                lines = f.readlines()
                if lines:
                    return lines[-1].strip()
        return None
    elif platform.system() == 'Linux':
        config_home = os.environ.get('XDG_CONFIG_HOME') or os.path.join(os.path.expanduser('~'), '.config')
        config_file = os.path.join(config_home, 'xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml')
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if 'last-image' in line:
                        wallpaper_path = line.split('value="')[1].split('"')[0]
                        return wallpaper_path
        return None
    else:
        print("Unsupported operating system")
        return None

def play_animation(animation_folder):
    frames_file = os.path.join(animation_folder, "frames.txt")
    if not os.path.exists(frames_file):
        print("Error: frames.txt not found in", animation_folder)
        return

    with open(frames_file, 'r') as file:
        num_frames = int(file.read().strip())

    frames_folder = os.path.join(animation_folder, "frames")
    print("Frames folder contents:", os.listdir(frames_folder))
    for i in range(1, num_frames + 1):
        frame_folder = os.path.join(frames_folder, str(i))
        print("Frame folder:", frame_folder)
        metadata_folder = os.path.join(frame_folder, "metadata")

        if not os.path.exists(metadata_folder):
            print(f"Error: Metadata folder not found for frame {i} in {animation_folder}")
            continue

        metadata_file = os.path.join(metadata_folder, "type.txt")
        if not os.path.exists(metadata_file):
            print(f"Error: Metadata file not found for frame {i} in {animation_folder}")
            continue

        with open(metadata_file, 'r') as meta_file:
            file_extension = meta_file.read().strip()

        frame_image = os.path.abspath(os.path.join(frame_folder, f"frame{file_extension}"))

        if not os.path.exists(frame_image):
            print(f"Error: Frame image not found for frame {i} in {animation_folder}")
            continue

        set_wallpaper(frame_image)
        time.sleep(1)

    # Show last frame for an additional second
    set_wallpaper(frame_image)
    time.sleep(1)

def restore_wallpaper(original_wallpaper):
    set_wallpaper(original_wallpaper)

def select_animation():
    animations_folder = "animations"
    animation_folders = [folder for folder in os.listdir(animations_folder) if os.path.isdir(os.path.join(animations_folder, folder))]
    
    print("Available animations:")
    for animation in animation_folders:
        print(animation)
    
    while True:
        choice = input("Enter the name of the animation you want to play: ")
        if choice in animation_folders:
            return os.path.join(animations_folder, choice)
        else:
            print("Invalid animation name. Please enter a valid name.")

def add_animation_from_zip():
    animations_folder = "animations"
    
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Prompt user to select a file
    zip_file = filedialog.askopenfilename(title="Select ZIP file", filetypes=(("ZIP files", "*.zip"), ("All files", "*.*")))
    if not zip_file:
        print("No file selected.")
        return
    
    # Prompt user to enter animation name
    animation_name = input("Enter the name for the new animation: ")
    animation_folder = os.path.join(animations_folder, animation_name)
    if os.path.exists(animation_folder):
        print("Error: Animation folder already exists.")
        return
    
    os.makedirs(animation_folder)
    extract_zip(zip_file, animation_folder)

def delete_animation(animation_name):
    animations_folder = "animations"
    animation_folder = os.path.join(animations_folder, animation_name)
    
    if os.path.exists(animation_folder):
        shutil.rmtree(animation_folder)
        print(f"Animation '{animation_name}' deleted successfully.")
    else:
        print(f"Animation '{animation_name}' does not exist.")


def main():
  def askaction():
    try:
     choice = input("what would you like to do? (play, add, remove, make): ")
     
     if choice.lower() == "play":
        original_wallpaper = get_current_wallpaper()
        animation_folder = select_animation()
        play_animation(animation_folder)
        if original_wallpaper:
         restore_wallpaper(original_wallpaper)
        askaction()
     elif choice.lower() == "add":
        add_animation_from_zip()
        askaction()
     elif choice.lower() == "make":
        if(os.path.exists("../../../PyVirus.py")):
          if(os.path.exists("../WallpaperAnimationMaker")):
            execute_script(os.path.abspath("../WallpaperAnimationMaker/main.py"))
            input("press enter to exit")
          else:
            print("ERROR: WallpaperAnimationMaker is not installed. install it to open the editor.")
        else:
           print("ERROR: you are not in a PyVirus environment.")
        askaction()
     elif choice.lower() == "remove":
        delete_animation(input("Enter name of animation to delete: "))
        askaction()
     else:
        print("Invalid action.")
        askaction()
    except Exception as e:
     print("An error occurred:", e)
    askaction()
  askaction()

if __name__ == "__main__":
    main()
