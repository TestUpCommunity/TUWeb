import hug

@hug.get('/helloworld')
def helloworld():
    return "hello world!"

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)