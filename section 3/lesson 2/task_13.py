import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistraion(unittest.TestCase):
	
	def setUp(self): 
		self.driver = webdriver.Chrome()

	def test_connection_1(self):
		self.driver.get("http://suninjuly.github.io/registration1.html")
		name = self.driver.find_element_by_css_selector(".first_block input.first")
		name.send_keys("John")
		
		last_name = self.driver.find_element_by_css_selector(".first_block input.second")
		last_name.send_keys("Smith")

		email = self.driver.find_element_by_css_selector(".first_block input.third")
		email.send_keys("john.smith@gmail.com")

		button = self.driver.find_element_by_css_selector("button.btn")
		button.click()
		
		time.sleep(1)
		
		welcome_text_elt = self.driver.find_element_by_tag_name("h1")
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text)
		
	def test_connection_2(self):
		self.driver.get("http://suninjuly.github.io/registration2.html")
		name = self.driver.find_element_by_css_selector(".first_block input.first")
		name.send_keys("John")
		
		last_name = self.driver.find_element_by_css_selector(".first_block input.second")
		last_name.send_keys("Smith")
		
		email = self.driver.find_element_by_css_selector(".first_block input.third")
		email.send_keys("john.smith@gmail.com")
		
		button = self.driver.find_element_by_css_selector("button.btn")
		button.click()
		
		time.sleep(1)
		
		welcome_text_elt = self.driver.find_element_by_tag_name("h1")
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text)

	def tearDown(self):
		self.driver.quit()
		

if __name__ == '__main__':
	unittest.main()
