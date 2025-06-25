from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WithdrawlPage(BasePage):
    Withdrawl_button = (By.XPATH, "//button[contains(text(), 'Withdrawl')]")
    amount_Withdrawl_input = (By.XPATH, "//input[@placeholder='amount']")
    Withdrawl_submit_button = (By.XPATH, "//button[@type='submit' and text()='Withdraw']")
    message_confirmation_span = (By.XPATH, "//span[contains(text(), 'Transaction successful')]")
    message_failed_span = (By.XPATH, "//span[contains(text(), 'Transaction Failed. You can not withdraw amount more than the balance.')]")
    def __init__(self, driver=None):
        super().__init__(driver)

    def click_Withdrawl_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.Withdrawl_button)).click()
    
    def register_amount_Withdrawl(self, amount):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.amount_Withdrawl_input)).send_keys(amount)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.Withdrawl_submit_button)).click()
    
    def confirmation_message(self):
        Withdrawl_message = self.driver.find_element(*self.message_confirmation_span)
        return Withdrawl_message.is_displayed()

    def failed_message(self):
        Withdrawl_message = self.driver.find_element(*self.message_failed_span)
        return Withdrawl_message.is_displayed()