from model.group import Group
import random


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.open_groups_page()
    app.group.selected_group_by_id(group.id)
    app.group.submit_deletion()
    app.group.return_to_groups_page()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
