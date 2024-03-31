#from selenium import webdriver
#import pytest
import pytest

from PageObject.LoginPage import LoginPage
from Testcases.configtest import browsersetup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Testcase_01:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getEmailaddress()
    password = ReadConfig.getPassword()
    logger = LogGen.Loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self,browsersetup):
       # self.logger.info("*************** Testcase_01 ************")
        LogGen.Loggen().info("*************** Testcase_01 ************")
        LogGen.Loggen().info("*************** home page title Test Started ************")
        #self.logger.info("*************** home page title Test Started ***********")
        self.driver = browsersetup
        self.driver.get(self.base_url)


        act_title=self.driver.title

        if act_title =="Your store. Login":
            assert True
            #self.logger.info("*************** home page title Test Passed ***********")
            LogGen.Loggen().info("*************** home page title Test Started ************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots"+"\\test_homepageTitle.png")
            self.driver.close()
            #self.logger.error("*************** home page title Test Failed ***********")
            LogGen.Loggen().info("*************** home page title Test failed ************")
            assert False


    @pytest.mark.regression
    def test_loginpageTitle(self,browsersetup):
        self.logger.info("*************** verifying the login page title ***********")
        self.logger.info("*************** login page title Test started ***********")
        self.driver=browsersetup
        self.driver.get(self.base_url)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #self.c = AddCustomerdetailsPage(self.driver)
        actual_title=self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*************** login page title Test Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots" + "\\test_loginpageTitle.png")
            self.driver.close()
            self.logger.error("*************** login page Test failed ***********")
            assert False

