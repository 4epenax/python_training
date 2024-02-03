# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(
        Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t1", company="c2", address="a3",
                homephone="hp", mobilephone="mp", workphone="wp", fax="f4", email="el", email2="el2", email3="e3",
                homepage="hp", bday="13", bmonth="September", byear="1990", aday="18", amonth="November", ayear="2020"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
