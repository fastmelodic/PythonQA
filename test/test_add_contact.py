# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import  Date



def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact, Date("20", "March", "1990"), Date("20", "June", "2000"))
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(lambda x: Contact(id=contact.id, firstname=x.firstname.strip(), lastname=x.lastname.strip()), db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)







