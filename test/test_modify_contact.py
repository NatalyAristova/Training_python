
from model.group_contact import Group_contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Group_contact(firstname="test"))
    app.contact.modify_first_contact(Group_contact(firstname="New firstname"))

def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Group_contact(middlename="test"))
    app.contact.modify_first_contact(Group_contact(middlename="New middlename"))