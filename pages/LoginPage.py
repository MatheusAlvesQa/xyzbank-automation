from pages.BasePage import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    url_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    url_manager = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    url_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    url_customer_logged = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    customer_login_button = (By.XPATH, "//button[contains(text(), 'Customer Login')]")
    customer_name_list = (By.ID, 'userSelect')
    customer_submit_login_button = (By.XPATH, "//button[contains(text(), 'Login')]")
    manager_login_button = (By.XPATH, "//button[contains(text(), 'Bank Manager Login')]")

    def __init__(self, driver=None):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.url_login)

    def is_url(self, page):
        if page == 'login':
            WebDriverWait(self.driver, 5).until(EC.url_to_be(self.url_login))
            return True
        elif page == 'manager':
            WebDriverWait(self.driver, 5).until(EC.url_to_be(self.url_manager))
            return True
        elif page == 'customer':
            WebDriverWait(self.driver, 5).until(EC.url_to_be(self.url_customer))
            return True
        elif page == 'logged':
            WebDriverWait(self.driver, 5).until(EC.url_to_be(self.url_customer_logged))
            return True
    
    def click_login_customer_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.customer_login_button)).click()

    def click_login_manager_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.manager_login_button)).click()
    
    def customer_select(self, name):
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(self.customer_name_list))
        select_name = Select(self.driver.find_element(*self.customer_name_list))
        select_name.select_by_visible_text(name)
        self.driver.find_element(*self.customer_submit_login_button).click()