from model.newcontact import Newcontact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Newcontact(firstname="New Firstname"))

def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Newcontact(middlename="New Middlename"))

def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Newcontact(lastname="New Lastname"))

def test_modify_contact_mobile(app):
    app.contact.modify_first_contact(Newcontact(mobile="+79222222222"))

def test_modify_contact_address(app):
    app.contact.modify_first_contact(Newcontact(address="New address"))
