# -*- coding: gbk -*-
import hug


@hug.get("/polls",output=hug.output_format.html)
def polls():
    return "Hello, world. You're at the polls index."

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
