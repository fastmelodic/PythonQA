from model.groups import Group
from random import randrange

def test_edit_rand_group(app):
    if app.group.count() == 0:
        app.group.create(Group("oOo"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name ='New name')
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    old_groups[index] = group
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

