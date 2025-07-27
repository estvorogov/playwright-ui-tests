from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_add_to_cart(page):
    login = LoginPage(page)
    cart = CartPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    page.click("button[name='add-to-cart-sauce-labs-backpack']")
    cart.open_cart()
    assert page.locator(".cart_item").is_visible()