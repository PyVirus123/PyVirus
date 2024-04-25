print("Loading Modules...")
print("import os")
import os
print("Modules loaded!")
print("WARNING: DO NOT USE THIS SOFTWARE IF YOU DONT KNOW WHAT YOU ARE DOING. THIS IS FOR EDUCATIONAL PURPOSES ONLY.")
print("Welcome to PyVirus.")
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
     print("Sorry! custom viruses are not implemented yet.")
  else:
    print("ERROR: installation is corrupt. (theres no viruses store.)")
 elif command == "install":
  print("comin soon")
 elif command == "uninstall":
  print("Comin after install")
 else:
  print("ERROR: Command not found")
 askaction() 
askaction()
