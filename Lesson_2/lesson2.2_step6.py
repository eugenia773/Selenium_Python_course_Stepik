import time
import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector('[id = "input_value"]')
    x = x_element.text
    y = calc(x)
       
    input_field = browser.find_element_by_class_name("form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(y)
     
    chkbox_element = browser.find_element_by_id("robotCheckbox")
    chkbox_element.click()
    
    rdbutton_element = browser.find_element_by_id("robotsRule")
    rdbutton_element.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(5)

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
