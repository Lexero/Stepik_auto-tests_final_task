import pytest
from pages.product_page import ProductPage
    #from .pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time


def test_guest_can_add_product_to_basket(browser):    # Тест добавления товара в корзину
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
