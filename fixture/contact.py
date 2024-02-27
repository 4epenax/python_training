import re

from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(
                wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def edit_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.contact_cache = None

    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_value("bday", contact.bday)
        self.change_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_value("aday", contact.aday)
        self.change_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def submit_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create(self, contact):
        self.add_new_contact()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.return_to_home_page()

    # сброс кеша происходит в методе, который вызывается в конце каждого теста
    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                fname = cells[2].text
                lname = cells[1].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(
                    Contact(id=id, firstname=fname, lastname=lname, address=address,
                            all_phones_from_home_page=all_phones,
                            all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        email = wd.find_element_by_xpath('//*[@id="content"]/a[1]').text
        email2 = wd.find_element_by_xpath('//*[@id="content"]/a[2]').text
        email3 = wd.find_element_by_xpath('//*[@id="content"]/a[3]').text
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       email=email, email2=email2, email3=email3)
