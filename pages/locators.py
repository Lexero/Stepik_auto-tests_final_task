from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > h2")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form > h2")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRODUCT_PRICE_IN_STORE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE_ADD_PRODUCT = (By.CSS_SELECTOR, "#messages div:first-child")
    SUCCESS_MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner > p")
