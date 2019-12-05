# -*- coding: utf-8 -*-
from model.groups import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name ='123', header ='321', footer ='4456'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name ='', header ='', footer =''))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

