from .base_page import BasePage
from .locators import CatalogPageLocators

class ProductPage(BasePage):

    def should_be_basket_button(self):
        assert self.is_element_present(*CatalogPageLocators.BASKET_BUTTON), "Add to basket is not presented"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*CatalogPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_item_in_basket(self):
        assert self.is_element_present(*CatalogPageLocators.ITEM_IN_BASKET), "Item in basket message is not presented"

    def name_equal(self):
        item_basket = self.browser.find_element(*CatalogPageLocators.ITEM_IN_BASKET)
        item_name_in_basket = item_basket.get_attribute('innerHTML')
        item_page = self.browser.find_element(*CatalogPageLocators.ITEM_ON_PAGE)
        item_name_on_page = item_page.get_attribute('innerHTML')
        assert item_name_in_basket == item_name_on_page, "Не совпадает цена товара в корзине и на странице"

    def should_be_basket_price(self):
        assert self.is_element_present(*CatalogPageLocators.PRICE_MESSAGE), "Price in the cart message is not presented"

    def price_equal(self):
        basket_price = self.browser.find_element(*CatalogPageLocators.PRICE_IN_BASKET)
        item_price_in_basket = basket_price.get_attribute('innerHTML')
        page_price = self.browser.find_element(*CatalogPageLocators.PRICE_ON_PAGE)
        item_price_on_page = page_price.get_attribute('innerHTML')
        assert item_price_in_basket == item_price_on_page, "Нихуя"

