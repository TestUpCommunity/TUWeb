import requests
s = requests.Session()
#part 1
url = 'http://127.0.0.1:8000/authenticated'
r = s.post(url)
print(r)
print(r.text)
print(r.cookies.get('session-id'))
print(s.cookies.get('session-id'))

#part 2
url = 'http://127.0.0.1:8000/login'
payload = {
    "username":"user4",
    "password":"pwd"
}
r = s.post(url,data=payload)
print(r)
print(r.text)
print(r.cookies.get('session-id'))
print(s.cookies.get('session-id'))

#part 3
url = 'http://127.0.0.1:8000/authenticated'
r = s.post(url,data=payload)
print(r)
print(r.text)
print(r.cookies.get('session-id'))
print(s.cookies.get('session-id'))
