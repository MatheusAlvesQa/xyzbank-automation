from pages.DepositPage import DepositPage
import pytest

class Test1:
    @pytest.mark.parametrize("login_customer", ["Neville Longbottom"], indirect=True)
    def test_customer_deposit(self, login_customer):
        """
        Tests the app Deposit operation with one positive integer.
        Ensures the Deposit successful message is displayed.
        """
        deposit_customer_page = DepositPage(driver=login_customer.driver)
        deposit_customer_page.click_deposit_button()
        deposit_customer_page.register_amount_deposit('2000')
        assert deposit_customer_page.confirmation_message()