import hug

sessions={}
class MockSession():
    def __init__(self):
        self.session_id ="5F00832B-DE24-4CAF-9638-C10D1C642C6C"

    def get_session_id(self):
        return self.session_id


@hug.post("/authenticated")
def cookie_api_call(request,response):
    session_id = request.cookies.get('session-id')
    if sessions.get(session_id):
        for k,v in request.cookies.items():
            response.set_cookie(k, v,domain="127.0.0.1", secure=False)
        return f"Successfully authenticated user={sessions[session_id].user}"
    else:
        return "Not authenticated"

@hug.post("/login")
def login(username, password, response):
    mockusername = "user4"
    mockpassword = "pwd"
    if mockpassword == password and mockusername == username:
        my_session = MockSession()
        my_session.user = username
        session_id= my_session.get_session_id()
        sessions[session_id]=my_session
        response.set_cookie('session-id', session_id,domain="127.0.0.1",secure=False)
        return {"status": "success" }
    return {"status": "fail","info":"Invalid username and/or password for user: {0}".format(username) }

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)

