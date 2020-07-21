import requests
payload={"name":"zhangsan","age":18}
r=requests.put("http://localhost:8000/hello_user",json=payload)
print(r.status_code)
print(r.text)