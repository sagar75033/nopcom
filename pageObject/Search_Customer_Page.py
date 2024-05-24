from selenium import webdriver

from selenium.webdriver.common.by import By


class Search_Customer_Page:
    text_email_id = "SearchEmail"
    text_first_name_id = "SearchFirstName"
    text_last_name_id = "SearchLastName"
    btn_search_id = "search-customers"
    text_company_id = "SearchCompany"

    rows_table_xpath = "//table[@id ='customers-grid']//tbody//tr"
    columns_table_xpath = "//table[@id ='customers-grid']//tbody//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enter_customer_email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def enter_customer_fname(self, fname):
        self.driver.find_element(By.ID, self.text_first_name_id).clear()
        self.driver.find_element(By.ID, self.text_first_name_id).send_keys(fname)

    def enter_customer_lname(self, lname):
        self.driver.find_element(By.ID, self.text_last_name_id).clear()
        self.driver.find_element(By.ID, self.text_last_name_id).send_keys(lname)

    def enter_company_name(self, cname):
        self.driver.find_element(By.ID, self.text_company_id).clear()
        self.driver.find_element(By.ID, self.text_company_id).send_keys(cname)

    def click_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def get_result_table_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.rows_table_xpath))

    def get_result_table_column(self):
        return len(self.driver.find_elements(By.XPATH, self.columns_table_xpath))

    def search_customer_by_email(self, email):
        email_present_flag = False
        for r in range(1, self.get_result_table_rows() + 1):
            cust_email = self.driver.find_element(By.XPATH, "//table[@id ='customers-grid']//tbody//tr[" + str(
                r) + "]/td[2]").text

            if cust_email == email:
                email_present_flag = True
                break
        return email_present_flag

    def search_customer_by_name(self, name):
        name_present_flag = False
        for r in range(1, self.get_result_table_rows() + 1):
            cust_name = self.driver.find_element(By.XPATH, "//table[@id ='customers-grid']//tbody//tr[" + str(
                r) + "]/td[3]").text

            if cust_name == name:
                name_present_flag = True
                break
        return name_present_flag

    def search_customer_by_company(self, company):
        company_present_flag = False
        for r in range(1, self.get_result_table_rows() + 1):
            company_name = self.driver.find_element(By.XPATH, "//table[@id ='customers-grid']//tbody//tr[" + str(
                r) + "]/td[5]").text

            if company_name == company:
                company_present_flag = True
                break
        return company_present_flag
