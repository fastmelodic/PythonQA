# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import  Date
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join(random.choice(symbols) for x in range(random.randrange(maxlen)))

testdata = [Contact(firstname = "", middlename = "", lastname = "", nickname = "", homephone = "", mobilephone = "", workphone = "", secondaryphone = "", address = "", title = "",
                    company = "", email ="" , email2 ="", email3 = "")] + [
    Contact(
        firstname = random_string("firstname", 15), middlename = random_string("middlename", 15), lastname = random_string("lastname", 15), nickname = random_string("nickname", 5),
        homephone = random_string("homephone", 10), mobilephone = random_string("mobilephone", 10), workphone = random_string("workphone", 10), secondaryphone = random_string("secondaryphone", 10),
        address = random_string("address", 15), title = random_string("title", 5), company = random_string("company", 10), email = random_string("email", 10), email2 = random_string("email2", 10),
        email3 = random_string("email3", 10)
    )
    for i in range(5)
]

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






