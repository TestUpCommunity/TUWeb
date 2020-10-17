from jinja2 import Template
template = Template('Hello {{ name }}!')
print(template.render(name='World'))
print(template.render(name='John Doe'))
