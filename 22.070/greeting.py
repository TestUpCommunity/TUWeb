import hug
@hug.get('/greet/{event}')
def greet(event: str):
    greetings = "Happy"
    if event == "Christmas":
        greetings = "Merry"
    if event == "Kwanzaa":
        greetings = "Joyous"
    if event == "wishes":
        greetings = "Warm"
    return f"{greetings} {event}!"

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)