from pages.WithdrawlPage import WithdrawlPage
import pytest

@pytest.mark.parametrize("login_customer", ["Hermoine Granger"], indirect=True)
class Test1:

    def test_customer_withdrawl_invalid_operation(self, login_customer):
        """
        Tests the app Withdrawl operation with one positive integer higher than the available account amount.
        Ensures the Withdrawl invalid operation message is displayed.
        """
        withdrawl_customer_page = WithdrawlPage(driver=login_customer.driver)
        withdrawl_customer_page.click_withdrawl_button()
        withdrawl_customer_page.register_amount_withdrawl('7000')
        assert withdrawl_customer_page.failed_message()