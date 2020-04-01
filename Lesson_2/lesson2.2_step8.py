import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_1name = browser.find_element_by_css_selector('[placeholder = "Enter first name"]')
    input_1name.send_keys("My_first_name")
    input_2name = browser.find_element_by_css_selector('[placeholder = "Enter last name"]')
    input_2name.send_keys("My_last_name")
    input_email = browser.find_element_by_css_selector('[placeholder = "Enter email"]')
    input_email.send_keys("My_Email")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'empty_file.txt')
    file_element = browser.find_element_by_id("file")
    file_element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
