import re
from model.contact import Contact


def test_all_main_info_on_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert contacts_from_home_page == contacts_from_db
    for index in range(len(contacts_from_home_page)):
        contact_from_home_page = contacts_from_home_page[index]
        contact_from_db = contacts_from_db[index]
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert (contact_from_home_page.all_phones_from_home_page ==
                app.contact.merge_phones_like_on_home_page(contact_from_db))
        assert (contact_from_home_page.all_emails_from_home_page ==
                app.contact.merge_emails_like_on_home_page(contact_from_db))
