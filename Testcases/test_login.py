#from selenium import webdriver
#import pytest
import time

from PageObject.LoginPage import LoginPage
from Testcases.configtest import browsersetup
from Testcases.configtest import firefoxsetup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excelUtil
class Testcase_01:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getEmailaddress()
    password = ReadConfig.getPassword()
    logger = LogGen.Loggen()


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



    def test_loginpageTitle(self,browsersetup):
        self.logger.info("*************** verifying the login page title ***********")
        self.logger.info("*************** login page title Test started ***********")
        self.driver=browsersetup
        self.driver.get(self.base_url)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
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

    path = "./Testcases/TestData/userLoginDetails.xlsx"


    def test_ddt_loginpageTitle(self, browsersetup):
        self.logger.info("*************** verifying the login page title ***********")
        self.logger.info("*************** login page title Test started ***********")
        self.driver = browsersetup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.rows = excelUtil.getrowCount(self.path, "Sheet1")
        print("no of rows in excel file:", self.rows)
        statuslst = []
        for r in range(2, self.rows + 1):
            self.un = excelUtil.readData(self.path, "Sheet1", r, 1)
            self.passwd = excelUtil.readData(self.path, "Sheet1", r, 2)
            self.expected = excelUtil.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.un)
            self.lp.setPassword(self.passwd)
            self.lp.clickLogin()
            time.sleep(3)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            if actual_title == expected_title:
                if self.expected == "Pass":
                    self.logger.info("****Passed***")
                    self.lp.clickLogout()
                    statuslst.append("Pass")
                elif self.expected == "Fail":
                    self.logger.error("***Failed***")
                    self.lp.clickLogout()
                    statuslst.append("Fail")
            elif actual_title != expected_title:
                if self.expected == 'Pass':
                    self.logger.error("*****Failed****")
                    #self.lp.clickLogout()
                    statuslst.append("Fail")
                elif self.expected == 'Fail':
                    self.logger.info("****Passed****")
                    #self.lp.clickLogout()
                    statuslst.append("Pass")
        if "Fail" not in statuslst:
            print("Login Data driven Test passed")
            self.logger.info("Login Data driven Test passed")
            self.driver.close()
            assert True
        else:
            print("Login Data driven Test Failed")
            self.logger.error("Login Data driven Test Failed")
            self.driver.close()
            assert False
        print(statuslst)


