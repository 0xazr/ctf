#!/usr/bin/env python

import requests
import re

username = 'natas0'
password = username

url = 'http://%s.natas.labs.overthewire.org/' % username

r = requests.get(url, auth=(username, password))

password = re.findall('(?<=natas1\sis\s)(.*)(?=\s-->)', r.text)[0]

print(password)