def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.selected_first_group()
    app.group.submit_deletion()
    app.group.return_to_groups_page()
    app.session.logout()
