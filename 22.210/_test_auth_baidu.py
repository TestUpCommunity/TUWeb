import requests

#case 1
url = 'http://localhost:8000/oauth/2.0/token'
r = requests.get(url)
print(r)
print(r.text)

#case 2
url = 'http://localhost:8000/oauth/2.0/token'
r = requests.get(url,data={"client_id":"Va5yQRHlA4Fq5eR3LT0vuXV4","client_secret":"0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2",
                           "grant_type":"client_credentials"})
print(r)
print(r.text)

#case 3
url = 'http://localhost:8000/oauth/2.0/token'
r = requests.post(url,data={"client_id":"Va5yQRHlA4Fq5eR3LT0vuXV4","client_secret":"0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2",
                           "grant_type":"client_credentials"})
print(r)
print(r.text)