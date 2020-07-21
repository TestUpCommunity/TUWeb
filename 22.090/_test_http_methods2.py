import requests
payload={"name":"zhangsan","age":18}
r=requests.post("http://localhost:8000/hello_user",data=payload)
print(r.status_code)
print(r.text)

r=requests.post("http://localhost:8000/hello_user?name=zhangsan&age=20")
print(r.status_code)
print(r.text)

payload={"age":18}
r=requests.post("http://localhost:8000/hello_user?name=zhangsan",data=payload)
print(r.status_code)
print(r.text)