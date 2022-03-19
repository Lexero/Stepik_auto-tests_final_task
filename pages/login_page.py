from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):  # Функция для проверки элементов на странице логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # Функция для проверки корректного url адреса
        assert "login" in self.browser.current_url, "URL does not contain 'login'"
        assert True

    def should_be_login_form(self):  # Функция для проверки наличия форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):  # Функция для проверки наличия формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login register is not presented"
        assert True
