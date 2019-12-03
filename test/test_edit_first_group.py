from model.groups import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("oOo"))
    app.group.edit_group(Group(name ='New name'))

