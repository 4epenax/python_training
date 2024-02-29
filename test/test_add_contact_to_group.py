from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Temp"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    contact = random.choice(old_contacts)
    app.contact.open_home_page()
    app.contact.select_contact_by_id(contact.id)
    app.contact.select_add_field()
    app.contact.selected_group_option_by_id(group.id)
    app.contact.select_add_to()
    app.contact.go_to_group_page(group.id)
