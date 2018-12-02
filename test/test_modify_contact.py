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
