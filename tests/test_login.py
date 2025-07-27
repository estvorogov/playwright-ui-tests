import pytest
from pages.login_page import LoginPage

# Смоук тест на успешную авторизацию
@pytest.mark.smoke
def test_login_success(page):
    login = LoginPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

# Негативный тест: неправильный пароль
@pytest.mark.regression
def test_login_invalid_password(page):
    login = LoginPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("standard_user", "wrong_password")
    assert login.is_visible("h3[data-test='error']")

# Негативный тест: пустые поля
@pytest.mark.regression
def test_login_empty_fields(page):
    login = LoginPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("", "")
    assert login.is_visible("h3[data-test='error']")

# Негативный тест: заблокированный пользователь
@pytest.mark.regression
def test_login_locked_out_user(page):
    login = LoginPage(page)
    login.goto("https://www.saucedemo.com/")
    login.login("locked_out_user", "secret_sauce")
    error_text = login.get_text("h3[data-test='error']")
    assert "locked out" in error_text.lower()
