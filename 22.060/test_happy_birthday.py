import requests
r=requests.get("http://localhost:8000/happy_birthday?name=ting&age=18")
print(r.status_code)
print(r.text)