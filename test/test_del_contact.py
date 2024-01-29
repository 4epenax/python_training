# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Temp"))
    app.contact.open_home_page()
    app.contact.select_first_contact()
    app.contact.submit_deletion()
