# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group = Group(name="tg change", header="hg change", footer="fg change")
    group.id = old_groups[0].id
    app.group.open_groups_page()
    app.group.selected_group_by_id(group.id)
    app.group.edit()
    app.group.fill_form(group)
    app.group.submit_modification()
    app.group.return_to_groups_page()
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
