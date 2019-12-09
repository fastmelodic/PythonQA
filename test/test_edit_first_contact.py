from model.contact import Contact
from model.date import Date

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("TIMMY"), Date("20", "March", "1990"), Date("20", "June", "2000"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname = "xxx", lastname = "xxx", nickname = "xxx", title = "RxxxAZ", company = "xxx", email = "XXX@mail.com")
    contact.id = old_contacts[0].id
    app.contact.edit_contact(contact, Date("1", "March", "1880"), Date("2", "March", "2333"))
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

