# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.open_groups_page()
    app.group.init_group_creation()
    app.group.fill_form(Group(name="tg", header="hg", footer="fg"))
    app.group.submit_group_creation()
    app.group.return_to_groups_page()


def test_add_empty_group(app):
    app.group.open_groups_page()
    app.group.init_group_creation()
    app.group.fill_form(Group(name="", header="", footer=""))
    app.group.submit_group_creation()
    app.group.return_to_groups_page()
