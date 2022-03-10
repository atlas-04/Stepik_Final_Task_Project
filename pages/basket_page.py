from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "Empty basket message not showing up"

    def empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_THE_BASKET), \
            "Items in the basket, but should not be"
