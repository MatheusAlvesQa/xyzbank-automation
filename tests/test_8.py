from pages.AddCustomerPage import AddCustomerPage

class Test8:

    def test_add_customer(self, login_manager):
        """
        Tests the duplicated Customer creation operation in the Bank app.
        Ensures the duplicate Customer is NOT added into the customers list.
        """
        add_customer_page = AddCustomerPage(driver=login_manager.driver)
        add_customer_page.click_add_customer_button()
        assert add_customer_page.is_url_add_customer(), 'Página não encontrada'
        add_customer_page.register_customer('Ron', 'Weasly', 'E55555')
        assert add_customer_page.failed_verify_alert_message
