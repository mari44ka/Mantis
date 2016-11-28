from selenium import webdriver
from fixture.session import Sessionhelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


class Application:
    def __init__(self,browser,config):
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome("/Users/Mari/Downloads/chromedriver")
        elif browser == "safari":
            self.wd = webdriver.Safari("/usr/bin/safaridriver")
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        #self.wd.implicitly_wait(5) only for dynamic applications
        self.config=config
        self.session=Sessionhelper(self)
        self.james=JamesHelper(self)
        self.signup=SignupHelper(self)
        self.mail=MailHelper(self)
        self.base_url=config["web"]["base_url"]


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_homepage(self):
        wd=self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
