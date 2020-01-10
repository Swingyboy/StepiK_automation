from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.ADD_TO_BASKET_BTN))
        basket_btn.click()
        self.solve_quiz_and_get_code()
        self.should_be_correct_name()
        self.should_be_correct_price()

    def go_to_basket_page(self):
        view_bskt_btn = self.browser.find_element(*ProductPageLocators.VIEW_BASKET_BTN)
        view_bskt_btn.click()

    def should_be_correct_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME).text
        assert product_name == added_name, f"You have added {added_name} instead {product_name}!!!!"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        assert product_price == added_price, f"You have added product with {added_price} price instead {product_price}!"