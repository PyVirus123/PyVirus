print("starting initalization of PyVirusSetup.py")
print("loading modules...")
print("import requests")
try:
    import requests
except ModuleNotFoundError:
    print("ERROR: module not found. please install the module requests to continue.")
    input("press enter to exit")
    exit()
print("modules loaded")
print("getting main setup via network...")
response = requests.get("https://pyvirus123.github.io/PyVirus/data/setup/setup.py")
if response.status_code == 200:
 print("main setup gotten via network. launching...")
 exec(response.content)
else:
 print("Failed to retreive main setup via network")
 input("press enter to exit")
 exit()
