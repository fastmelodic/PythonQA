from model.groups import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name ='xx', header ='xx', footer ='xx'))
    app.session.logout()
