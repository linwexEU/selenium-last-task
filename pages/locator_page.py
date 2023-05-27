from selenium.webdriver.common.by import By 

class PageLocators:
    BASKET_BUTTON_PRODUCT = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert.alert-safe.alert-noicon.alert-success.fade.in")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    NO_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner  a")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL = (By.CSS_SELECTOR, ".form-group  #id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, ".form-group  #id_registration-password1")
    SAME_PASSWORD = (By.CSS_SELECTOR, ".form-group  #id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"



