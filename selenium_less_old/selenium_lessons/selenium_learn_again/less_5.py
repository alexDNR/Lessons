"""
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. 
Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

 

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
"""

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)

    
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure') #нашли картинку "сундук" по id
    x = x_element.get_attribute('valuex') # взяли значение из атрибута этой картинки "сундук"

    answer = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x)) # нашли элемент ввода посчитанного значения

    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click() # нашли чекбокс 

    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()# нашли радиобаттоны  

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(15)


finally:
    browser.close()
    time.sleep(2)
    browser.quit()