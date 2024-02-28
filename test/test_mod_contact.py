# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Temp"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contacts = Contact(firstname="fn change", middlename="mn change", lastname="ln change",
                      nickname="nn change", title="t1 change", company="c2 change",
                      address="a3 change", homephone="hp change", mobilephone="mp change",
                      workphone="wp change", fax="f4 change", email="el change",
                      email2="el2 change", email3="e3 change", homepage="hp change", bday="18",
                      bmonth="August", byear="1985", aday="9", amonth="April", ayear="2011")
    contacts.id = contact.id
    app.contact.open_home_page()
    app.contact.edit_contact_by_id(contact.id)
    app.contact.fill_contact_form(contacts)
    app.contact.update_contact()
    app.contact.return_to_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts = new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
