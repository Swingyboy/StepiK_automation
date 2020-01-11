from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
	
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    LOGIN_RESET_LINK = (By.CSS_SELECTOR, "[href='/en-gb/password-reset/']")
	
    REGIST_FORM = (By.CSS_SELECTOR, "#register_form")
    REGIST_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGIST_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGIST_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGIST_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
	
	
class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_WISHLST_BTN = (By.CSS_SELECTOR, ".btn-wishlist")
    VIEW_BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    ADDED_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")


class BasketPageLocators():
    pass