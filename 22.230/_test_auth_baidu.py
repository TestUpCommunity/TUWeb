# -*- coding: gbk -*-
from rest_client import RestClient #�����˰�rest_client.py���ϼ�Ŀ¼���뵽pythonpath��ȥ��
import requests
#��½��ȡtoken
rest_client=RestClient(client_id="Va5yQRHlA4Fq5eR3LT0vuXV4",client_secret="0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2")
#���ýӿ�

token = rest_client.token
print(f"�����Ѿ�Ĭ�ϵ����ˣ�token={token}")
rest_client.logout()
token = rest_client.token
print(f"�����Ѿ��ǳ��ˣ�token={token}")
rest_client.login(client_id="Va5yQRHlA4Fq5eR3LT0vuXV4",client_secret="0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2")
token = rest_client.token
print(f"�����Ѿ��ֶ��ǳ��ˣ�token={token}")

tex = "������ǰ���ɱ�����˳��������·���γ·���㴦���࣬�����׶����ʻ���T3��վ¥ ȥ�� ��������������·36��ϲ���Ǵ�Ƶ�(���������)"

#�ô����token���ýӿ�
payload =  {'tok': "fail", 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1}
r = rest_client.post(url='/text2audio',data=payload)
print(r)
print(r.text)

#����ȷtoken���ýӿ�
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1}
r = rest_client.post(url='/text2audio',data=payload)
print(r)
print(r.text)

#�ô���Ĳ������ýӿڣ��˴���©һ���������ctp
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh'}
r = rest_client.post(url='/text2audio',data=payload)
print(r)
print(r.text)

#�ô���Ĳ������ýӿڣ��˴�ctp���˲������ֵ2
payload =  {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 2}
r = rest_client.post(url='/text2audio',data=payload)
print(r)
print(r.text)