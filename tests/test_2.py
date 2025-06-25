from pages.WithdrawlPage import WithdrawlPage
import pytest

@pytest.mark.parametrize("login_customer", ["Hermoine Granger"], indirect=True)
class Test1:

    def test_customer_Withdrawl(self, login_customer):
        Withdrawl_customer_page = WithdrawlPage(driver=login_customer.driver)
        Withdrawl_customer_page.click_Withdrawl_button()
        Withdrawl_customer_page.register_amount_Withdrawl('1000')
        Withdrawl_customer_page.confirmation_message()