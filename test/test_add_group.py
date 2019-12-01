# -*- coding: utf-8 -*-
from model.groups import Group

def test_add_group(app):

    app.group.create(Group(name ='123', header ='321', footer ='4456'))


def test_add_empty_group(app):

    app.group.create(Group(name ='', header ='', footer =''))


