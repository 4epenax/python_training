def test_all_main_info_on_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert contacts_from_home_page == contacts_from_db
