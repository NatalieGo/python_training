from model.newcontact import Newcontact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Newcontact(firstname="Testfirstname"))
    app.contact.delete_first_contact()
