# -*- coding: utf-8 -*-

from model.group_contact import Group_contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact=Group_contact(firstname="Ivan", middlename="Sergeevich", lastname="Sergeev", nickname="Ssss", title="aaaa", company="ssss", address="rrrr", home="4", mobile="1111111",
                                     work="22222", fax="333", email="fff@ya.ru", byear="1990", address2="ffff", phone2="fff", notes="ggg")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group_contact.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)

def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact=Group_contact(firstname="", middlename="", lastname="", nickname="",
                                     title="", company="", address="", home="", mobile="",
                                     work="", fax="", email="", byear="", address2="", phone2="",
                                     notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group_contact.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)

