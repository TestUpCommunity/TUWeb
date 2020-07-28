import hug
authentication = hug.authentication.basic(hug.authentication.verify("user1", "mypassword"))


@hug.get("/public")
def public_api_call():
    return "Needs no authentication"

@hug.get("/authenticated", requires=authentication)
def basic_auth_api_call(user: hug.directives.user):
    return "Successfully authenticated with user: {0}".format(user)


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)