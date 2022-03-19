import pytest
from pages.product_page import ProductPage
# from .pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

URL_PRODUCT_NewYear = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]


@pytest.mark.parametrize('link', URL_PRODUCT_NewYear)  # Тест добавления товара в корзину с промо нового года
def test_guest_can_add_product_to_basket_promo_newyear(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):  # Тест добавления товара в корзину с промо offer
    product_base_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, product_base_link)
    page.open()
    page.guest_can_add_product_to_basket()


@pytest.mark.xfail(reason="Success message is shown.")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message not close.")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappear_success_message()
