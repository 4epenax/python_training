from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        # self.dw = webdriver.Firefox()
        self.wd = webdriver.Chrome('E:\\Home\\chromedriver.exe')
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_start_page(self):
        dw = self.wd
        dw.get("http://localhost/addressbook/#")

    def destroy(self):
        self.wd.quit()
