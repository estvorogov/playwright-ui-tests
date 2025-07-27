from .base_page import BasePage

class CartPage(BasePage):
    def open_cart(self):
        self.click('.shopping_cart_link')

    def checkout(self):
        self.click('#checkout')
