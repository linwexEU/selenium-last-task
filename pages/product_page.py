from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locator_page import PageLocators
from .locator_page import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from .locator_page import BasePageLocators 
import math 
import pytest 

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def add_to_basket(self):
        button = self.browser.find_element(*PageLocators.BASKET_BUTTON_PRODUCT)
        button.click()
    
    def go_to_basket(self):
        link = self.browser.find_element(*PageLocators.BASKET_BUTTON).get_attribute("href")
        self.browser.get(link)

    @pytest.mark.xfail
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False         
        return True 
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    @pytest.mark.xfail  
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def main_book_after_book(self):
        main_book_text = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6.product_main h1").text.strip()
        main_price_book_text = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6.product_main .price_color").text.strip()

        after_book_text = self.browser.find_element(By.CSS_SELECTOR, ".alertinner strong").text.strip()
        after_price_book_text = self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner  strong").text.strip()

        assert main_book_text == after_book_text, "Error"
        assert main_price_book_text == after_price_book_text, "Error"

    def open(self): 
        self.browser.get(self.url)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be" 

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
    
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(
            EC.alert_is_present()
        )
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    
    

    

    
