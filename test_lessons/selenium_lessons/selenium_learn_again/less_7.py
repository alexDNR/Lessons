"""
Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, 
который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу https://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), 
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
"""

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'https://SunInJuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)

    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(int(x_element)))
    
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click() # нашли чекбокс 

    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
    #browser.execute_script("window.scrollBy(0, 100);") - можно и не скроллить до определённого элемента, а просто на определённое количество пикселей
    radiobutton.click()  

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(5)


finally:
    browser.close()
    time.sleep(2)
    browser.quit()