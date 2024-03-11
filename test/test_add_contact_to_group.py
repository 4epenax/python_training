from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_contacts_not_in_groups()) == 0:
        app.contact.create(Contact(firstname="Temp"))
    if len(orm.get_groups_without_contacts()) == 0:
        app.group.create(Group(name="new"))
    old_contacts = orm.get_contacts_not_in_groups()
    old_groups = orm.get_groups_without_contacts()
    group = random.choice(old_groups)
    contact = random.choice(old_contacts)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_not_in_groups = orm.get_contacts_not_in_groups()
    app.contact.open_home_page()
    app.contact.select_contact_by_id(contact.id)
    app.contact.select_add_field()
    app.contact.selected_group_option_by_id(group.id)
    app.contact.select_add_to()
    app.contact.go_to_group_page(group.id)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    new_contacts_not_in_groups = orm.get_contacts_not_in_groups()
    old_contacts_not_in_groups.remove(contact)
    assert old_contacts_in_group + [contact] == new_contacts_in_group
    assert old_contacts_not_in_groups == new_contacts_not_in_groups
