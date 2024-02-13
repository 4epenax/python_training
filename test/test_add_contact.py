# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("fn", 10), middlename=random_string("mn", 10),
            lastname=random_string("ln", 10), nickname=random_string("nn", 10),
            title=random_string("t1", 10), company=random_string("c2", 10),
            address=random_string("a3", 10), homephone=random_string("hp", 10),
            mobilephone=random_string("mp", 10), workphone=random_string("wp", 10),
            fax=random_string("f4", 10), email=random_string("el", 10),
            email2=random_string("el2", 10), email3=random_string("el3", 10),
            homepage=random_string("hp4", 10), bday="13", bmonth="May", byear="1968", aday="4",
            amonth="April", ayear="2020")
    for i in range(2)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max)
