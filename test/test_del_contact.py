

def test_del_contact(app):
    app.contact.select_first_contact()
    app.contact.delete_first_contact()