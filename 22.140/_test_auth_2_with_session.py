# -*- coding:utf-8 -*-
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
r1 = s.get(url)
print(r1)
print(r1.text)

#另一种写法，这里是为了回复一个读者提问增加的
r2=requests.get(url,headers={"Authorization":r.json()["token"]})
print(r2)
print(r2.text)