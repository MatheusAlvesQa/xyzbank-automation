from pages.OpenAccountPage import OpenAccountPage
class Test5:

    def test_open_account(self, login_manager):
        """
        Tests the Opening a customer account operation in the Bank app.
        Ensures the new account is created with a successful message displayed.
        """
        open_account_page = OpenAccountPage(driver=login_manager.driver)
        open_account_page.click_open_account_button()
        assert open_account_page.is_url_open_account(), 'Página não encontrada'
        open_account_page.customer_select('Neville Longbottom')
        open_account_page.currency_select('Dollar')
        open_account_page.click_process_button()
        assert open_account_page.verify_alert_message
        