import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Customer_Page:
    link_customer_menu_xpath = '//a[@href="#"]//p[contains(text(),"Customers")]'
    link_customer_menu_option = "//li[@class='nav-item']//p[normalize-space(text())='Customers']"
    btn_add_new_xpath = '//a[@class="btn btn-primary"]'
    text_email_id = "Email"
    text_password_id = "Password"
    text_first_name_id = "FirstName"
    text_last_name_id = "LastName"
    rdo_gender_male_id = "Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    text_DOB_id = "DateOfBirth"
    text_company_name_id = "Company"
    checkbox_tax_id = "IsTaxExempt"
    newsletter_cusrole_list_xpath = '//div[@class="select2-blue"]'
    cusrole_guest_xpath = '//li[contains(text(),"Guests")]'
    cusrole_administrators_xpath = '//li[contains(text(),"Administrators")]'
    cusrole_forummoderators_xpath = '//li[contains(text(),"Forum Moderators")]'
    cusrole_registered_xpath = '//li[contains(text(),"Registered")]'
    cusrole_vendors_xpath = '//li[contains(text(),"Vendors")]'
    drpdwn_mngrofvandor_id = 'VendorId'
    text_admincoment_id = 'AdminComment'
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_customers(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()

    def click_customers_menu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_option).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def enter_first_name(self, firstname):
        self.driver.find_element(By.ID, self.text_first_name_id).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(By.ID, self.text_last_name_id).send_keys(lastname)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdo_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()

    def enter_dob(self, dob):
        self.driver.find_element(By.ID, self.text_DOB_id).send_keys(dob)

    def select_tax_exempt(self):
        self.driver.find_element(By.ID, self.checkbox_tax_id).click()

    def select_newsletter(self, value):
        elements = self.driver.find_elements(By.XPATH, self.newsletter_cusrole_list_xpath)
        newsletter_field = elements[0]
        newsletter_field.click()
        time.sleep(3)
        if value == "Your store name":
            self.driver.find_element(By.XPATH, '//li[contains(text(),"Your store name")]').click()
        elif value == "Test store 2":
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Test store 2')]").click()
        else:
            self.driver.find_element(By.XPATH, '//li[contains(text(),"Your store name")]').click()

    def select_cusrole(self, role):
        elements = self.driver.find_elements(By.XPATH, self.newsletter_cusrole_list_xpath)
        cusrole_field = elements[1]
        cusrole_field.click()
        time.sleep(3)
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()
            time.sleep(3)
            cusrole_field.click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.cusrole_administrators_xpath).click()
        elif cusrole_field == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.cusrole_forummoderators_xpath).click()
        elif cusrole_field == "Registered":
            pass
        elif cusrole_field == "vendors":
            self.driver.find_element(By.XPATH, self.cusrole_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.cusrole_administrators_xpath).click()

    def select_Manager_of_vendor(self, value):
        select = Select(self.driver.find_element(By.ID, self.drpdwn_mngrofvandor_id))
        select.select_by_visible_text(value)

    def enter_admincomnt(self, admincomments):
        self.driver.find_element(By.ID, self.text_admincoment_id).send_keys(admincomments)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
