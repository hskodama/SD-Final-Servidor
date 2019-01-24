import json
import requests

# Ton to be sent
datas = {'vCPUs':50, 'RAM':100, 'HD':400}

url = "http://127.0.0.1:5000/customer_request"

files = [
    ('datas', ('datas', json.dumps(datas), 'application/json')),
]

r = requests.post(url, files=files)
print(str(r.content))