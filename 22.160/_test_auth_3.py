import requests
url = 'http://localhost:8000/key_authenticated'
r = requests.get(url)
print(r)
print(r.text)

url = 'http://localhost:8000/key_authenticated'
r = requests.get(url,headers={"X-Api-Key":"5F00832B-DE24-4CAF-9638-C10D1C642C6C"})
print(r)
print(r.text)