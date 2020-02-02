import random
from pytest_bdd import when, then, given
from model.contact import Contact
from model.date import  Date

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <name>, <last>')
def new_contact(name, last):
    return Contact(firstname = name, lastname = last)

@when('add new contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact, Date("20", "March", "1990"), Date("20", "June", "2000"))

@then('the new contact list is equal to the old list with new contact')
def verify_contact_added(check_ui, contact_list, db, app, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(lambda x: Contact(id=x.id, firstname=x.firstname.strip(), lastname=x.lastname.strip()),
                           db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("TIMMY"), Date("20", "March", "1990"), Date("20", "June", "2000"))
    return db.get_contact_list()

@given('a random contact from list')
def random_contact_from_list(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('modify the chosen contact with a new values <name>, <last>')
def modify_contact(random_contact_from_list, app, name, last):
    new_contact = random_contact_from_list
    new_contact.firstname = name
    new_contact.lastname = last
    app.contact.edit_contact_by_id(new_contact.id ,new_contact, Date("1", "March", "1880"),
                                   Date("2", "March", "2333"))
    return new_contact

@then('the new contact list is equal to the old list with modified contact')
def verify_contact_edited(db, non_empty_contact_list, check_ui, random_contact_from_list, name, last, app):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    new_contact = random_contact_from_list
    new_contact.firstname = name
    new_contact.lastname = last
    old_contacts[old_contacts.index(random_contact_from_list)] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(lambda x: Contact(id=x.id, firstname=x.firstname.strip(), lastname=x.lastname.strip()),
                           db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

@when('delete the random contact')
def delete_rnd_contact(app, random_contact_from_list):
    app.contact.delete_contact_by_id(random_contact_from_list.id)

@then('the new contact list is equal to the old list without deleted contact')
def verify_delete_contact(db, app, check_ui, non_empty_contact_list, random_contact_from_list):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact_from_list)
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = map(lambda x: Contact(id=x.id, firstname=x.firstname.strip(), lastname=x.lastname.strip()),
                           db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)