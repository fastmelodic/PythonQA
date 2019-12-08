from model.contact import Contact
from model.date import Date

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact("TIMMY"), Date("20", "March","1990"), Date("20", "June","2000"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[:1] = []
    assert old_contacts == new_contacts
