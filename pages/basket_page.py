from selenium.webdriver.common.by import By 
from .product_page import BasePage 
from .locator_page import PageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert "basket is empty" in self.browser.find_element(*PageLocators.BASKET_IS_EMPTY).text.strip(), "Basket is not empty"

    def should_be_no_product(self):
        assert "Continue shopping" in self.browser.find_element(*PageLocators.NO_PRODUCT_IN_BASKET).text.strip(), "Error, there are some products in the basket"












