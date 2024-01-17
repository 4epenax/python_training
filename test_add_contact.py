# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class AddTestContact(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)

    def test_add_test_contact(self):
        dw = self.dw
        self.open_home_page(dw)
        self.login(dw)
        self.create_contact(dw)
        self.return_to_home_page(dw)
        self.logout(dw)

    def logout(self, dw):
        dw.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, dw):
        dw.find_element_by_link_text("home page").click()

    def create_contact(self, dw):
        # init contact creation
        dw.find_element_by_link_text("add new").click()
        # fill contact form
        dw.find_element_by_name("firstname").click()
        dw.find_element_by_name("firstname").clear()
        dw.find_element_by_name("firstname").send_keys("qwe")
        dw.find_element_by_name("middlename").click()
        dw.find_element_by_name("middlename").clear()
        dw.find_element_by_name("middlename").send_keys("wea")
        dw.find_element_by_name("lastname").click()
        dw.find_element_by_name("lastname").clear()
        dw.find_element_by_name("lastname").send_keys("qwe")
        dw.find_element_by_name("nickname").click()
        dw.find_element_by_name("nickname").clear()
        dw.find_element_by_name("nickname").send_keys("123")
        dw.find_element_by_name("title").click()
        dw.find_element_by_name("title").clear()
        dw.find_element_by_name("title").send_keys("asd")
        dw.find_element_by_name("company").click()
        dw.find_element_by_name("company").clear()
        dw.find_element_by_name("company").send_keys("asd")
        dw.find_element_by_name("address").click()
        dw.find_element_by_name("address").clear()
        dw.find_element_by_name("address").send_keys("fsd")
        dw.find_element_by_name("home").click()
        dw.find_element_by_name("home").clear()
        dw.find_element_by_name("home").send_keys("123")
        dw.find_element_by_name("mobile").click()
        dw.find_element_by_name("mobile").clear()
        dw.find_element_by_name("mobile").send_keys("asd")
        dw.find_element_by_name("work").click()
        dw.find_element_by_name("work").clear()
        dw.find_element_by_name("work").send_keys("zcx")
        dw.find_element_by_name("fax").click()
        dw.find_element_by_name("fax").clear()
        dw.find_element_by_name("fax").send_keys("312")
        dw.find_element_by_name("email").click()
        dw.find_element_by_name("email").clear()
        dw.find_element_by_name("email").send_keys("qwe1")
        dw.find_element_by_name("email2").click()
        dw.find_element_by_name("email2").clear()
        dw.find_element_by_name("email2").send_keys("123q")
        dw.find_element_by_name("email3").click()
        dw.find_element_by_name("email3").clear()
        dw.find_element_by_name("email3").send_keys("e12e")
        dw.find_element_by_name("homepage").click()
        dw.find_element_by_name("homepage").clear()
        dw.find_element_by_name("homepage").send_keys("31wea")
        dw.find_element_by_name("bday").click()
        Select(dw.find_element_by_name("bday")).select_by_visible_text("13")
        dw.find_element_by_xpath("//option[@value='13']").click()
        dw.find_element_by_name("bmonth").click()
        Select(dw.find_element_by_name("bmonth")).select_by_visible_text("September")
        dw.find_element_by_xpath("//option[@value='September']").click()
        dw.find_element_by_name("byear").click()
        dw.find_element_by_name("byear").clear()
        dw.find_element_by_name("byear").send_keys("1990")
        dw.find_element_by_name("aday").click()
        Select(dw.find_element_by_name("aday")).select_by_visible_text("13")
        dw.find_element_by_xpath("//div[@id='content']/form/select[3]/option[15]").click()
        dw.find_element_by_name("amonth").click()
        Select(dw.find_element_by_name("amonth")).select_by_visible_text("November")
        dw.find_element_by_xpath("//div[@id='content']/form/select[4]/option[12]").click()
        dw.find_element_by_name("ayear").click()
        dw.find_element_by_name("ayear").clear()
        dw.find_element_by_name("ayear").send_keys("2020")
        # submit contact creation
        dw.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def login(self, dw):
        dw.find_element_by_name("user").click()
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys("admin")
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys("secret")
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, dw):
        dw.get("http://localhost/addressbook/#")

    def is_element_present(self, how, what):
        try:
            self.dw.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.dw.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.dw.quit()


if __name__ == "__main__":
    unittest.main()
