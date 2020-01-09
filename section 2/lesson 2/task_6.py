import math
import time

from selenium import webdriver
	

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
	
	
browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:
	x = browser.find_element_by_id("input_value")
	
	res = calc(x.text)
	
	res_field = browser.find_element_by_id("answer")
	res_field.send_keys(str(res))
	
	check_box = browser.find_element_by_id("robotCheckbox")
	check_box.click()
	
	radio_button = browser.find_element_by_id("robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
	radio_button.click()
	
	button = browser.find_element_by_css_selector("button.btn.btn-primary")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
	
finally:
	time.sleep(5)
	browser.quit()