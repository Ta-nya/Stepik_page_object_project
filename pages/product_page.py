from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button add to basket is not found!"

    def check_added_product(self):
        product_price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        product_title = self.get_element_text(*ProductPageLocators.PRODUCT_TITLE)
        message_success_add_to_basket = self.get_element_text(*ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET)
        message_price_of_basket = self.get_element_text(*ProductPageLocators.MESSAGE_PRICE_OF_BASKET)
        assert product_price == message_price_of_basket, "Price is not equal"
        assert product_title == message_success_add_to_basket, "Added wrong product"

