import time
import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    time.sleep(2)
    button_element = browser.find_element_by_tag_name("button")
    button_element.click()
    
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    
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
