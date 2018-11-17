# -*- coding: utf-8 -*-
import pytest
from model.newcontact import Newcontact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Newcontact(firstname="Firstnameex", middlename="Middlenameex", lastname="Lastnameex",
                        nickname="Nickex", title="Titleex", company="Companyex", address="Addressex",
                        home="1(999)111-11-11", mobile="+79111111111", work="2(999)222-22-22",
                        fax="3(999)333-33-33", email="123@mail.com", email2="456@mail.com", email3="789@mail.com",
                        homepage="Pageex", bday="1", bmonth="January", byear="1990", aday="2", amonth="February",
                        ayear="2002", address2="Addressex2", phone2="4(999)444-44-44", notes="Notesex"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Newcontact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                        home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="",
                        bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes=""))
    app.session.logout()
