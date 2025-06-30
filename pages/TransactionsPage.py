from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransactionsPage(BasePage):
    url_transactions_list = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    transactions_button = (By.XPATH, "//button[contains(text(), 'Transactions')]")
    reset_button = (By.XPATH, "//button[contains(text(), 'Reset')]")
    back_button = (By.XPATH, "//button[contains(text(), 'Back')]")
    balance_value = (By.XPATH, "(//div[@class='center']//strong)[2]")
    transacion_record_id = (By.ID, "anchor0")
    transacion_record_type = (By.XPATH, "//*[@id='anchor0']/td[3]")
    transacion_record_amount = (By.XPATH, "//*[@id='anchor0']/td[2]")

    def __init__(self, driver=None):
        super().__init__(driver)

    def click_transactions_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.transactions_button)).click()

    def click_reset_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.reset_button)).click()

    def click_back_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.back_button)).click()

    def verify_balance_value(self):
        get_balance_value = self.driver.find_element(*self.balance_value)
        return int(get_balance_value.text.strip())

    def verify_deposit_record_id(self):
        try:
            WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(self.transacion_record_id))
        except:
            print('Transferencias ainda carregando')

    def verify_balance_value_record(self):
        get_balance_value_record = self.driver.find_element(*self.transacion_record_amount)
        return int(get_balance_value_record.text.strip())
    
    def verify_type_record(self):
        get_type_deposit = self.driver.find_element(*self.transacion_record_type)
        return get_type_deposit.text.strip()
        