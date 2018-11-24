from model.newcontact import Newcontact


def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Newcontact(firstname="New Firstname"))
    app.session.logout()

def test_modify_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Newcontact(middlename="New Middlename"))
    app.session.logout()

def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Newcontact(lastname="New Lastname"))
    app.session.logout()

def test_modify_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Newcontact(mobile="+79222222222"))
    app.session.logout()

def test_modify_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Newcontact(address="New address"))
    app.session.logout()
