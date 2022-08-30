from PageObjects.LoginPage import Loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils
class Test_002_login:
    # username=ReadConfig.getUserName()
    # password=ReadConfig.getPassword()
    path=".//TestData/login_data.xlsx"
    url=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    def test_001_loginvalidate(self,setup):
        self.driver=setup
        self.lp=Loginpage(self.driver,self.url)
        self.rows=ExcelUtils.getRowCount(self.path,"Sheet1")
        ls = []
        for r in range(2,self.rows+1):
            self.username=ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected = ExcelUtils.readData(self.path,'Sheet1',r,3)
            self.lp.set_user_name(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()

            title = self.driver.title
            if title == "Dashboard / nopCommerce administration":
                if self.expected=='Pass':
                 ls.append('Pass')
                 self.lp.click_logout()
                elif self.expected=='Fail':
                  ls.append('Fail')
                  self.lp.click_logout()
            elif title != "Dashboard / nopCommerce administration":
                if self.expected=='Pass':
                 ls.append('Fail')
                 # self.lp.click_logout()
                elif self.expected=='Fail':
                  ls.append('Pass')
        print(ls)
        if "Fail" not in ls:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

'''
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
'''

