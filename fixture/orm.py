from pony.orm import *
from model.group import Group
from model.contact import Contact


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups",
                       column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups",
                     column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header,
                         footer=group.footer)

        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname,
                           lastname=contact.lastname)

        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact))

    def get_orm_group(self, group):
        return list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]

    @db_session
    def get_contacts_in_group(self, group):
        return self.convert_contacts_to_model(self.get_orm_group(group).contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if self.get_orm_group(group) not in c.groups))

    @db_session
    def get_contacts_not_in_groups(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if len(c.groups) == 0))

    @db_session
    def get_groups_without_contacts(self):
        return self.convert_groups_to_model(
            select(g for g in ORMFixture.ORMGroup if len(g.contacts) == 0))
