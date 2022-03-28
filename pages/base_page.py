from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):  # Конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):  # Метод для перехода на страницу корзины
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_login_page(self):  # Метод для перехода на страницу логина
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No alert presented")

    def is_disappeared(self, how, what, timeout=4):  # Метод, который будет ждать 4 секунды, пока элемент не исчезнет
        """
        WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

        Args:
        driver - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
        timeout - Number of seconds before timing out
        poll_frequency - sleep interval between calls By default, it is 0.5 second.
        ignored_exceptions - iterable structure of exception classes ignored during calls.
                             By default, it contains NoSuchElementException only.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):  # Метод для проверки элемента на странице
        """
        :param how:  - how to search (css, id, xpath)
        :param what: - what to look for (selector string)
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):  # Метод для проверки отсутствия какого-либо элемента
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):  # Метод для открытия браузера по ссылке
        self.browser.get(self.url)

    def should_be_login_link(self):  # Метод для проверки наличия кнопки логина
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать

    def solve_quiz_and_get_code(self):  # Метод для решения задачки при добавлении товара в корзину
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
