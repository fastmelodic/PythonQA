# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import  Date


def test_add_contact(app):

    app.contact.fill_form(Contact(firstname = "tim", middlename = "Share", lastname = "L", nickname = "popa", title = "RAZ", company = "TANDIR", email = "dpd@mail.com"), Date("20", "March"), Date("20", "June"))







