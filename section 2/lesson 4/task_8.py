import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(x))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
browser.find_element_by_css_selector('button#book').click()

value = browser.find_element_by_id('input_value')
answer_filed = browser.find_element_by_id('answer')
answer_filed.send_keys(calc(int(value.text)))

submit_button2 = browser.find_element_by_id('solve')
submit_button2.click()

time.sleep(20)
#browser.quit()
