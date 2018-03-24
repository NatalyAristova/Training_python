from model.group_contact import Group_contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Group_contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts