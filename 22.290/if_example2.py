from jinja2 import Template
source = """
<ul>
{% for user in users %}
    {% if user.username=="WORLD" %}
    <li>Hello {{ user.username|e }}</li>
    {% elif user.username=="PYTHONIC" %}
    <li>I like {{ user.username|e }}</li>
    {% else %}
    <li>It is {{ user.username|e }}</li>
    {% endif %}
{% endfor %}
</ul>
"""
class CommonItem:
    pass

user1=CommonItem()
user2=CommonItem()
user3=CommonItem()
user1.username = "WORLD"
user2.username = "PYTHONIC"
user3.username = "TOM"
template = Template(source)
print(template.render(users=[user1,user2,user3]))
