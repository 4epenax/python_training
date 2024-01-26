def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_home_page()
    app.contact.select_first_contact()
    app.contact.submit_deletion()
    app.session.logout()
