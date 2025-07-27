from pages.login_page import LoginPage

def test_login_success(page):
    login = LoginPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"