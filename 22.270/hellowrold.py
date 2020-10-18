from jinja2 import Template
template = Template('Hello {{ name | lower}}!')
print(template.render(name='WORLD'))
print(template.render(name='PYTHON'))


from jinja2 import Template
template = Template("Hello {{ names | join('-')}}!")
print(template.render(names=['WORLD','PYTHON']))



from jinja2 import Template
template = Template('Hello {{ name }}!')
print(template.render(name='WORLD'.lower()))
print(template.render(name='PYTHON'.lower()))


from jinja2 import Template
template = Template("Hello {{ names }}!")
print(template.render(names=('-').join(['WORLD','PYTHON'])))
