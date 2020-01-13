from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

	def __init__(self, *args, **kwargs):
		super(MainPage, self).__init__(*args, **kwargs)

	def go_to_recommended_product_page(self):
		link = self.browser.find_element(*MainPageLocators.RECOMMENDED_PRODUCT_LINK)
		link.click()