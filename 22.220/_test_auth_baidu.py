# -*- coding: gbk -*-
import requests

#登陆获取token
url = 'http://localhost:8000/oauth/2.0/token'
r = requests.post(url,data={"client_id":"Va5yQRHlA4Fq5eR3LT0vuXV4","client_secret":"0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2",
                           "grant_type":"client_credentials"})
print(r)
print(r.text)

#调用接口
url = 'http://localhost:8000/text2audio'
token = r.json()['access_token']
tex = "三分钟前，由北京市顺义区二经路与二纬路交汇处北侧，北京首都国际机场T3航站楼 去往 东城区北三环东路36号喜来登大酒店(北京金隅店)"

#用错误的token调用接口
payload =  {'tok': "fail", 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1}
r = requests.post(url,data=payload)
print(r)
print(r.text)

#用正确token调用接口
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1}
r = requests.post(url,data=payload)
print(r)
print(r.text)

#用错误的参数调用接口，此处遗漏一个必填参数ctp
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh'}
r = requests.post(url,data=payload)
print(r)
print(r.text)

#用错误的参数调用接口，此处ctp传了不允许的值2
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 2}
r = requests.post(url,data=payload)
print(r)
print(r.text)