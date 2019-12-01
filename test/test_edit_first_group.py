from model.groups import Group

def test_edit_first_group(app):
    app.group.edit_group(Group(name ='New name'))

