print("loading modules...")
print("import requests")
try:
    import requests
except ModuleNotFoundError:
    print("ERROR: module not found. please install the module requests to continue.")
    input("press enter to exit")
    exit()
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
print("setup has been initalized")
print("creating directories")
if not os.path.isdir("viruses"):
 os.mkdir("viruses")
if not os.path.isdir("viruses/preset"):
 os.mkdir("viruses/preset")
if not os.path.isdir("viruses/custom"):
 os.mkdir("viruses/custom")
print("directories created")
print("downloading files")
try:
 download_file("http://example.com/data.txt", save_path)
except:
 print("Failed to download files.")
 input("Press enter to exit")
 exit()
print("Files downloaded sucesfully!")
input("Press enter to exit")
exit()
