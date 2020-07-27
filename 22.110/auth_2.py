import hug

class APIUser(object):
    """A minimal example of a rich User object"""

    def __init__(self, user_id, api_key):
        self.user_id = user_id
        self.api_key = api_key


def api_key_verify(api_key):
    magic_key = "5F00832B-DE24-4CAF-9638-C10D1C642C6C"  # Obviously, this would hit your database
    if api_key == magic_key:
        # Success!
        return APIUser("user_foo", api_key)
    else:
        # Invalid key
        return None

api_key_authentication = hug.authentication.api_key(api_key_verify)


@hug.get("/key_authenticated", requires=api_key_authentication)  # noqa
def basic_auth_api_call(user: hug.directives.user):
    return "Successfully authenticated with user: {0}".format(user.user_id)

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)