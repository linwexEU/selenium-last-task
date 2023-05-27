from selenium.webdriver.common.by import By
from .product_page import BasePage
from .locator_page import PageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


