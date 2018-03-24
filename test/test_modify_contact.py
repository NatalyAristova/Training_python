
from model.group_contact import Group_contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Group_contact(firstname="Natalia", lastname="Aristova"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact=Group_contact(firstname="Fedor", lastname="Aristov")
    contact.id=old_contacts[index].id
    #contact.firstname=old_contacts[0].firstname
    app.contact.modify_contact_by_index(index=index, new_contact_data=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Group_contact.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)

#def test_modify_contact_middlename(app):
 #   if app.contact.count() == 0:
#        app.contact.create(Group_contact(middlename="test"))
 #   old_contacts = app.contact.get_contact_list()
 #   app.contact.modify_first_contact(Group_contact(middlename="New middlename"))
 #   new_contacts = app.contact.get_contact_list()
  #  assert len(old_contacts) == len(new_contacts)