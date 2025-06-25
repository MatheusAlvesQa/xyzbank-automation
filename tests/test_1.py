from pages.DepositPage import DepositPage
import pytest

@pytest.mark.parametrize("login_customer", ["Neville Longbottom"], indirect=True)
class Test1:    
    def test_customer_deposit(self, login_customer):
        deposit_customer_page = DepositPage(driver=login_customer.driver)
        deposit_customer_page.click_deposit_button()
        deposit_customer_page.register_amount_deposit('2000')
        deposit_customer_page.confirmation_message()