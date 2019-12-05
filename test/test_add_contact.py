# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import  Date


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_form(Contact(firstname = "tim", middlename = "Share", lastname = "L", nickname = "popa", title = "RAZ", company = "TANDIR", email = "dpd@mail.com"), Date("20", "March","1990"), Date("20", "June","2000"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)






