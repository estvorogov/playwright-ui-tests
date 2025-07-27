import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_generator import generate_user

# Позитивный тест: успешное оформление заказа
@pytest.mark.regression
def test_checkout_flow(page):
    login = LoginPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    page.click("button[name='add-to-cart-sauce-labs-backpack']")
    cart.open_cart()
    cart.checkout()

    user = generate_user()
    checkout.fill_information(user['first'], user['last'], user['zip'])
    assert page.url.endswith("checkout-step-two.html")

# Негативные тесты: ошибки при неполном заполнении данных
@pytest.mark.parametrize("first,last,zip", [
    ("", "Doe", "12345"),
    ("John", "", "12345"),
    ("John", "Doe", ""),
])
def test_checkout_validation(page, first, last, zip):
    login = LoginPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    page.click("button[name='add-to-cart-sauce-labs-backpack']")
    cart.open_cart()
    cart.checkout()

    checkout.fill_information(first, last, zip)
    assert page.locator(".error-message-container").is_visible()
