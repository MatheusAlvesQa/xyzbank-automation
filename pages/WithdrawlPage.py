from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import consts


class WithdrawlPage(BasePage):
    Withdrawl_button = (By.XPATH, "//button[contains(text(), 'Withdrawl')]")
    amount_Withdrawl_input = (By.XPATH, "//input[@placeholder='amount']")
    Withdrawl_submit_button = (By.XPATH, "//button[@type='submit' and text()='Withdraw']")
    message_confirmation_span = (By.XPATH, f"//span[contains(text(), '{consts.WITHDRAWL_SUCCESSFUL_MSG}')]")
    message_failed_span = (By.XPATH, f"//span[contains(text(), '{consts.WITHDRAWL_FAILED_MSG}')]")
    def __init__(self, driver=None):
        super().__init__(driver)

    def click_withdrawl_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.Withdrawl_button)).click()
    
    def register_amount_withdrawl(self, amount):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.amount_Withdrawl_input)).send_keys(amount)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.Withdrawl_submit_button)).click()
    
    def confirmation_message(self):
        withdrawl_message = self.driver.find_element(*self.message_confirmation_span)
        return withdrawl_message.is_displayed()

    def failed_message(self):
        withdrawl_message = self.driver.find_element(*self.message_failed_span)
        return withdrawl_message.is_displayed()