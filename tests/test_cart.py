import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage

# Тест: добавление товара в корзину
@pytest.mark.regression
def test_add_to_cart(page):
    login = LoginPage(page)
    cart = CartPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    page.click("button[name='add-to-cart-sauce-labs-backpack']")
    cart.open_cart()
    assert page.locator(".cart_item").is_visible()

# Тест: удаление товара из корзины
def test_remove_from_cart(page):
    login = LoginPage(page)
    cart = CartPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    page.click("button[name='add-to-cart-sauce-labs-backpack']")
    cart.open_cart()
    page.click("button[name='remove-sauce-labs-backpack']")
    assert page.locator(".cart_item").count() == 0
