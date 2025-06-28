from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from utils import consts


class OpenAccountPage(BasePage):
    url_open_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    open_account_button = (By.XPATH, "//button[contains(text(), 'Open Account')]")
    customer_name_list = (By.ID, 'userSelect')
    currency_list = (By.ID, 'currency')
    open_account_submit_button = (By.XPATH, "//button[@type='submit' and text()='Process']")
    
    def __init__(self, driver=None):
        super().__init__(driver)

    def click_open_account_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.open_account_button)).click()

    def customer_select(self, customer = 'Neville Longbottom'):
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(self.customer_name_list))
        select_name = Select(self.driver.find_element(*self.customer_name_list))
        select_name.select_by_visible_text(customer)

    def currency_select(self, currency = 'Dollar'):
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(self.currency_list))
        select_currency = Select(self.driver.find_element(*self.currency_list))
        select_currency.select_by_visible_text(currency)

    def click_process_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.open_account_submit_button)).click()
    
    def is_url_open_account(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(self.url_open_account))
        return True

    def verify_alert_message(self):
        alert_message = Alert(self.driver)
        return consts.ACCOUNT_OPENED_SUCCESSFUL_MSG in alert_message