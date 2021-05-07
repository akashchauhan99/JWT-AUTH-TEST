import requests

# THIS IS TO TEST THE AUTHENTICATION
headers = {}
headers['Authorization'] = 'Bearer --PASTE YOUR ACCESS(TOKEN VALUE) HERE--'
r = requests.get('http://127.0.0.1:8000/paradigm/', headers=headers)
print(r.text)