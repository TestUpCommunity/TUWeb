import requests
s=requests.Session()
r=s.get("http://localhost:8000/public")
print(r)
print(r.text)

r=s.get("http://localhost:8000/authenticated")
print(r)
print(r.text)

error_pwd="mypasswordx"# fail
usr,pwd="user1", "mypassword" # pass

s.auth = usr,pwd #1:pass
r=s.get("http://localhost:8000/authenticated")
print("1:pass")
print(r)
print(r.text)

s.auth = None # 2:fail
r=s.get("http://localhost:8000/authenticated")
print("2:fail")
print(r)
print(r.text)

s.auth = usr,error_pwd # 3:fail
r=s.get("http://localhost:8000/authenticated")
print("3:fail")
print(r)
print(r.text)


s.auth = None #4:pass
r=s.get(f"http://{usr}:{pwd}@localhost:8000/authenticated")
print("4:pass")
print(r)
print(r.text)

import base64
s.auth = None  #5:pass
raw=f"{usr}:{pwd}"
encoded = base64.b64encode(raw.encode("utf-8")).decode("utf-8")
s.headers["Authorization"] = f"Basic {encoded}"
r=s.get("http://localhost:8000/authenticated")
print("5:pass")
print(r)
print(r.text)
