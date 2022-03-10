from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REG_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_REPEAT_PASSWORD = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, "#login_form > p > a")


class CatalogPageLocators:
    BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    ITEM_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    ITEM_ON_PAGE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    PRICE_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]')
    PRICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRICE_ON_PAGE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > p.price_color')


class BasketPageLocators:
    SHOW_BASKET_BUTTON = (By.XPATH, "//header/div[1]/div/div[2]/span/a")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_IN_THE_BASKET = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[2]/h3')

