from jinja2 import Template
template = Template('Hello {{ name }}!')
print(template.render(name='World'))
print(template.render(name='John Doe'))


template = Template('Hello {{ name }} and {{ name2 }}!')
print(template.render(name='World',name2='John Doe'))
print(template.render({'name':'python','name2':'study'}))