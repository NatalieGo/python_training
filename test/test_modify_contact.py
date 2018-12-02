from model.newcontact import Newcontact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Newcontact(firstname="Testfirstname"))
    app.contact.modify_first_contact(Newcontact(firstname="New Firstname"))

def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Newcontact(firstname="Testfirstname"))
    app.contact.modify_first_contact(Newcontact(middlename="New Middlename"))

def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Newcontact(firstname="Testfirstname"))
    app.contact.modify_first_contact(Newcontact(lastname="New Lastname"))

def test_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Newcontact(firstname="Testfirstname"))
    app.contact.modify_first_contact(Newcontact(mobile="+79222222222"))

def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Newcontact(firstname="Testfirstname"))
    app.contact.modify_first_contact(Newcontact(address="New address"))

def test_modify_contact_all(app):
    if app.contact.count() == 0:
        app.contact.create(Newcontact(firstname="Testfirstname"))
    app.contact.modify_first_contact(Newcontact(firstname="Newfirstname", middlename="Newmiddlename",
                                                lastname="NewLastname", nickname="NewNick", title="Newtitle",
                                                company="Newcompany", address="Newaddress", home="1(999)111-11-22",
                                                mobile="+79111111122", work="2(999)222-22-33", fax="3(999)333-33-44",
                                                email="321@mail.com", email2="654@mail.com", email3="987@mail.com",
                                                homepage="Newpage", bday="3", bmonth="March", byear="1991", aday="4",
                                                amonth="April", ayear="2003", address2="Newaddress2",
                                                phone2="4(999)444-44-55", notes="Newnotes"))
