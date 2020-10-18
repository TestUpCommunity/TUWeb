from jinja2 import Template
source = """
{% if users %}
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% endfor %}
</ul>
{% endif %}
"""
class CommonItem:
    pass

user1=CommonItem()
user2=CommonItem()
user1.username = "WORLD"
user2.username = "PYHONIC&"

template = Template(source)
print(template.render(should_be_users=[user1,user2]))
# print(template.render(users=[user1,user2]))