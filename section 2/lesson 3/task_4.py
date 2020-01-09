import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
	
	
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
	button1 = browser.find_element_by_css_selector("button.btn.btn-primary")
	button1.click()
	
	confirm = browser.switch_to.alert
	confirm.accept()
	
	val = browser.find_element_by_id("input_value")
	res = calc(int(val.text))
	
	res_field = browser.find_element_by_id("answer")
	res_field.send_keys(str(res))
	
	submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
	submit_button.click()
	
finally:
	time.sleep(5)
	browser.quit()