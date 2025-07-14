"""
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

 

Когда ваш код заработает, попробуйте запустить его на странице https://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = 'https://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

try:   
    total = int(browser.find_element(By.ID, 'num1').text) + int (browser.find_element(By.ID, 'num2').text)
    
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(total))

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(15)


finally:
    browser.close()
    time.sleep(2)
    browser.quit()