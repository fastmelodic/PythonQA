from model.groups import Group
import random

def test_edit_rand_group(app,db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("oOo"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_value_group = Group(name ="LOLO", id=group.id)
    app.group.edit_group_by_id(group.id,new_value_group)
    old_groups[index] = new_value_group
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

