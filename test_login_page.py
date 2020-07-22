from .pages.login_page import LoginPage
import pytest

login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

@pytest.mark.need_review_custom_scenarios
def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_form()

@pytest.mark.need_review_custom_scenarios
def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_register_form()

@pytest.mark.need_review_custom_scenarios
def test_should_be_login_url(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_url()