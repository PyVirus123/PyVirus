import ctypes
from pathlib import Path
import shutil
import os
import platform
import time

def duplicate_file(source_path, destination_path):
    shutil.copyfile(source_path, destination_path)

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

def get_wallpaper():
    if platform.system() == 'Windows':
        SPI_GETDESKWALLPAPER = 0x73
        wallpaper_path = ctypes.create_unicode_buffer(512)
        ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 512, wallpaper_path, 0)
        return Path(wallpaper_path.value)
    elif platform.system() == 'Darwin':  # macOS
        wallpaper_path = os.path.expanduser("~/Library/Application Support/Dock/desktoppicture.db")
        if os.path.exists(wallpaper_path):
            with open(wallpaper_path, "r") as f:
                lines = f.readlines()
                if lines:
                    return Path(lines[-1].strip())
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
                        return Path(wallpaper_path)
        return None
    else:
        print("Unsupported operating system")

def reload_wallpaper(log):
    if(log):
     print("getting wallpaper...")
    path = get_wallpaper()
    if(log):
     print("removing wallpaper...")
    set_wallpaper("")
    if(log):
     print("waiting for changes to take effect...")
    time.sleep(1)
    if(log):
     print("adding wallpaper back...")
    set_wallpaper(path)
    if(log):
     print("wallpaper reloaded sucesfully")

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def set_file_contents(file_path, contents):
    with open(file_path, 'w') as file:
        file.write(contents)

def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print("Directory created:", directory_path)
    else:
        print("Directory already exists:", directory_path)

def list_slots():
        for entry in os.listdir("wallpapers"):
         full_path = os.path.join("wallpapers", entry)
         if os.path.isdir(full_path):
            print(entry)

def delete_directory(directory_path):
    if os.path.exists(directory_path):
        try:
            shutil.rmtree(directory_path)
        except OSError as e:
            print("Error:", e)
            
def askaction():
    action = input("What would you like to do (save, load, reload, location, list)?: ")
    if(action == "delete"):
     name = input("enter name of wallpaper to delete: ")
     if(input("are you sure you want to delete your wallpaper " + name + "? (y/n): ") == "y"):
      print("deleting wallpaper if exsists...")
      delete_directory("wallpapers/" + name)
      print("deleted wallpaper " + name)
    if(action == "list"):
     print("every slot that is saved:")
     list_slots()
    if(action == "reload"):
     reload_wallpaper(True)
    if(action == "location"):
     print("Your wallpaper is at: " + str(get_wallpaper()))
    if(action == "save"):
     name = input("as how would you like to name it?: ")
     print("creating slot if inexsistant...")
     create_directory("wallpapers/" + name)
     print("creating metadata store if inexsistant...")
     create_directory("wallpapers/" + name + "/metadata")
     print("saving image...")
     duplicate_file(get_wallpaper(), "wallpapers/" + name + "/image." + get_file_extension(get_wallpaper()))
     print("saving metadata")
     set_file_contents("wallpapers/" + name + "/metadata/type.txt", get_file_extension(get_wallpaper()))
     print("wallpaper saved sucesfully!")
    if(action == "load"):
      name = input("enter the name of the saved wallpaper to load: ")
      print("checking for slot...")
      if(os.path.exists("wallpapers/" + name)):
        print("loading wallpaper image with metadata")
        set_wallpaper(os.path.abspath("wallpapers/" + name + "/image." + read_file_contents("wallpapers/" + name + "/metadata/type.txt")))
        print("wallpaper loaded sucesfully")
      else:
        print("slot not found")
    
    askaction()

askaction()
