# -*- coding: gbk -*-
import requests

#��½��ȡtoken
url = 'http://localhost:8000/oauth/2.0/token'
r = requests.post(url,data={"client_id":"Va5yQRHlA4Fq5eR3LT0vuXV4","client_secret":"0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2",
                           "grant_type":"client_credentials"})
print(r)
print(r.text)

#���ýӿ�
url = 'http://localhost:8000/text2audio'
token = r.json()['access_token']
tex = "������ǰ���ɱ�����˳��������·���γ·���㴦���࣬�����׶����ʻ���T3��վ¥ ȥ�� ��������������·36��ϲ���Ǵ�Ƶ�(���������)"

#�ô����token���ýӿ�
payload =  {'tok': "fail", 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1}
r = requests.post(url,data=payload)
print(r)
print(r.text)

#����ȷtoken���ýӿ�
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1}
r = requests.post(url,data=payload)
print(r)
print(r.text)

#�ô���Ĳ������ýӿڣ��˴���©һ���������ctp
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh'}
r = requests.post(url,data=payload)
print(r)
print(r.text)

#�ô���Ĳ������ýӿڣ��˴�ctp���˲������ֵ2
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 2}
r = requests.post(url,data=payload)
print(r)
print(r.text)