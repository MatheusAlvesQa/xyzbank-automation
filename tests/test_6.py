from pages.CustomersListPage import CustommersListPage

class Test6:

    def test_delete_account(self, login_manager):
        custommers_list_page = CustommersListPage(driver=login_manager.driver)
        custommers_list_page.click_customers_list_button()
        assert custommers_list_page.is_url_customers_list(), 'Página não encontrada'
        custommers_list_page.customer_filter_input('Neville')
        custommers_list_page.delete_custom_button()