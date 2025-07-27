from .base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.fill('#user-name', username)
        self.fill('#password', password)
        self.click('#login-button')
