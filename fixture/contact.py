from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("home page").click()

    def open_home_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("home").click()

    def add_new_contact(self):
        dw = self.app.dw
        dw.find_element_by_link_text("add new").click()

    def edit_contact(self):
        dw = self.app.dw
        dw.find_element_by_xpath("//img[@alt='Edit']").click()

    def submit_contact_creation(self):
        dw = self.app.dw
        dw.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def update_contact(self):
        dw = self.app.dw
        dw.find_element_by_name("update").click()

    def fill_contact_form(self, contact):
        dw = self.app.dw
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
        dw = self.app.dw
        if text is not None:
            dw.find_element_by_name(field_name).click()
            Select(dw.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        dw = self.app.dw
        if text is not None:
            dw.find_element_by_name(field_name).click()
            dw.find_element_by_name(field_name).clear()
            dw.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        dw = self.app.dw
        dw.find_element_by_name("selected[]").click()

    def submit_deletion(self):
        dw = self.app.dw
        dw.find_element_by_xpath("//input[@value='Delete']").click()

    def count(self):
        dw = self.app.dw
        self.open_home_page()
        return len(dw.find_elements_by_name("selected[]"))

    def create(self, contact):
        dw = self.app.dw
        self.add_new_contact()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.return_to_home_page()
