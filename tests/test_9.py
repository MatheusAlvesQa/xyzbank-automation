from pages.TransactionsPage import TransactionsPage
import pytest

@pytest.mark.parametrize("login_customer", ["Hermoine Granger"], indirect=True)
class Test1:    
    def test_transaction_reset_list(self, login_customer):
        """
        Tests the Transactions Reset operation in the Bank app.
        Ensures the balance of the Customer account is equal to 0.
        """
        transaction_page = TransactionsPage(driver=login_customer.driver)
        transaction_page.click_transactions_button()
        transaction_page.click_reset_button()
        transaction_page.click_back_button()
        assert transaction_page.verify_balance_value() == 0, 'Saldo incorreto'