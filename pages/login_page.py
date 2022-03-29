from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):  # Функция для проверки элементов на странице логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # Функция для проверки корректного url адреса
        assert "login" in self.browser.current_url, "URL does not contain 'login'"

    def should_be_login_form(self):  # Функция для проверки наличия форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):  # Функция для проверки наличия формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login register is not presented"

    def register_new_user(self, email, password):  # Функция регистрации нового пользователя
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_USER).click()
        time.sleep(2)
        self.should_be_authorized_user()
        print("user authorized")
