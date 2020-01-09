import os
import time

from selenium import webdriver
	

def find_path(filename):
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path  = os.path.join(current_dir, filename)
	return file_path
	

	
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
	first_name = browser.find_element_by_css_selector("[name='firstname']")
	first_name.send_keys("Rick")
	
	last_name = browser.find_element_by_css_selector("[name='lastname']")
	last_name.send_keys("Sanchez")
	
	email = browser.find_element_by_css_selector("[name='email']")
	email.send_keys("Rick.Sanchez@gmail.com")
	
	link_button = browser.find_element_by_id("file")
	link_button.send_keys(find_path("test.txt"))
	
	button = browser.find_element_by_css_selector("button.btn.btn-primary")
	button.click()
	
finally:
	time.sleep(5)
	browser.quit()