# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.group.open_groups_page()
    app.group.selected_first_group()
    app.group.edit()
    app.group.fill_form(Group(name="tg change", header="hg change", footer="fg change"))
    app.group.submit_modification()
    app.group.return_to_groups_page()


def test_modify_group_name(app):
    app.group.open_groups_page()
    app.group.selected_first_group()
    app.group.edit()
    app.group.fill_form(Group(name="New group"))
    app.group.submit_modification()
    app.group.return_to_groups_page()
