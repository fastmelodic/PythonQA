from model.contact import Contact
from model.date import Date

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact("TIMMY"), Date("20", "March","1990"), Date("20", "June","2000"))
    app.contact.edit_contact(Contact(firstname = "xxx", lastname = "xxx", nickname = "xxx", title = "RxxxAZ", company = "xxx", email = "XXX@mail.com"), Date("1", "March", "1880"), Date("2", "March", "2333"))

