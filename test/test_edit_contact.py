from model.contact import Contact
from model.date import Date
import random


def test_edit_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("TIMMY"), Date("20", "March", "1990"), Date("20", "June", "2000"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index =  old_contacts.index(contact)
    new_value_contact = Contact(id = contact.id, firstname = "xxx", lastname = "xxx", nickname = "xxx", title = "RxxxAZ", company = "xxx", email = "XXX@mail.com")
    app.contact.edit_contact_by_id(contact.id, new_value_contact, Date("1", "March", "1880"), Date("2", "March", "2333"))
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_value_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(lambda x: Contact(id=x.id, firstname=x.firstname.strip(), lastname=x.lastname.strip()), db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
