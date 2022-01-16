#!/usr/bin/env python

import requests
import re

username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = 'http://%s.natas.labs.overthewire.org/' % username

r = requests.get(url, auth=(username, password))

password = re.findall('(?<=natas2\sis\s)(.*)(?=\s-->)', r.text)[0]

print(password)