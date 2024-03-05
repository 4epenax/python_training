from model.contact import Contact
from model.group import Group
import random


def test_del_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Temp"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="new"))
    group = random.choice(old_groups)
    contact = random.choice(old_contacts)
    app.contact.open_home_page()
    app.contact.select_field_group()
    app.contact.selected_group_option_by_id(group.id)
    # проверить, что на странице есть контакт, если нет,
    # то добавить контакт в эту групп и вернутся на страницу этой группы
    app.contact.select_contact_by_id(contact.id)
    app.contact.submit_deletion()
