from model.contact import Contact
from model.date import Date

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact("TIMMY"), Date("20", "March","1990"), Date("20", "June","2000"))

    app.contact.delete_contact()

