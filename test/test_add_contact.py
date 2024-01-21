# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t1",
                               company="c2", address="a3", homephone="hp", mobilephone="mp",
                               workphone="wp",
                               fax="f4", email="el",
                               email2="el2", email3="e3", homepage="hp", bday="13", bmonth="September",
                               byear="1990",
                               aday="18", amonth="12", ayear="2020"))
    app.session.logout()
