import random
from model.groups import Group
from pytest_bdd import when, then, given

@given('a group list')
def group_list(db):
    return db.get_group_list()

@given('a group witn <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name = name, header = header, footer = footer)

@when('add a new group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, new_group, group_list):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("oOo"))
    return db.get_group_list()

@given('a random group from list')
def random_group(group_list):
    return random.choice(group_list)

@when('i delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then('the new group list is equal to the old list without deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert old_groups == new_groups