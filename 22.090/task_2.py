import hug

@hug.put(output=hug.output_format.json)
def hello_user(name,age):
    return {name:age}

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)