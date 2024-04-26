print("Loading Modules...")
print("import os")
import os
print("import psutil (recommended but optional)")
try:
    import psutil
except ImportError:
    print("psutil is not installed. this will prevent the 'stop' action from working.")
print("import requests (recommended but optional)")
try:
    import requests
except ImportError:
    print("requests is not installed. this will prevent the 'install' action from working.")
print("Modules loaded!")
print("WARNING: DO NOT USE THIS SOFTWARE IF YOU DONT KNOW WHAT YOU ARE DOING. THIS IS FOR EDUCATIONAL PURPOSES ONLY.")
print("Welcome to PyVirus.")

def execute_setup(script_url):
    try:
        # Fetch the Python script from the URL
        response = requests.get(script_url)
        if response.status_code == 200:
            # Execute the fetched Python script
            exec(response.text)
        else:
            print(f"Setup failed. ERROR: Network Error with status {response.status_code}. URL: {script_url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

def stopvirus(file_path):
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if proc.info['exe'] == file_path:
                print(f"Terminating process: {proc.pid}")
                proc.terminate()
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass

def uninstallVirus(directory):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        # Delete each file in the directory
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                print(f"Deleting file: {file_path}")
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

        # Delete the directory itself
        os.rmdir(directory)
        print(f"Uninstalled Virus at {directory} Sucesfully!")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

def askaction():
 command = input("Enter A Command (install, uninstall, launch):")
 if command == "launch":
  if os.path.isdir("viruses"):
   typ = input("What type of virus would you like to launch (custom, preset):")
   if typ == "preset":
    if os.path.isdir("viruses/preset"):
     name = input("Enter the name of the preset virus.")
     if os.path.isdir("viruses/preset/" + name):
      os.startfile("viruses/preset/" + name + "/main.py")
     else:
      print("ERROR: That preset does not exsist or is not installed.")
   else:
     print("ERROR: installation is corrupt. (the viruses store dosent contain preset category).")
   if typ == "custom":
     name = input("Enter the name of the preset virus.")
     if os.path.isdir("viruses/custom/" + name):
      os.startfile("viruses/custom/" + name + "/main.py")
     else:
      print("ERROR: That custom virus does not exsist or is not installed.")
  else:
    print("ERROR: installation is corrupt. (theres no viruses store.)")
 elif command == "install":
    name = input("Enter the name of the preset to install:")
    execute_setup("https://pyvirus123.github.io/PyVirus/viruses/preset/" + name + "/setup.py")
 elif command == "uninstall":
  if os.path.isdir("viruses"):
   typ = input("Enter the type of the virus you would like to uninstall (custom, preset):")
   if typ == "preset":
    if os.path.isdir("viruses/preset"):
     name = input("Enter the name of the preset virus.")
     if os.path.isdir("viruses/preset/" + name):
      uninstallVirus("viruses/preset/" + name)
     else:
      print("ERROR: That preset does not exsist or is not installed.")
   else:
     print("ERROR: installation is corrupt. (the viruses store dosent contain custom category).")
   if typ == "custom":
     name = input("Enter the name of the custom virus.")
     if os.path.isdir("viruses/custom/" + name):
      uninstallVirus("viruses/custom/" + name)
     else:
      print("ERROR: That custom virus does not exsist or is not installed.")
  else:
    print("ERROR: installation is corrupt. (theres no viruses store.)")
 elif command == "stop":
  if os.path.isdir("viruses"):
   typ = input("Enter the type of virus to stop (custom, preset):")
   if typ == "preset":
    if os.path.isdir("viruses/preset"):
     name = input("Enter the name of the preset virus.")
     if os.path.isdir("viruses/preset/" + name):
      stopvirus("viruses/preset/" + name)
     else:
      print("ERROR: That preset does not exsist or is not installed.")
   else:
     print("ERROR: installation is corrupt. (the viruses store dosent contain custom category).")
   if typ == "custom":
     name = input("Enter the name of the custom virus.")
     if os.path.isdir("viruses/custom/" + name):
      stopvirus("viruses/custom/" + name)
     else:
      print("ERROR: That custom virus does not exsist or is not installed.")
  else:
    print("ERROR: installation is corrupt. (theres no viruses store.)")
 else:
  print("ERROR: Command not found")
 askaction() 
askaction()
