# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="tg change", header="hg change", footer="fg change")
    group.id = old_groups[index].id
    app.group.open_groups_page()
    app.group.selected_group_by_index(index)
    app.group.edit()
    app.group.fill_form(group)
    app.group.submit_modification()
    app.group.return_to_groups_page()
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="new"))
#     old_groups = app.group.get_group_list()
#     app.group.open_groups_page()
#     app.group.selected_first_group()
#     app.group.edit()
#     app.group.fill_form(Group(name="New group"))
#     app.group.submit_modification()
#     app.group.return_to_groups_page()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
