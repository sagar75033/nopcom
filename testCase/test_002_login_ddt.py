import time

from pageObject.LoginPage import LoginPage
from utilities import XLUtilitis
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_Login_ddt:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/DDT.xlsx"
    logger = LogGen.loggen()
    status_list = []

    def test_002_login_ddt(self, setup):
        self.logger.info("***********Verifying the login test***********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtilitis.get_row_count(self.path, "Sheet1")
        print("Number of rows:", self.rows)

        for r in range(2, self.rows + 1):
            self.username = XLUtilitis.read_data(self.path, "Sheet1", r, 1)
            self.password = XLUtilitis.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = XLUtilitis.read_data(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp_login == "Pass":
                    self.logger.info("Test data is passed")
                    self.status_list.append("Pass")
                    self.lp.clickLogout()
                elif self.exp_login == "Fail":
                    self.logger.info("Test data is failed")
                    self.status_list.append("Fail")
                    self.lp.clickLogout()
            elif exp_title != act_title:
                if self.exp_login == "Pass":
                    self.logger.info("Test data is failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "Fail":
                    self.logger.info("Test data is pass")
                    self.status_list.append("Pass")

        print("status list is", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test_002_Login_ddt is failed")
            assert False
        else:
            self.logger.info("Test_002_Login_ddt is pass")
            assert True
