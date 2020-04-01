import time
import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button_element = browser.find_element_by_css_selector("button.btn")
    button_element.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input_value_element = browser.find_element_by_id("answer")
    input_value_element.send_keys(y)
    
    submit_element = browser.find_element_by_css_selector("button.btn")
    submit_element.click()
    
finally:
    time.sleep(5)
    browser.quit()
