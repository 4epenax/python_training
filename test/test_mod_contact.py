# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification_first(
        Contact(firstname="fn change", middlename="mn change", lastname="ln change", nickname="nn change",
                title="t1 change", company="c2 change", address="a3 change", homephone="hp change",
                mobilephone="mp change", workphone="wp change", fax="f4 change", email="el change", email2="el2 change",
                email3="e3 change", homepage="hp change", bday="18", bmonth="August", byear="1985", aday="9",
                amonth="8", ayear="2011"))
    app.session.logout()
