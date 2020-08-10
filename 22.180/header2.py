import hug,falcon


@hug.post("/hello2")
def hello2(request,response):
    response.data = {'message': 'Hello world!'}
    response.append_header("token","mock")
    response.status = falcon.HTTP_400
    if request.headers.get('USER'):
        response.headers['token']="mock token"
        return "hello " + request.headers['USER']
    return "hello "


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)

