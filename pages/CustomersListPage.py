from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CustommersListPage(BasePage):
    url_customers_list = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    customers_list_button = (By.XPATH, "//button[contains(text(), 'Customers')]")
    customer_filter = (By.XPATH, "//input[@placeholder='Search Customer']")
    delete_button = (By.XPATH, "//button[contains(text(), 'Delete')]")

    def __init__(self, driver=None):
        super().__init__(driver)

    def click_customers_list_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.customers_list_button)).click()

    def customer_filter_input(self, customer = 'Neville'):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.customer_filter)).send_keys(customer)

    def delete_custom_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.delete_button)).click()

    def is_url_customers_list(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(self.url_customers_list))
        return True