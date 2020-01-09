import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
	

def summ(x, y):
	return int(x) + int(y)
	
	
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

try:
	num1 = browser.find_element_by_id("num1")
	num2 = browser.find_element_by_id("num2")
	
	s = summ(num1.text, num2.text)
	
	drop_down = Select(browser.find_element_by_id("dropdown"))
	drop_down.select_by_visible_text(str(s))
	
	button = browser.find_element_by_css_selector("button.btn.btn-default")
	button.click()
	
finally:
	time.sleep(5)
	browser.quit()