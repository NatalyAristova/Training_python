from model.group_contact import Group_contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Group_contact(firstname="test"))
    app.contact.delete_first_contact()