# -*- coding: utf-8 -*-
from model.groups import Group
import random

def test_delete_rand_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("oOo"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    def clean(group):
        return Group(id = group.id, name = group.name.strip())
    if check_ui:
        new_groups = map(clean, db.get_group_list())
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)


