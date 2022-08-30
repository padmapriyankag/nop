from selenium.webdriver.support.ui import Select

class AddCustomer:
    licustomerxpath="//a[@href='#']//p[contains(text(),'Customers')]"
    licustomeractionxpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    liaddnewxpath="//a[normalize-space()='Add new']"
    textemailxpath="//input[@id='Email']"
    textpasswordxpath="//input[@id='Password']"
    textfirstnamexpath="//input[@id='FirstName']"
    textlastnamexpath="//input[@id='LastName']"
    radiomalexpath="//input[@id='Gender_Male']"
    radiofemalexpath="//input[@id='Gender_Female']"
    textdobxpath="//input[@id='DateOfBirth']"
    textcompanyxpath="//input[@id='Company']"
    selectvendorxpath="//select[@id='VendorId']"
    btnsavexpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver
        # self.url=url

    def click_on_customer(self):
        self.driver.find_element("xpath",self.licustomerxpath).click()

    def click_on_customer_action(self):
        self.driver.find_element("xpath",self.licustomeractionxpath).click()
    def click_on_add_new(self):
        self.driver.find_element("xpath",self.liaddnewxpath).click()
    def send_email(self,email):
        self.driver.find_element("xpath",self.textemailxpath).send_keys(email)
    def send_password(self,password):
        self.driver.find_element("xpath",self.textpasswordxpath).send_keys(password)
    def send_firstname(self,firstname):
        self.driver.find_element("xpath",self.textfirstnamexpath).send_keys(firstname)
    def send_lastname(self,lastname):
        self.driver.find_element("xpath",self.textlastnamexpath).send_keys(lastname)
    def select_gender(self,gender):
        if gender=="male":
            self.driver.find_element("xpath",self.radiomalexpath).click()
        else:
            self.driver.find_element("xpath",self.radiomalexpath).click()
    def send_dob(self,dob):
        self.driver.find_element("xpath",self.textdobxpath).send_keys(dob)
    def send_company(self,cname):
        self.driver.find_element("xpath",self.textcompanyxpath).send_keys(cname)
    def select_vendor(self,v):
        drp=Select(self.driver.find_element("xpath",self.selectvendorxpath))
        drp.select_by_visible_text(v)
    def click_on_save(self):
        self.driver.find_element("xpath",self.btnsavexpath).click()
