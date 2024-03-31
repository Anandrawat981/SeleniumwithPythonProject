import random
import string
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from PageObject.LoginPage import LoginPage
from Testcases.configtest import browsersetup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObject.AddCustomerdetailsPage import customerdetailsPage

class Testcase_03_addCustomer:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getEmailaddress()
    password = ReadConfig.getPassword()
    logger = LogGen.Loggen()

    @pytest.mark.regression
    def test_addcustomer1(self,browsersetup):
        self.logger.info("*************** verifying the login page title ***********")
        self.logger.info("*************** login page title Test started ***********")
        self.driver = browsersetup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        sleep(3)
        #actual_title = self.driver.title
        self.custdetails = customerdetailsPage(self.driver)
        self.custdetails.clickonCustomersmainmenu()
        self.custdetails.clickonlCutomersubmenu()
        self.custdetails.clickonbutton_Add_new()

        self.email = random_generator() + "@gmail.com"
        self.paswrd = random_generator()
        self.custdetails.setEmail(self.email)
        self.custdetails.setPassword(self.paswrd)
        self.firstname =random_generator_names()
        self.lastname = random_generator_names()
        self.custdetails.setFirstname(self.firstname)
        self.custdetails.setLastname(self.lastname)
        self.custdetails.setDateofBirth("10/08/2020")
        #self.custdetails.setCustomersroles("Guests")
        self.custdetails.clickonSave()
        #actual_message=self.custdetails.getmessageAftersave()
        self.msg =self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            print("Test case passed")
            assert True
        else:
            print("Test failed")
            self.driver.save_screenshot(".\\Screenshots" + "\\test_message_aftersave.png")
            assert False







def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
def random_generator_names(size=8,chars=string.ascii_uppercase+string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))