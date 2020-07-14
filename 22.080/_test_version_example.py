import requests

for _ in range(1,5):
    r=requests.get(f"http://localhost:8000/v{_}/echo?text=%E4%BD%A0%E5%A5%BD")
    print(r.status_code)
    print(r.text)