from .pages.login_page import LoginPage
import pytest
import time

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

@pytest.mark.need_review_custom_scenarios
def test_register_with_correct_data(browser):
    page = LoginPage(browser, login_link)
    page.open()
    current_time = int(round(time.time() * 1000))
    username = f"test1+{current_time}@gmail.com"
    password = "R0ZPg2A6c"
    page.register_new_user(username, password)
    page.should_be_authorized_user()