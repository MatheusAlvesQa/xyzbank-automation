from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import consts


class AddCustomerPage(BasePage):
    url_add_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    add_customer_button = (By.XPATH, "//button[contains(text(), 'Add Customer')]")
    first_name_input = (By.XPATH, "//input[@placeholder='First Name']")
    last_name_input = (By.XPATH, "//input[@placeholder='Last Name']")
    post_code_input = (By.XPATH, "//input[@placeholder='Post Code']")
    add_customer_submit_button = (By.XPATH, "//button[@type='submit' and text()='Add Customer']")
    
    def __init__(self, driver=None):
        super().__init__(driver)

    def click_add_customer_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_customer_button)).click()
    
    def register_customer(self, first_name, last_name, post_code):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.post_code_input)).send_keys(post_code)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_customer_submit_button)).click()
    
    def is_url_add_customer(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(self.url_add_customer))
        return True

    def successful_verify_alert_message(self):
        alert_message = Alert(self.driver)
        return consts.CUSTOMER_ADDING_CONFIRMATION_ALERT_MSG in alert_message.text

    def failed_verify_alert_message(self):
        alert_message = Alert(self.driver)
        return consts.CUSTOMER_ADDING_DUPLICATED_ALERT_MSG in alert_message.text