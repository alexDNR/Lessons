"""
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/alert_accept.html'


browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url=url)

try:
    submit = browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    alert = browser.switch_to.alert
    alert.accept()
    
    x = browser.find_element(By.ID, 'input_value').text
    answer_x = browser.find_element(By.ID, 'answer').send_keys(calc(x))
    end = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(10)


finally:
    browser.close()
    time.sleep(1)
    browser.quit()    