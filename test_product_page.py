from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest


@pytest.mark.parametrize('product_link',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, product_link):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_added_product_price()
    product_page.check_added_product_title()
    time.sleep(1)


product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.message_basket_is_empty()

@pytest.mark.users_tests
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.login_page = LoginPage(browser, login_link)
        current_time = int(round(time.time() * 1000))
        username = f"test1+{current_time}@gmail.com"
        password = "R0ZPg2A6c"
        self.login_page.register_new_user(username, password)
        self.login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(browser, product_link):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_added_product_price()
        product_page.check_added_product_title()
        time.sleep(1)


