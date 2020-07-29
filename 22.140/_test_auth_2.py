import requests
url = 'http://localhost:8000/token_generation'
payload = {
    "username":"User2",
    "password":"Mypassword"
}
r = requests.post(url,data=payload)
print(r)
print(r.text)

url = 'http://localhost:8000/token_authenticated'
r = requests.get(url,headers={"Authorization":r.json()["token"]})
print(r)
print(r.text)



