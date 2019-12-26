from model.contact import Contact
import re

def test_full_contact(app, db):
    contact_from_homepage = sorted(app.contact.get_contact_list(), key = Contact.id_or_max)#[index]
    contact_from_bd = sorted(db.get_contact_list(), key = Contact.id_or_max)
    for i in range(len(contact_from_homepage)):
        assert contact_from_homepage[i].firstname == contact_from_bd[i].firstname.strip()
        assert contact_from_homepage[i].lastname == contact_from_bd[i].lastname.strip()
        assert contact_from_homepage[i].address == contact_from_bd[i].address
        assert contact_from_homepage[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_bd[i])
        assert contact_from_homepage[i].all_email_from_home_page == merge_email_like_on_home_page(contact_from_bd[i])

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_home_page (contact):
    return "\n".join(filter(lambda x: x is not None and x !="", [contact.email, contact.email2, contact.email3]))

# def test_phones_on_home_page(app, db):
#     index = randrange(len(app.contact.get_contact_list()))
#     contact_from_homepage = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_list_from_edit_page(index)
#     assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_list_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_list_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
