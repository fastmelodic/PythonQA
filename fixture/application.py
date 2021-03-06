from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import  GroupHelper
from fixture.contact import  ContactHelper


class Application:

    def __init__(self, browser, baseurl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser ==  "chrome":
            self.wd = webdriver.Chrome()
        elif browser ==  "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseurl = baseurl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def enter_home_page(self):
        wd = self.wd
        wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()