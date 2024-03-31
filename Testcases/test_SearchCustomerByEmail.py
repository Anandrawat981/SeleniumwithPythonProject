import time
import pytest
from PageObject.LoginPage import LoginPage
from PageObject.AddCustomerdetailsPage import customerdetailsPage
#from PageObject.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getEmailaddress()
    password = ReadConfig.getPassword()
    logger = LogGen.Loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = customerdetailsPage(self.driver)
        self.addcust.clickonCustomersmainmenu()
        self.addcust.clickonlCutomersubmenu()
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")

