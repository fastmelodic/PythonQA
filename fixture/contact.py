from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    def create(self, Contact, Date1, Date2):
        self.open_page_create_contact()
        self.fill_main_info(Contact)
        self.fill_bday(Date1)
        self.fill_aday(Date2)
        self.submit()
        self.contact_cache = None

    def change_value_field(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)


    def fill_main_info(self, Contact):
        self.change_value_field("firstname", Contact.firstname)
        self.change_value_field("middlename", Contact.middlename)
        self.change_value_field("lastname", Contact.lastname)
        self.change_value_field("nickname", Contact.nickname)
        self.change_value_field("title", Contact.title)
        self.change_value_field("company", Contact.company)
        self.change_value_field("email", Contact.email)
        self.change_value_field("home", Contact.homephone)
        self.change_value_field("mobile", Contact.mobilephone)
        self.change_value_field("work", Contact.workphone)
        self.change_value_field("phone2", Contact.secondaryphone)
        self.change_value_field("address", Contact.address)
        self.change_value_field("email2", Contact.email2)
        self.change_value_field("email3", Contact.email3)


    def fill_bday(self, Date):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Date.day)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Date.month)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Date.year)

    def fill_aday(self,Date):
        wd = self.app.wd
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(Date.day)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(Date.month)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Date.year)

    def fill_address(self):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("0")

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_page_create_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit"))>0):
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//input[@id='%s']" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def edit_first_contact(self, Contact, Date1, Date2):
        self.edit_first_contact(0, Contact, Date1, Date2)

    def edit_contact_by_index(self, index, Contact, Date1, Date2):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_main_info(Contact)
        self.fill_bday(Date1)
        self.fill_aday(Date2)
        self.fill_address()
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.open_home_page()
        self.contact_cache = None


    def edit_contact_by_id(self, id, Contact, Date1, Date2):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()
        self.fill_main_info(Contact)
        self.fill_bday(Date1)
        self.fill_aday(Date2)
        self.fill_address()
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.open_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") or wd.current_url.endswith("/addressbook")):
        #if len(wd.find_elements_by_name("Delete")) < 0:
            wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("id")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_email_from_home_page = cells[4].text
                phones = cells[5].text
                self.contact_cache.append(Contact(firstname = firstname, lastname = lastname, address = address, all_email_from_home_page = all_email_from_home_page, id = id, all_phones_from_home_page = phones))
        return list(self.contact_cache)

    def get_contact_list_from_edit_page(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname = firstname, lastname = lastname, id = id, homephone = homephone, mobilephone = mobilephone,
                       workphone = workphone, secondaryphone = secondaryphone, address = address, email = email, email2 = email2, email3 = email3)

    def get_contact_list_from_view_page(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone = homephone, mobilephone = mobilephone, workphone = workphone, secondaryphone = secondaryphone)
