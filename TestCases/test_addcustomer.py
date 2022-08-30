import string
import random
import pytest
from selenium.webdriver.common.by import By

from PageObjects.AddCustomer import AddCustomer
from PageObjects.LoginPage import Loginpage

from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_T003_Add_customer:
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    url=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_addcustomer(self,setup):
        self.driver=setup
        self.lp=Loginpage(self.driver,self.url)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.ac=AddCustomer(self.driver)

        self.ac.click_on_customer()
        self.ac.click_on_customer_action()
        self.ac.click_on_add_new()
        email=''.join(random.choices(string.ascii_lowercase,k=5))+"@gmail.com"
        self.ac.send_email(email)
        self.ac.send_password("abc")
        self.ac.send_firstname("ab")
        self.ac.send_lastname("a")
        self.ac.select_gender("male")
        self.ac.send_dob("1/1/1997")
        self.ac.select_vendor("Vendor 1")
        self.ac.click_on_save()
        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        if 'The new customer has been added successfully.' in self.msg:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False




