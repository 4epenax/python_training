# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new"))
    old_groups = app.group.get_group_list()
    group = Group(name="tg change", header="hg change", footer="fg change")
    group.id = old_groups[0].id
    app.group.open_groups_page()
    app.group.selected_first_group()
    app.group.edit()
    app.group.fill_form(group)
    app.group.submit_modification()
    app.group.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
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
