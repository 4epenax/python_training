class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        dw = self.app.wd
        self.app.open_start_page()
        dw.find_element_by_name("user").click()
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        dw = self.app.wd
        dw.find_element_by_link_text("Logout").click()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        dw = self.app.wd
        return len(dw.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        dw = self.app.wd
        return dw.find_element_by_xpath("//div[@id='top']/form/b").text == "(%s)" % username
