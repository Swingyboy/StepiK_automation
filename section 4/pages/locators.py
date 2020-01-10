from selenium.webdriver.common.by import By


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