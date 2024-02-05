from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new"))
    old_groups = app.group.get_group_list()
    app.group.open_groups_page()
    app.group.selected_first_group()
    app.group.submit_deletion()
    app.group.return_to_groups_page()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
