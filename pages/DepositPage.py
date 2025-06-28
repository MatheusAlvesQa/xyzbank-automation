from pages.BasePage import BasePage
from utils import consts
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DepositPage(BasePage):
    deposit_button = (By.XPATH, "//button[contains(text(), 'Deposit')]")
    amount_deposit_input = (By.XPATH, "//input[@placeholder='amount']")
    deposit_submit_button = (By.XPATH, "//button[@type='submit' and text()='Deposit']")
    message_confirmation_span = [By.XPATH, f"//span[contains(text(), '{consts.DEPOSIT_MSG}')]"]
    
    def __init__(self, driver=None):
        super().__init__(driver)

    def click_deposit_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.deposit_button)).click()
    
    def register_amount_deposit(self, amount):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.amount_deposit_input)).send_keys(amount)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.deposit_submit_button)).click()
    
    def confirmation_message(self):
        deposit_message = self.driver.find_element(*self.message_confirmation_span)
        return deposit_message.is_displayed()