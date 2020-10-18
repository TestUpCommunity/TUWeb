from jinja2 import Template
source = """
<dl>
{% for key, value in my_dict.items() %}
    <dt>{{ key|e }}</dt>
    <dd>{{ value|e }}</dd>
{% endfor %}
</dl>
"""


template = Template(source)
print(template.render(my_dict={"name1":"WORLD","name2":"PYTHONIC"}))


