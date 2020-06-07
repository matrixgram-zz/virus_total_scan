#!/usr/bin/env python3
import sys
import requests


print(sys.argv)
URL = "https://www.virustotal.com/vtapi/v2/file/scan"
PARAMS = {"apikey": sys.argv[1]}
files = {"files": ("file1.py", open(sys.argv[2], "rb"))}
reponse = requests.post(URL, files=files, params=PARAMS)
print(reponse.json())
