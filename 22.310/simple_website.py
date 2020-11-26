# -*- coding: gbk -*-
from jinja2 import Environment,FileSystemLoader
import hug,falcon
import os

class CommonItem:
    def load_html(self,html,folder,data=None):
        env = Environment(loader=FileSystemLoader(folder))
        result = env.get_template(html).render(data=data)
        return result

@hug.get("/",output=hug.output_format.html)
def homepage():

    data = CommonItem()
    data.title = "我是标题"
    data.body = "我是内容"
    item = CommonItem().load_html("example.html",
                                 os.path.dirname(os.path.realpath(__file__)),
                                 data=data)
    return item



if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
