from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

	def product_is_in_basket(self):
		pass

	def should_be_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), f"There are some products in the basket!!!"

	def empty_message_should_be_present(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Empty message isn't present!!!"

