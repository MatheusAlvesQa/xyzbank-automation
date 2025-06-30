from pages.DepositPage import DepositPage
from pages.TransactionsPage import TransactionsPage

import pytest

@pytest.mark.parametrize("login_customer", ["Neville Longbottom"], indirect=True)
class Test3:
    def test_customer_deposit_withdrawl_check(self, login_customer):

        deposit_customer_page = DepositPage(driver=login_customer.driver)
        deposit_customer_page.click_deposit_button()
        deposit_customer_page.register_amount_deposit('2000')
        deposit_customer_page.confirmation_message()

        transaction_page = TransactionsPage(driver=login_customer.driver)
        transaction_page.click_transactions_button()
        transaction_page.verify_deposit_record_id()
        transaction_page.click_back_button()
        transaction_page.click_transactions_button()
        transaction_page.verify_deposit_record_id()
        assert transaction_page.verify_balance_value_record() == 2000, 'Saldo incorreto'
        assert transaction_page.verify_type_record() == 'Credit', 'Tipo de transação incorreta'
