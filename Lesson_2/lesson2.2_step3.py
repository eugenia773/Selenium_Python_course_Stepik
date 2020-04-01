import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1_element = browser.find_element_by_id("num1")
    num2_element = browser.find_element_by_id("num2")
    int_sum = int(num1_element.text) + int(num2_element.text)
    str_sum = str(int_sum)
        
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str_sum)
       
# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(5)

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
