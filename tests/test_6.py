from pages.CustomersListPage import CustomersListPage

class Test6:

    def test_delete_account(self, login_manager):
        """
        Tests the Removal of a customer account operation in the Bank app.
        Ensures the Deleted account is no longer displayed.
        """
        customers_list_page = CustomersListPage(driver=login_manager.driver)
        customers_list_page.click_customers_list_button()
        assert customers_list_page.is_url_customers_list(), 'Página não encontrada'
        customers_list_page.customer_filter_input('Neville')
        customers_list_page.delete_custom_button()
        assert not customers_list_page.customer_filter_results('Neville')