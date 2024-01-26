class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("group page").click()

    def init_group_creation(self):
        dw = self.app.dw
        dw.find_element_by_name("new").click()

    def submit_group_creation(self):
        dw = self.app.dw
        dw.find_element_by_name("submit").click()

    def selected_first_group(self):
        dw = self.app.dw
        dw.find_element_by_name("selected[]").click()

    def edit(self):
        dw = self.app.dw
        dw.find_element_by_name("edit").click()

    def submit_modification(self):
        dw = self.app.dw
        dw.find_element_by_name("update").click()

    def fill_form(self, group):
        dw = self.app.dw
        # clear and fill group form
        dw.find_element_by_name("group_name").click()
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").click()
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").click()
        dw.find_element_by_name("group_footer").clear()
        dw.find_element_by_name("group_footer").send_keys(group.footer)

    def submit_deletion(self):
        dw = self.app.dw
        dw.find_element_by_name("delete").click()
