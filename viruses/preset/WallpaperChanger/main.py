import ctypes
import os
import random
import time
import platform

supported = ["Windows"]

def set_wallpaper(image_path):
    if(platform.system() == "Windows"):
     SPI_SETDESKWALLPAPER = 20
     ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def change_desktop_wallpaper(wallpaper_directory):
    wallpapers = [os.path.join(wallpaper_directory, file) for file in os.listdir(wallpaper_directory) if file.endswith(('.jpg', '.jpeg', '.png'))]
    if wallpapers:
        while True:
            selected_wallpaper = random.choice(wallpapers)
            selected_wallpaper_full_path = os.path.abspath(selected_wallpaper)  
            set_wallpaper(selected_wallpaper_full_path)
            print(f"Desktop wallpaper changed to: {selected_wallpaper_full_path}")
            time.sleep(0.0000000001)  # Change wallpaper every 5 seconds
    else:
        print("No valid wallpaper images found in the directory.")

if platform.system() in supported:
    wallpaper_directory = "wallpapers"
    change_desktop_wallpaper(wallpaper_directory)
else:
    print("ERROR: this operating system is not supported")
