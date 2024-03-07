from model.contact import Contact
from model.group import Group
import random


def test_del_contact_to_group(app, db, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Temp"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="new"))
    if len(db.get_inside_group()) == 0:
        old_contacts = orm.get_contact_list()
        old_groups = orm.get_group_list()
        random_group = random.choice(old_groups)
        random_contact = random.choice(old_contacts)
        app.contact.open_home_page()
        app.contact.select_contact_by_id(random_contact.id)
        app.contact.select_add_field()
        app.contact.selected_group_option_by_id(random_group.id)
        app.contact.select_add_to()
    old_groups_inside = db.get_inside_group()
    group = random.choice(old_groups_inside)
    app.contact.open_home_page()
    app.contact.select_field_group()
    app.contact.selected_group_page_option_by_id(group.id)
    old_contacts_inside = app.contact.get_contact_list_in_group()
    contact = random.choice(old_contacts_inside)
    app.contact.select_contact_by_id(contact.id)
    app.contact.submit_remove()
    app.contact.go_to_group_page(group.id)
    new_contacts_inside = app.contact.get_contact_list_in_group()
    old_contacts_inside.remove(contact)
    assert old_contacts_inside == new_contacts_inside
