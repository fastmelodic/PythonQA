from model.contact import Contact
from model.groups import Group
from model.date import Date
import random


def test_delete_contact_from_group(app,db,orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("oOo"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("TIMMY"), Date("20", "March", "1990"), Date("20", "June", "2000"))
    groups_with_contacts = []
    for g in db.get_group_list():
        if len(orm.get_contacts_in_group(g)) >= 1:
            groups_with_contacts.append(g)
    if len(groups_with_contacts) == 0:
        contact = random.choice(db.get_contact_list())
        group = random.choice(db.get_group_list())
        app.contact.add_contact_in_group_by_id(contact.id, group.id)
        groups_with_contacts.append(group)
    contact_in_group = orm.get_contacts_in_group(groups_with_contacts[0])[0]
    app.contact.delete_contact_from_group_by_id(contact_in_group.id, groups_with_contacts[0].id)
    assert contact_in_group not in orm.get_contacts_in_group(groups_with_contacts[0])
    assert contact_in_group in orm.get_contacts_not_in_group(groups_with_contacts[0])