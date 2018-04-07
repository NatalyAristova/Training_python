# -*- coding: utf-8 -*-

from model.group_contact import Group_contact

def test_add_contact(app, json_contacts):
    contact=json_contacts
    old_contacts = app.contact.get_contact_list()
    #contact=Group_contact(firstname="Ivan", middlename="Sergeevich", lastname="Sergeev", nickname="Ssss", title="aaaa")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group_contact.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)



