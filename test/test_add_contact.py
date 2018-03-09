# -*- coding: utf-8 -*-
import pytest
from model.group_contact import Group_contact
from fixture.application_cont import Application_cont


@pytest.fixture
def app(request):
    fixture = Application_cont()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Group_contact(firstname="Ivan", middlename="Sergeevich", lastname="Sergeev", nickname="Ssss", title="aaaa", company="ssss", address="rrrr", home="4", mobile="1111111",
                                     work="22222", fax="333", email="fff@ya.ru", byear="1990", address2="ffff", phone2="fff", notes="ggg"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Group_contact(firstname="", middlename="", lastname="", nickname="",
                                     title="", company="", address="", home="", mobile="",
                                     work="", fax="", email="", byear="", address2="", phone2="",
                                     notes=""))
    app.session.logout()

