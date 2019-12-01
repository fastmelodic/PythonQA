from model.contact import Contact
from model.date import Date

def test_edit_first_contact(app):

    app.contact.edit_contact(Contact(firstname = "xxx", middlename = "xxx", lastname = "xxx", nickname = "xxx", title = "RxxxAZ", company = "xxx", email = "XXX@mail.com"), Date("1", "March"), Date("2", "March"))

