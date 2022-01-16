import requests

url = 'http://mercury.picoctf.net:28916/'

req = requests.head(url)

print(req.headers['flag'])