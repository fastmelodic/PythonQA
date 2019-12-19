# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import  Date
import pytest


@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact, Date("20", "March", "1990"), Date("20", "June", "2000"))
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_1contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname = "tim", middlename = "Share", lastname = "L", nickname = "popa", title = "RAZ", company = "TANDIR", email = "dpd@mail.com")
#     app.contact.create(contact, Date("20", "March", "1990"), Date("20", "June", "2000"))
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






