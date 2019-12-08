# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import  Date


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname = "tim", middlename = "Share", lastname = "L", nickname = "popa", title = "RAZ", company = "TANDIR", email = "dpd@mail.com")
    app.contact.fill_form(contact, Date("20", "March","1990"), Date("20", "June","2000"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






