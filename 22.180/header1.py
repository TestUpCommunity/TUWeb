import hug


@hug.post("/hello")
def hello(request):
    if request.headers.get('USER'):
        return "hello " + request.headers['USER']
    return "hello "


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)

