#!/usr/bin/env python

import requests
import re
import base64

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % username

r = requests.get(url, auth=(username, password))

print(r.text)