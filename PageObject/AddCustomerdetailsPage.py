from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class customerdetailsPage:

    link_Customers_mainmenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_cutomer_submenu_xapth = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_Add_new_xpath = "//a[@class='btn btn-primary']"
    text_Email_xapth = "//input[@id='Email']"
    text_Password_xpath = "//input[@id='Password']"
    text_Firstname_xpath= "//input[@id='FirstName']"
    text_Lastname_xpath = "//input[@id='LastName']"
    radio_Gender_Male_xpath = "//input[@id='Gender_Male']"
    radio_Gender_Female_xpath = "//input[@id='Gender_Female']"
    text_Dateofbirth_xpath = "//input[@id='DateOfBirth']"
    text_CompanyName_xpath = "//input[@id='Company']"
    checkbox_IsTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    list_Newsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    list_Customersroles_xapth="//div[@class='input-group-append input-group-required']//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    listvalue_Registered_xpath ="//li[contains(text(),'Registered')]"
    listvalue_ForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    listvalue_Guests_xpath = "//li[contains(text(),'Guests')]"
    listvalue_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    listvalue_Administrators_xpath = "//li[contains(text(),'Administrators')]"
    select_MangerofVendor_xapth="//select[@id='VendorId']"
    text_admincomment_xpath= "//textarea[@id='AdminComment']"
    button_save_xapth = "//button[@name='save']"
    verify_text_Aftersave_xpath ="//div[@class='alert alert-success alert-dismissable']"



    def __init__(self,driver):
        self.driver=driver

    def clickonCustomersmainmenu(self):
        self.driver.find_element(By.XPATH,self.link_Customers_mainmenu_xpath).click()
    def clickonlCutomersubmenu(self):
        self.driver.find_element(By.XPATH,self.link_cutomer_submenu_xapth).click()
    def clickonbutton_Add_new(self):
        self.driver.find_element(By.XPATH,self.button_Add_new_xpath).click()
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.text_Email_xapth).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.text_Password_xpath).send_keys(password)
    def setFirstname(self,firstname):
        self.driver.find_element(By.XPATH,self.text_Firstname_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.XPATH, self.text_Lastname_xpath).send_keys(lastname)

    def setCustomersroles(self,role):
        self.driver.find_element(By.XPATH,self.list_Customersroles_xapth).click()
        sleep(3)
        if role == "Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.listvalue_Registered_xpath)
        elif role == "Administrators":
            self.listitem =self.driver.find_element(By.XPATH,self.listvalue_Administrators_xpath)

        elif role == "Guests":
            self.driver.find_element(By.XPATH,"//span[@class='k-icon k-i-close']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.listvalue_Guests_xpath)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH,self.radio_Gender_Male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH,self.radio_Gender_Female_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.radio_Gender_Male_xpath).click()

    def setDateofBirth(self,dob):
        self.driver.find_element(By.XPATH,self.text_Dateofbirth_xpath).send_keys(dob)

    def clickonSave(self):
        self.driver.find_element(By.XPATH,self.button_save_xapth).click()

    def getmessageAftersave(self):
        self.driver.find_element(By.XPATH,self.verify_text_Aftersave_xpath)










