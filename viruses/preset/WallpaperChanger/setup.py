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
def download_github_pages_directory(owner, repo, path, target_directory):
    os.makedirs(target_directory, exist_ok=True)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)
    if response.status_code == 200:
        contents = response.json()
        for item in contents:
            if item['type'] == 'file':
                download_file(item['download_url'], target_directory)
            elif item['type'] == 'dir':
                subdir_path = os.path.join(path, item['name'])
                subdir_target_directory = os.path.join(target_directory, item['name'])
                download_directory(owner, repo, subdir_path, subdir_target_directory)
    else:
        print(f"Failed to access directory at {url}. Status code: {response.status_code}")

def parse_and_download_github_pages_url(url, target_directory):
    owner, repo, path = parse_github_pages_url(url)
    download_github_pages_directory(owner, repo, path, target_directory)
  
def parse_github_pages_url(url):
    # Remove leading and trailing slashes
    url = url.strip("/")

    # Split the URL by "/"
    parts = url.split("/")

    # Extract owner, repository, and path
    owner = parts[parts.index("github.io") - 1]
    repo = parts[parts.index(owner) + 1]
    path_parts = parts[parts.index(repo) + 1:]
    path = "/".join(path_parts)

    return owner, repo, path
print("functions loaded")
print("creating directory")
if not os.path.isdir("viruses/preset/WallpaperChanger"):
 os.mkdir("viruses/preset/WallpaperChanger")
print("directories created")
print("downloading files")
try:
 download_file("https://pyvirus123.github.io/PyVirus/viruses/preset/WallpaperChanger/main.py", "viruses/preset/WallpaperChanger/main.py")
 parse_and_download_github_pages_url("https://pyvirus123.github.io/PyVirus/viruses/preset/WallpaperChanger/wallpapers", "viruses/preset/WallpaperChanger")
except:
 print("Failed to download files.")
print("Virus installed sucesfully!")
