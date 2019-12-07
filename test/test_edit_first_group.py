from model.groups import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("oOo"))
    old_groups = app.group.get_group_list()
    group = Group(name ='New name')
    group.id = old_groups[0].id
    app.group.edit_group(group)
    old_groups[0] = group
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

