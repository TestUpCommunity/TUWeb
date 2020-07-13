import hug
@hug.get('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
    return f"Happy {name} Birthday {age}!"


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)