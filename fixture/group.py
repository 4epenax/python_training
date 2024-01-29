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
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        dw = self.app.dw
        if text is not None:
            dw.find_element_by_name(field_name).click()
            dw.find_element_by_name(field_name).clear()
            dw.find_element_by_name(field_name).send_keys(text)

    def submit_deletion(self):
        dw = self.app.dw
        dw.find_element_by_name("delete").click()

    def count(self):
        dw = self.app.dw
        self.open_groups_page()
        return len(dw.find_elements_by_name("selected[]"))

    def create(self, group):
        dw = self.app.dw
        self.open_groups_page()
        self.init_group_creation()
        self.fill_form(group)
        self.submit_group_creation()
        self.return_to_groups_page()
