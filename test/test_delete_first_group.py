# -*- coding: utf-8 -*-
from model.groups import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("oOo"))
    app.group.delete_group()


