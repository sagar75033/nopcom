import time

import pytest

from pageObject.Add_Customer_Page import Add_Customer_Page
from pageObject.LoginPage import LoginPage
from pageObject.Search_Customer_Page import Search_Customer_Page
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_Search_Customer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_customer_by_email(self, setup):
        self.logger.info("***********Test_004_Search_Customer with email***********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.driver.maximize_window()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login completed***********")
        self.logger.info("*********navigating to customer search page******")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_menu()
        self.search_cust = Search_Customer_Page(self.driver)
        self.logger.info("*********starting search customer by email********")
        self.search_cust.enter_customer_email("arthur_holmes@nopCommerce.com")
        self.search_cust.click_search()
        time.sleep(3)

        is_email_present = self.search_cust.search_customer_by_email("arthur_holmes@nopCommerce.com")

        if is_email_present == True:
            assert True
            self.logger.info("**********Test_004_Search_Customer by Email passed**********")
            self.driver.close()

        else:
            self.logger.info("**********Test_004_Search_Customer by Email passed**********")
            self.driver.save_screenshot(".\\Screenshots\\test_search_customer_email.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_customer_by_name(self, setup):
        self.logger.info("***********Test_004_Search_Customer with email***********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.driver.maximize_window()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login completed***********")
        self.logger.info("*********navigating to customer search page******")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_menu()
        self.search_cust = Search_Customer_Page(self.driver)
        self.logger.info("*********starting search customer by Name********")
        self.search_cust.enter_customer_fname("Arthur")
        self.search_cust.enter_customer_lname("Holmes")
        self.search_cust.click_search()
        time.sleep(3)

        is_name_present = self.search_cust.search_customer_by_name("Arthur Holmes")

        if is_name_present == True:
            assert True
            self.logger.info("**********Test_004_Search_Customer by name passed**********")
            self.driver.close()

        else:
            self.logger.info("**********Test_004_Search_Customer by name failed**********")
            self.driver.save_screenshot(".\\Screenshots\\test_search_customer_name.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_customer_by_company(self, setup):
        self.logger.info("***********Test_004_Search_Customer with email***********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.driver.maximize_window()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login completed***********")
        self.logger.info("*********navigating to customer search page******")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_menu()
        self.search_cust = Search_Customer_Page(self.driver)
        self.logger.info("*********starting search customer by Name********")
        self.search_cust.enter_company_name("Indian Cricket Team")
        self.search_cust.click_search()
        time.sleep(3)

        is_company_name_present = self.search_cust.search_customer_by_company("Indian Cricket Team")

        if is_company_name_present == True:
            assert True
            self.logger.info("**********Test_004_Search_Customer by Company name passed**********")
            self.driver.close()

        else:

            self.logger.info("**********Test_004_Search_Customer by Company name failed**********")
            self.driver.save_screenshot(".\\Screenshots\\test_search_company_name.png")
            self.driver.close()
            assert False
