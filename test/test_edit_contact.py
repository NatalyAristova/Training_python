from model.group_contact import Group_contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.select_first_contact()
    app.contact.button_Edit()
    app.contact.edit_contact_firm(Group_contact(firstname="Lex", middlename="Alex", lastname="Alex", nickname="Alex", title="Baaa", company="Bsss", address="Brrr", home="4", mobile="1111111",
                                     work="22222", fax="333", email="fff@ya.ru", byear="1990", address2="ffff", phone2="fff", notes="ggg"))
    app.contact.button_Update()
    app.session.logout()