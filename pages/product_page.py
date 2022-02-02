from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class ProductPage(BasePage):

    def add_to_basket(self)