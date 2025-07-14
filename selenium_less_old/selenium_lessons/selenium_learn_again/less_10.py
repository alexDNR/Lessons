"""
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/redirect_accept.html'


browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url=url)

try:
    submit = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value').text
    answer_x = browser.find_element(By.ID, 'answer').send_keys(calc(x))
    end = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(10)


finally:
    browser.close()
    time.sleep(1)
    browser.quit()    