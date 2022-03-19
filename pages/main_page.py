from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators
from selenium.common.exceptions import NoAlertPresentException


class MainPage(BasePage):
    def should_be_login_link(self):  # Метод для проверки наличия кнопки логина
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать

    def go_to_login_page(self):  # Метод для перехода на страницу логина
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No alert presented")
