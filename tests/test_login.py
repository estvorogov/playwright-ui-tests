import pytest
from pages.login_page import LoginPage

# Позитивный тест: успешный вход
@pytest.mark.smoke
def test_login_success(page):
    login = LoginPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

# Негативные проверки: разные ошибочные комбинации
@pytest.mark.parametrize("username,password", [
    ("", ""),
    ("standard_user", ""),
    ("", "secret_sauce"),
    ("locked_out_user", "wrong"),
    ("unknown", "secret_sauce"),
])
def test_login_invalid_combinations(page, username, password):
    login = LoginPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login(username, password)
    # Проверяем наличие блока ошибки
    assert page.locator(".error-message-container").is_visible()
