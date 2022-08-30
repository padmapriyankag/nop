import pytest

from PageObjects.LoginPage import Loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_login:
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    url=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logintitle_validate(self,setup):
        self.logger.info("********* test_001_login****")
        self.driver=setup
        self.lp=Loginpage(self.driver,self.url)
        # self.driver.get("https://admin-demo.nopcommerce.com/login")
        title=self.driver.title
        if title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("D:\\python\\nopcom\\ScreenShots\\"+"test_login.png")
            self.driver.close()
            assert False
    @pytest.mark.regression
    def test_001_loginvalidate(self,setup):
        self.driver=setup

        self.lp=Loginpage(self.driver,self.url)
        # self.driver.find_element("id",self.textbox_email_id).clear()
        # self.driver.find_element("id",self.textbox_email_id).send_keys("admin@yourstore.com")

        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        title = self.driver.title
        if title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("D:\\python\\nopcom\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            assert False


