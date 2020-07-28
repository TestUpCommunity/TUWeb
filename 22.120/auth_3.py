import hug
import jwt


def token_verify(token):
    secret_key = "super-secret-key-please-change"
    try:
        return jwt.decode(token, secret_key, algorithm="HS256")
    except jwt.DecodeError:
        return False

token_key_authentication = hug.authentication.token(token_verify)


@hug.get("/token_authenticated", requires=token_key_authentication)  # noqa
def token_auth_call(user: hug.directives.user):
    return "You are user: {0} with data {1}".format(user["user"], user["data"])


@hug.post("/token_generation")  # noqa
def token_gen_call(username, password):
    """Authenticate and return a token"""
    secret_key = "super-secret-key-please-change"
    mockusername = "User2"
    mockpassword = "Mypassword"
    if mockpassword == password and mockusername == username:  # This is an example. Don't do that.
        return {
            "token": jwt.encode({"user": username, "data": "mydata"}, secret_key, algorithm="HS256")
        }
    return "Invalid username and/or password for user: {0}".format(username)

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)