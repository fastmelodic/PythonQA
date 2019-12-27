from model.contact import Contact
from model.groups import Group
from model.date import Date
import random


def test_add_contact_to_group(app,db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("oOo"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("TIMMY"), Date("20", "March", "1990"), Date("20", "June", "2000"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_in_group_by_id(contact.id,group.id)
    assert contact in orm.get_contacts_in_group(group = group)