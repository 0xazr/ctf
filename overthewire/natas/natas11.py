#!/usr/bin/env python

import requests
import re
import base64

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' % username
cookies = {'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}

r = requests.get(url, auth=(username, password), cookies=cookies)

print(re.findall('The password for natas12 is (.*)\<br\>', r.text)[0])