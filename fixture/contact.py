from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, newcontact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(newcontact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def fill_contact_form(self, newcontact):
        wd = self.app.wd
        self.change_field_value("firstname", newcontact.firstname)
        self.change_field_value("middlename", newcontact.middlename)
        self.change_field_value("lastname", newcontact.lastname)
        self.change_field_value("nickname", newcontact.nickname)
        self.change_field_value("title", newcontact.title)
        self.change_field_value("company", newcontact.company)
        self.change_field_value("address", newcontact.address)
        self.change_field_value("home", newcontact.home)
        self.change_field_value("mobile", newcontact.mobile)
        self.change_field_value("work", newcontact.work)
        self.change_field_value("fax", newcontact.fax)
        self.change_field_value("email", newcontact.email)
        self.change_field_value("email2", newcontact.email2)
        self.change_field_value("email3", newcontact.email3)
        self.change_field_value("homepage", newcontact.homepage)
        self.change_field_value_select("bday", newcontact.bday)
        self.change_field_value_select("bmonth", newcontact.bmonth)
        self.change_field_value("byear", newcontact.byear)
        self.change_field_value_select("aday", newcontact.aday)
        self.change_field_value_select("amonth", newcontact.amonth)
        self.change_field_value("ayear", newcontact.ayear)
        self.change_field_value("address2", newcontact.address2)
        self.change_field_value("phone2", newcontact.phone2)
        self.change_field_value("notes", newcontact.notes)

    def change_field_value_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open contact form
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

