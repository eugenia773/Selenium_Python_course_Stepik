import time
import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    bt_book_element = browser.find_element_by_id("book")
    price_element = WebDriverWait(browser, 12).until(
                    EC.text_to_be_present_in_element((By.ID, "price"), "100")
                )
    bt_book_element.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input_value_element = browser.find_element_by_id("answer")
    input_value_element.send_keys(y)
    
    submit_element = browser.find_element_by_id("solve")
    submit_element.click()
    
finally:
    time.sleep(10)
    browser.quit()
