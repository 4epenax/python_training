# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application import Application


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="qwe", middlename="wea", lastname="qwe", nickname="123", title="asd",
                                        company="asd", address="fsd", homephone="123", mobilephone="asd",
                                        workphone="zcx",
                                        fax="312", email="qwe1",
                                        email2="123q", email3="e12e", homepage="31wea", bday="13", bmonth="September",
                                        byear="1990",
                                        aday="18", amonth="12", ayear="2020"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
