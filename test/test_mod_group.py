# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new"))
    old_groups = db.get_group_list()
    groups = random.choice(old_groups)
    group = Group(name="tg change", header="hg change", footer="fg change")
    group.id = groups.id
    app.group.open_groups_page()
    app.group.selected_group_by_id(groups.id)
    app.group.edit()
    app.group.fill_form(group)
    app.group.submit_modification()
    app.group.return_to_groups_page()
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[old_groups.index(groups)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                 key=Group.id_or_max)
