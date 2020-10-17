from jinja2 import Template

class CommonItem:
    pass
data=CommonItem()
data.name = "Python"

template = Template("Hello {{ data['name'] }}!")
print(template.render(data=data))
template = Template("Hello {{ data.name}}!")
print(template.render(data=data))


