"""
Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. 
Если всё сделано правильно, то вы увидите окно с проверочным кодом. 
Это число вам нужно ввести в качестве ответа в этой задаче.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)

    first_name = browser.find_element(By.NAME, 'first_name')
    first_name.send_keys('Ivan')

    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('Petrov')

    city = browser.find_element(By.NAME, 'firstname')
    city.send_keys('Smolensk')

    country = browser.find_element(By.ID, 'country')
    country.send_keys('Russia')

    submit = browser.find_element(By.ID, 'submit_button')
    submit.click()

    time.sleep(10)


finally:
    browser.close()
    time.sleep(2)
    browser.quit()