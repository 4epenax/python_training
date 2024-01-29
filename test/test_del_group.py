from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new"))
    app.group.open_groups_page()
    app.group.selected_first_group()
    app.group.submit_deletion()
    app.group.return_to_groups_page()
