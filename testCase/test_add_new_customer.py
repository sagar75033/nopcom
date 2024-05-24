import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from pageObject.Add_Customer_Page import Add_Customer_Page
from pageObject.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_Add_New_Customer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_mew_customer(self, setup):
        self.logger.info("***********Test_003_Login***********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.baseURL)
        self.logger.info("***********Verifying the login test***********")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_menu()
        self.add_customer.click_add_new()

        self.logger.info("****** Providing customer info******")
        email = generate_random_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Admin123")
        self.add_customer.enter_first_name("Sagar")
        self.add_customer.enter_last_name("Waghmare")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_dob("02/09/1992")
        self.add_customer.select_tax_exempt()
        self.add_customer.select_newsletter("Test store 2")
        self.add_customer.select_cusrole("Guests")
        self.add_customer.select_Manager_of_vendor("Vendor 2")
        self.add_customer.enter_admincomnt("Test Admin")
        self.add_customer.click_save()
        time.sleep(3)

        self.logger.info("***** Saving customer info ****")

        self.logger.info("*** Add customer validation started *******")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("*** Add customer Test Passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Add_Customer_Page.png")  # Screenshot
            self.logger.error("*** Add customer Test Failed ****")
            assert False

        self.driver.close()
        self.logger.info("*** Ending Add customer test ****")


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com"])
    return f'{username}@{domain}'
