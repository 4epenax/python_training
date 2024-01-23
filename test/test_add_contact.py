# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t1", company="c2", address="a3",
                homephone="hp", mobilephone="mp", workphone="wp", fax="f4", email="el", email2="el2", email3="e3",
                homepage="hp", bday="13", bmonth="September", byear="1990", aday="18", amonth="12", ayear="2020"))
    app.session.logout()