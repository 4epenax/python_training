# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Temp"))
    old_contacts = app.contact.get_contact_list()
    app.contact.open_home_page()
    app.contact.select_first_contact()
    app.contact.submit_deletion()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
