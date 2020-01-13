from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It is not a login page!!!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented!!!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGIST_FORM), "Registration form is not presented!!!"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGIST_EMAIL)
        email_field.send_keys(email)

        password_field1 = self.browser.find_element(*LoginPageLocators.REGIST_PASSWORD)
        password_field1.send_keys(password)

        password_field2 = self.browser.find_element(*LoginPageLocators.REGIST_CONFIRM_PASSWORD)
        password_field2.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.REGIST_BUTTON)
        button.click()