import requests
import json

URL = 'http://127.0.0.1:8000/createemp/'

data = {
    'name':'Code Sode',
    'salary':4567890,
    'city':'Rewa'
}
print(data)

json_data = json.dumps(data)
print(json_data)
r = requests.post(url= URL, data=json_data)

data = r.json()
print(data)

 