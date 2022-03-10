from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "подстрока login отсутствует в текущем url браузера"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Отсутствует форма для логина"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Отсутствует форма для регистрации"

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        login.click()
        login.clear()
        login.send_keys(email)
        passw = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        passw.click()
        passw.clear()
        passw.send_keys(password)
        repeat_passw = self.browser.find_element(*LoginPageLocators.REG_REPEAT_PASSWORD)
        repeat_passw.click()
        repeat_passw.clear()
        repeat_passw.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()
