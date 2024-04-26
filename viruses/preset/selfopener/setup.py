print("loading modules...")
print("import requests")
try:
    import requests
except ModuleNotFoundError:
    print("ERROR: module not found. please install the module requests to continue.")
print("modules loaded")
print("loading classes...")
print("class CustomError()")
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
print("classes loaded")
print("loading functions...")
print("def download_file()")
def download_file(url, save_path):
    print("Downloading " + save_path)
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a file in binary write mode and write the response content to it
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("Downloaded " + save_path)
    else:
        print(f"Failed to download " + save_path + ". Status code: {response.status_code}")
        raise CustomError("Could not download file " + save_path)
print("functions loaded")
print("creating directory")
if not os.path.isdir("viruses/preset/selfopener"):
 os.mkdir("viruses/preset/selfopener")
print("directories created")
print("downloading files")
try:
 download_file("https://pyvirus123.github.io/PyVirus/viruses/preset/selfopener/main.py", "viruses/preset/selfopener/main.py")
except:
 print("Failed to download files.")
print("Virus install sucesfully!")
