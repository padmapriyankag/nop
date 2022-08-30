from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Loginpage:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_xpath= "//a[normalize-space()='Logout']"

    def __init__(self, driver,url):
        self.driver=driver
        self.driver.get(url)


    def set_user_name(self, username):
        self.driver.find_element("id",self.textbox_email_id).clear()
        self.driver.find_element("id",self.textbox_email_id).send_keys(username)

    # def set_user_name(self,username):
    #     self.driver.find_element_by_id(self.textbox_email_id).clear()
    #     self.driver.find_element_by_id(self.textbox_email_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element("id",self.textbox_password_id).clear()
        self.driver.find_element("id",self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element("xpath",self.button_login_xpath).click()
    def click_logout(self):
        self.driver.find_element("xpath",self.link_logout_xpath).click()
