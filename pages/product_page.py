from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_basket(self):    # Функция для добавления товара в корзину
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def guest_can_add_product_to_basket(self):  # Функция для запуска проверок при добавлении товара в корзину
        self.add_product_to_basket()
        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            print("No alert presented")
        self.guest_can_see_message_product_add_to_basket()
        self.guest_can_see_same_product_name()
        self.guest_can_see_message_price_basket()
        self.guest_can_see_correct_price_basket()

    def guest_can_see_message_product_add_to_basket(self):  # Проверка сообщения, что товар добавлен в корзину
        message_product_add_to_basket = self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT)
        assert message_product_add_to_basket, "Product not added to basket."

    def guest_can_see_same_product_name(self):  # Проверка, что имена товара в корзине и в магазине совпадают
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        print(f'Name in store: {product_name_in_store.text}, Name in basket: {product_name_in_basket.text}')
        assert product_name_in_store.text == product_name_in_basket.text, "Products names are not the same"

    def guest_can_see_message_price_basket(self):   # Проверка на наличие цены на товар в корзине
        message_price_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_PRICE)
        assert message_price_basket, "No price in basket."

    def guest_can_see_correct_price_basket(self):   # Проверка, что цены товара в корзине и в магазине совпадают
        product_prise_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_STORE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        print(f'Price in store: {product_prise_in_store.text}, Price in basket: {product_price_in_basket.text}')
        assert product_prise_in_store.text == product_price_in_basket.text, "Prices don't match"
