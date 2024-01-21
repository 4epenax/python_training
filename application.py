from selenium import webdriver


class Application:

    def __init__(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)

    def login(self, username, password):
        dw = self.dw
        self.open_home_page()
        dw.find_element_by_name("user").click()
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        dw = self.dw
        dw.find_element_by_link_text("Logout").click()

    def open_home_page(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/#")

    def return_to_home_page(self):
        dw = self.dw
        dw.find_element_by_link_text("home page").click()

    def open_groups_page(self):
        dw = self.dw
        dw.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        dw = self.dw
        dw.find_element_by_link_text("group page").click()

    def create_group(self, group):
        dw = self.dw
        self.open_groups_page()
        # init group creation
        dw.find_element_by_name("new").click()
        # fill group form
        dw.find_element_by_name("group_name").click()
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").click()
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").click()
        dw.find_element_by_name("group_footer").clear()
        dw.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        dw.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def create_contact(self, contact):
        dw = self.dw
        # init contact creation
        dw.find_element_by_link_text("add new").click()
        # fill contact form
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
        # submit contact creation
        dw.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()

    def destroy(self):
        self.dw.quit()
