#            ╔═════════════════════════HaZaRd═════════════════════════════╗
#            ║        Youtube: https://www.youtube.com/@IIIHaZaRd         ║
#            ║        Github: https://github.com/Pytholearn               ║
#            ║        Discord: https://discord.gg/YU7jYRkxwp              ║
#            ╚════════════════════════════════════════════════════════════╝

# This is a Python script for an automatic updating system using a library named AutoUpdate
import urllib.request

# Default URL for fetching the latest version information
url = ""

# Current version of the program
current = ""

# Default download link for the updated program
download_link = ""

# Function to set a new URL for fetching version information
def set_url(url_):
    global url
    url = url_

# Function to retrieve the latest version information from the specified URL
def get_latest_version():
    file = urllib.request.urlopen(url)
    lines = ""
    for line in file:
        lines += line.decode("utf-8")
    return lines

# Function to set the current version of the program
def set_current_version(current_):
    global current
    current = current_

# Function to set a new download link for the updated program
def set_download_link(link):
    global download_link
    download_link = link

# Function to check if the current program version is up to date
def is_up_to_date():
    return current + "\n" == get_latest_version()

# Function to download and save the updated program to a specified path
def download(path_to_file):
    urllib.request.urlretrieve(download_link, path_to_file)



#═══════════════════════════════════════════════════════════════════════════════════════
#How To Use?:


# Set a new URL for version checking
#set_url("https://raw.githubusercontent.com/ribkix/testr/main/AutoUpdateTest.txt")

# Get the latest version information
#latest_version = get_latest_version()

# Set the current version of the program
#set_current_version("0.0.1")

# Check if the program is up to date
#if is_up_to_date():
#    print("The program is up to date!")
#else:
#    print("A new version is available. Downloading...")

    # Download and install the new version
#    download("new_version.py")
#    print("The program has been successfully updated to the latest version.")
#═══════════════════════════════════════════════════════════════════════════════════════


#            ╔═════════════════════════HaZaRd═════════════════════════════╗
#            ║        Youtube: https://www.youtube.com/@IIIHaZaRd         ║
#            ║        Github: https://github.com/Pytholearn               ║
#            ║        Discord: https://discord.gg/YU7jYRkxwp              ║
#            ╚════════════════════════════════════════════════════════════╝
