class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("group page").click()

    def create(self, group):
        dw = self.app.dw
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

    def modification_first(self, group):
        dw = self.app.dw
        self.open_groups_page()
        # init group modification
        dw.find_element_by_name("selected[]").click()
        dw.find_element_by_name("edit").click()
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
        # submit group modification
        dw.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        dw = self.app.dw
        self.open_groups_page()
        # select first group
        dw.find_element_by_name("selected[]").click()
        # submit deletion
        dw.find_element_by_name("delete").click()
        self.return_to_groups_page()