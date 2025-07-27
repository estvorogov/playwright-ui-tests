from .base_page import BasePage

class CheckoutPage(BasePage):
    def fill_information(self, first_name, last_name, zip_code):
        self.fill('#first-name', first_name)
        self.fill('#last-name', last_name)
        self.fill('#postal-code', zip_code)
        self.click('#continue')