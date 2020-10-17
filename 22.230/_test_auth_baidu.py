# -*- coding: gbk -*-
from rest_client import RestClient #别忘了把rest_client.py的上级目录加入到pythonpath中去。
import requests
#登陆获取token
rest_client=RestClient(client_id="Va5yQRHlA4Fq5eR3LT0vuXV4",client_secret="0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2")
#调用接口

token = rest_client.token
print(f"现在已经默认登入了，token={token}")
rest_client.logout()
token = rest_client.token
print(f"现在已经登出了，token={token}")
rest_client.login(client_id="Va5yQRHlA4Fq5eR3LT0vuXV4",client_secret="0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2")
token = rest_client.token
print(f"现在已经手动登出了，token={token}")

tex = "三分钟前，由北京市顺义区二经路与二纬路交汇处北侧，北京首都国际机场T3航站楼 去往 东城区北三环东路36号喜来登大酒店(北京金隅店)"

#用错误的token调用接口
payload =  {'tok': "fail", 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1}
r = rest_client.post(url='/text2audio',data=payload)
print(r)
print(r.text)

#用正确token调用接口
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1}
r = rest_client.post(url='/text2audio',data=payload)
print(r)
print(r.text)

#用错误的参数调用接口，此处遗漏一个必填参数ctp
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh'}
r = rest_client.post(url='/text2audio',data=payload)
print(r)
print(r.text)

#用错误的参数调用接口，此处ctp传了不允许的值2
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 2}
r = rest_client.post(url='/text2audio',data=payload)
print(r)
print(r.text)