# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Temp"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.open_home_page()
    app.contact.select_contact_by_id(contact.id)
    app.contact.submit_deletion()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
