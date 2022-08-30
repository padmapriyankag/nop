from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
import time
link_logout_linktext= "Logout"
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element("id","Email").clear()
driver.find_element("id","Email").send_keys("admin@yourstore.com")
driver.find_element("id","Password").clear()
driver.find_element("id","Password").send_keys("admin")
time.sleep(2)
driver.find_element("xpath","//button[normalize-space()='Log in']").click()
time.sleep(2)
# driver.find_element("xpath","//a[normalize-space()='Logout']").click()

driver.find_element("xpath","//a[@href='#']//p[contains(text(),'Customers')]").click()
driver.find_element("xpath","//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()
driver.find_element("xpath","//a[normalize-space()='Add new']").click()
driver.find_element("xpath","//input[@id='Email']").send_keys("abc@gmail.com")
driver.find_element("xpath","//input[@id='Password']").send_keys("pass")
driver.find_element("xpath","//input[@id='FirstName']").send_keys("a")
driver.find_element("xpath","//input[@id='LastName']").send_keys("b")
driver.find_element("xpath","//input[@id='Gender_Male']").click()
driver.find_element("xpath","//input[@id='Gender_Female']").click()
driver.find_element("xpath","//input[@id='DateOfBirth']").send_keys("1/2/1997")
driver.find_element("xpath","//input[@id='Company']").send_keys("sdc")
def cust(role):
    driver.find_element("xpath","//div[@class='k-multiselect-wrap k-floatwrap'][2]").click()
    if role=="Registered":
        pass
    elif role=="Administrators":
        driver.find_element("xpath","//li[normalize-space()='Administrators']").click()
    elif role=="Forum Moderators":
        driver.find_element("xpath","//li[normalize-space()='Forum Moderators']").click()
    elif role=="Guests":
        driver.find_element("xpath","// span[text() = 'Registered'] / following - sibling::span[ @ title = 'delete']").click()
        driver.find_element("xpath","//li[normalize-space()='Guests']").click()
    elif role=='Vendors':
# driver.find_element("xpath","//option[normalize-space()='Registered']")
        driver.find_element("xpath","//li[normalize-space()='Vendors']").click()

# cust("Guests")
drp=Select(driver.find_element("xpath","//select[@id='VendorId']"))
drp.select_by_visible_text("Vendor 1")

