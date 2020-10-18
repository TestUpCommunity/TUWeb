from jinja2 import Template
source = """
<h1>Members</h1>
<ul>
{% for user in users %}
  <li>{{ user.username|e }}</li>
{% endfor %}
</ul>
"""
class CommonItem:
    pass

user1=CommonItem()
user2=CommonItem()
user1.username = "WORLD"
user2.username = "PYHONIC&"
template = Template(source)
print(template.render(users=[user1,user2]))


