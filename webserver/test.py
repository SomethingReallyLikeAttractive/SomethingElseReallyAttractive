import requests

data = 'love you'
r = requests.post('http://0.0.0.0:5000', data=data)
