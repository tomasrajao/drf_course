import requests

endpoint = 'http://127.0.0.1:8000/api/'

get_response = requests.get(endpoint, params={"abc": "123"}, json={"message": "Hi, there."})

# print(get_response.status_code)
print(get_response.json())
