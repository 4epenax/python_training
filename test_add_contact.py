# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="qwe", middlename="wea", lastname="qwe", nickname="123", title="asd",
                               company="asd", address="fsd", homephone="123", mobilephone="asd",
                               workphone="zcx",
                               fax="312", email="qwe1",
                               email2="123q", email3="e12e", homepage="31wea", bday="13", bmonth="September",
                               byear="1990",
                               aday="18", amonth="12", ayear="2020"))
    app.logout()
