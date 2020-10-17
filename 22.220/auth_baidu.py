# -*- coding: gbk -*-
import hug,falcon

@hug.post("/oauth/2.0/token", output=hug.output_format.json)
@hug.get("/oauth/2.0/token", output=hug.output_format.json)
def get_oauth_token(client_id,client_secret,grant_type):
    magic_client_secret = "0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2"
    magic_client_id = "Va5yQRHlA4Fq5eR3LT0vuXV4"
    if client_id == magic_client_id and client_secret == magic_client_secret and grant_type == "client_credentials":
        # Success!
        return {
  "refresh_token": "25.b55fe1d287227ca97aab219bb249b8ab.315360000.1798284651.282335-8574074",
  "expires_in": 2592000,
  "scope": "public wise_adapt",
  "session_key": "9mzdDZXu3dENdFZQurfg0Vz8slgSgvvOAUebNFzyzcpQ5EnbxbF+hfG9DQkpUVQdh4p6HbQcAiz5RmuBAja1JJGgIdJI",
   # ���������access tokenӦ����ͨ���㷨��secret key���������
  "access_token": "24.6c5e1ff107f0e8bcef8c46d3424a0e78.2592000.1485516651.282335-8574074",
  "session_secret": "dfac94a3489fe9fca7c3221cbf7525ff"
}

    elif client_id != magic_client_id:
        # Invalid client id
        return {
            "error": "invalid_client",
            "error_description": "unknown client id"
        }

    elif client_secret != magic_client_secret: # Invalid client secret
        return {
            "error": "invalid_client",
            "error_description": "Client authentication failed"
        }
    else:
        return None # grant_type not match




@hug.post("/text2audio")
@hug.get("/text2audio")
def text2audio(body,response):

    access_token = body.get('tok')#��get��ֹ�ͻ���û��tok��ʱ�����˳����﷨����
    #�������д����tokenӦ���Ǵ����ݿ���������ģ��˴�д��ֻ��Ϊ�˼��ʾ�⡣
    if access_token != "24.6c5e1ff107f0e8bcef8c46d3424a0e78.2592000.1485516651.282335-8574074":
        response.status = falcon.HTTP_502 #�����������falcon�Դ���
        return {"err_no":502, "err_msg":"auth failed.","sn":"abcdefgh","idx":1} #������Ϣ���չٷ��ĵ���500������Ϣ���
    #��������û�����У��
    if (body.get('tex') and body.get('cuid') and body.get('ctp') and body.get('lan')) == None:
        response.status = falcon.HTTP_501
        return {"err_no":501, "err_msg":"input param incorrect.","sn":"abcdefgh","idx":2}
    #�������У��
    if len(body['tex'])>2048 or len(body['cuid'])>60 or len(body['ctp'])!=1 or len(body['lan'])!='zh':
        response.status = falcon.HTTP_501
        return {"err_no": 501, "err_msg": "input param incorrect.", "sn": "abcdefgh", "idx": 2}
    #ѡ�����У��,��д��һ����Ϊ���ӣ�ʣ�µ�������Լ�����ϰ��
    if body.get('spd') and body.get('spd') not in range(0,16):
        response.status = falcon.HTTP_501
        return {"err_no": 501, "err_msg": "input param incorrect.", "sn": "abcdefgh", "idx": 2}


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)