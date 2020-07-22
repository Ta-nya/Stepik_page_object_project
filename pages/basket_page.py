from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_elements_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket is not empty, but should be"

    def message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "There is no MESSAGE_BASKET_IS_EMPTY"
