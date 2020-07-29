import requests
url = 'http://localhost:8000/token_generation'
payload = {
    "username":"User2",
    "password":"Mypassword"
}
r = requests.post(url,data=payload)
print(r)
print(r.text)

s=requests.Session()
s.headers["Authorization"]=r.json()["token"]
url = 'http://localhost:8000/token_authenticated'
r = s.get(url)
print(r)
print(r.text)