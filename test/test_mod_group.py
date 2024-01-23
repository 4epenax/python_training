# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first(Group(name="tg change", header="hg change", footer="fg change"))
    app.session.logout()
