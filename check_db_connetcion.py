from fixture.orm import ORMFixture
from model.groups import Group
db = ORMFixture(host = "127.0.0.1", name = "addressbook", user = "root", password = "")

try:
    l = db.get_contacts_in_group(Group(id = 217))
    for item in l:
        print(item)
finally:
    pass #connection.close()