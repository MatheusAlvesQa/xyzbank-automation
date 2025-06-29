import time

from pages.DepositPage import DepositPage
from pages.WithdrawlPage import WithdrawlPage
from pages.TransactionsPage import TransactionsPage

import pytest

@pytest.mark.parametrize("login_customer", ["Neville Longbottom"], indirect=True)
class Test3:
    def test_customer_deposit_withdrawl_check(self, login_customer):

        deposit_customer_page = DepositPage(driver=login_customer.driver)
        deposit_customer_page.click_deposit_button()
        deposit_customer_page.register_amount_deposit('2000')
        deposit_customer_page.confirmation_message()

        withdrawl_customer_page = WithdrawlPage(driver=login_customer.driver)
        withdrawl_customer_page.click_withdrawl_button()
        time.sleep(1)
        withdrawl_customer_page.register_amount_withdrawl('1000')

        transaction_page = TransactionsPage(driver=login_customer.driver)
        transaction_page.click_transactions_button()
        assert transaction_page.verify_balance_value() == 1000, 'Saldo incorreto'
