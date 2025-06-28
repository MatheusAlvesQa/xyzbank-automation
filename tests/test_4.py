from pages.AddCustomerPage import AddCustomerPage

class Test4:
    def test_add_customer(self, login_manager):
        """
        Tests the Customer creation operation in the Bank app.
        Ensures the Customer is added with a successful message displayed.
        """
        add_customer_page = AddCustomerPage(driver=login_manager.driver)
        add_customer_page.click_add_customer_button()
        assert add_customer_page.is_url_add_customer(), 'Página não encontrada'
        add_customer_page.register_customer('Novo', 'Usuario', '12345678')
        assert add_customer_page.successful_verify_alert_message()
