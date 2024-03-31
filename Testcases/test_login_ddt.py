#from selenium import webdriver
#import pytest
import time

import pytest

from PageObject.LoginPage import LoginPage
from Testcases.configtest import browsersetup
from Testcases.configtest import firefoxsetup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excelUtil

class Testcase_02_ddt:
    base_url = ReadConfig.getApplicationUrl()
    path="./Testcases/TestData/userLoginDetails.xlsx"
    logger = LogGen.Loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ddt_loginpageTitle(self,firefoxsetup):
        self.logger.info("*************** verifying the login page title ***********")
        self.logger.info("*************** login page title Test started ***********")
        self.driver=firefoxsetup
        self.driver.get(self.base_url)
        self.lp=LoginPage(self.driver)
        self.rows=excelUtil.getrowCount(self.path,"Sheet1")
        print("no of rows in excel file:",self.rows)
        f = open("lst.txt","w+")
        statuslst = []

        for r in range(2,self.rows+1):
            self.username=excelUtil.readData(self.path,"Sheet1",r,1)
            self.password=excelUtil.readData(self.path,"Sheet1",r,2)
            self.expected = excelUtil.readData(self.path,"Sheet1",r,3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
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
            elif actual_title!=expected_title:
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
        f.writelines([str(i)+'\n' for i in statuslst])
        f.close()










