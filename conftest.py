import pytest

from pages.LoginPage import LoginPage

@pytest.fixture
def open_xyz_bank():
    login_page = LoginPage()
    login_page.open_page()
    yield login_page
    login_page.close()

@pytest.fixture
def login_manager(open_xyz_bank):
    login_manager = open_xyz_bank
    if login_manager.is_url('login'):
        login_manager.click_login_manager_button()
    assert login_manager.is_url('manager'), 'Página não encontrada'
    yield login_manager

@pytest.fixture
def login_customer(open_xyz_bank, request):
    name_login = request.param
    login_customer = open_xyz_bank
    if login_customer.is_url('login'):
        login_customer.click_login_customer_button()
    assert login_customer.is_url('customer'), 'Página não encontrada'
    login_customer.customer_select(name_login)
    yield login_customer