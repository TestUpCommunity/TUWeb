# -*- coding: gbk -*-
from jinja2 import Environment,FileSystemLoader

class CommonItem:
    def load_html(self,html,folder,data=None):
        env = Environment(loader=FileSystemLoader(folder))
        result = env.get_template(html).render(data=data)
        return result


if __name__ == "__main__":
    import os
    data = CommonItem()
    data.title = "我是标题"
    data.body = "我是内容"
    item = CommonItem().load_html("example.html",
                                  os.path.dirname(os.path.realpath(__file__)),
                                  data=data)
    print(item)
    with open("rendered_example.html","w") as f:
        f.write(item)