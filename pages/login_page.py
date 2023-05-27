from .product_page import BasePage 
from .locator_page import BasePageLocators 


class LoginPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def register_new_user(self, email, password):
        email_text = self.browser.find_element(*BasePageLocators.EMAIL)
        email_text.send_keys(email)

        password_text = self.browser.find_element(*BasePageLocators.PASSWORD)   
        password_text.send_keys(password)

        same_password_text = self.browser.find_element(*BasePageLocators.SAME_PASSWORD)   
        same_password_text.send_keys(password)

        button_reg = self.browser.find_elements(*BasePageLocators.REG_BUTTON)[-1]
        button_reg.click()