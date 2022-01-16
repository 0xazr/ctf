#!/usr/bin/env python

import requests
import base64
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org/' % username

encoded = "3d3d516343746d4d6d6c315669563362"
secret = base64.b64decode(bytearray.fromhex(encoded).decode()[::-1]).decode('utf-8')

payload = {'secret': secret, 'submit': 'Submit+Query'}
r = requests.post(url, auth=(username, password), data=payload)

password = re.findall('(?<=natas9\sis\s)(.*)', r.text)[0]

print(password)