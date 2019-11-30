# -*- coding: utf-8 -*-

from model.groups import Group
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_new_group(Group(name = '123', header = '321', footer = '4456'))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_new_group(Group(name = '', header = '', footer = ''))
    app.session.logout()

