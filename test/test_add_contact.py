# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t1", company="c2",
                      address="a3", homephone="hp", mobilephone="mp", workphone="wp", fax="f4", email="el",
                      email2="el2", email3="e3", ayear="2020")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
