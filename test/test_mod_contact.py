# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Temp"))
    old_groups = app.group.get_group_list()
    app.contact.open_home_page()
    app.contact.edit_contact()
    app.contact.fill_contact_form(
        Contact(firstname="fn change", middlename="mn change", lastname="ln change", nickname="nn change",
                title="t1 change", company="c2 change", address="a3 change", homephone="hp change",
                mobilephone="mp change", workphone="wp change", fax="f4 change", email="el change", email2="el2 change",
                email3="e3 change", homepage="hp change", bday="18", bmonth="August", byear="1985", aday="9",
                amonth="April", ayear="2011"))
    app.contact.update_contact()
    app.contact.return_to_home_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
