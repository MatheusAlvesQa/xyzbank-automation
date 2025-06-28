from pages.WithdrawlPage import WithdrawlPage
import pytest

@pytest.mark.parametrize("login_customer", ["Hermoine Granger"], indirect=True)
class Test1:

    def test_customer_withdrawl(self, login_customer):
        """
        Tests the app Withdrawl operation with one positive integer.
        Ensures the Withdrawl successful message is displayed.
        """
        withdrawl_customer_page = WithdrawlPage(driver=login_customer.driver)
        withdrawl_customer_page.click_withdrawl_button()
        withdrawl_customer_page.register_amount_withdrawl('1000')
        assert withdrawl_customer_page.confirmation_message()