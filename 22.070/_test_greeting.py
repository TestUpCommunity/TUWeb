import requests
r=requests.get("http://localhost:8000/greet/Christmas")
print(r.status_code)
print(r.text)