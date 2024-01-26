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
        dw.find_element_by_name("firstname").click()
        dw.find_element_by_name("firstname").clear()
        dw.find_element_by_name("firstname").send_keys(contact.firstname)
        dw.find_element_by_name("middlename").click()
        dw.find_element_by_name("middlename").clear()
        dw.find_element_by_name("middlename").send_keys(contact.middlename)
        dw.find_element_by_name("lastname").click()
        dw.find_element_by_name("lastname").clear()
        dw.find_element_by_name("lastname").send_keys(contact.lastname)
        dw.find_element_by_name("nickname").click()
        dw.find_element_by_name("nickname").clear()
        dw.find_element_by_name("nickname").send_keys(contact.nickname)
        dw.find_element_by_name("title").click()
        dw.find_element_by_name("title").clear()
        dw.find_element_by_name("title").send_keys(contact.title)
        dw.find_element_by_name("company").click()
        dw.find_element_by_name("company").clear()
        dw.find_element_by_name("company").send_keys(contact.company)
        dw.find_element_by_name("address").click()
        dw.find_element_by_name("address").clear()
        dw.find_element_by_name("address").send_keys(contact.address)
        dw.find_element_by_name("home").click()
        dw.find_element_by_name("home").clear()
        dw.find_element_by_name("home").send_keys(contact.homephone)
        dw.find_element_by_name("mobile").click()
        dw.find_element_by_name("mobile").clear()
        dw.find_element_by_name("mobile").send_keys(contact.mobilephone)
        dw.find_element_by_name("work").click()
        dw.find_element_by_name("work").clear()
        dw.find_element_by_name("work").send_keys(contact.workphone)
        dw.find_element_by_name("fax").click()
        dw.find_element_by_name("fax").clear()
        dw.find_element_by_name("fax").send_keys(contact.fax)
        dw.find_element_by_name("email").click()
        dw.find_element_by_name("email").clear()
        dw.find_element_by_name("email").send_keys(contact.email)
        dw.find_element_by_name("email2").click()
        dw.find_element_by_name("email2").clear()
        dw.find_element_by_name("email2").send_keys(contact.email2)
        dw.find_element_by_name("email3").click()
        dw.find_element_by_name("email3").clear()
        dw.find_element_by_name("email3").send_keys(contact.email3)
        dw.find_element_by_name("homepage").click()
        dw.find_element_by_name("homepage").clear()
        dw.find_element_by_name("homepage").send_keys(contact.homepage)
        dw.find_element_by_name("bday").click()
        dw.find_element_by_xpath("//option[@value='" + contact.bday + "']").click()
        dw.find_element_by_name("bmonth").click()
        dw.find_element_by_xpath("//option[@value='" + contact.bmonth + "']").click()
        dw.find_element_by_name("byear").click()
        dw.find_element_by_name("byear").clear()
        dw.find_element_by_name("byear").send_keys(contact.byear)
        dw.find_element_by_name("aday").click()
        # для поля aday в Anniversary счет идёт с -1, т.е. указывая 18 число, получаем 16
        dw.find_element_by_xpath("//div[@id='content']/form/select[3]/option[" + contact.aday + "]").click()
        dw.find_element_by_name("amonth").click()
        # для поля amonth в Anniversary счет идёт с 0, т.е. указывая 12 месяц, получаем 11(November)
        dw.find_element_by_xpath("//div[@id='content']/form/select[4]/option[" + contact.amonth + "]").click()
        dw.find_element_by_name("ayear").click()
        dw.find_element_by_name("ayear").clear()
        dw.find_element_by_name("ayear").send_keys(contact.ayear)

    def select_first_contact(self):
        dw = self.app.dw
        dw.find_element_by_name("selected[]").click()

    def submit_deletion(self):
        dw = self.app.dw
        dw.find_element_by_xpath("//input[@value='Delete']").click()
