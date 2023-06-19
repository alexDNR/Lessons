"""
Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, 
являющийся простым для компьютера, но сложным для человека.

Ваша программа должна выполнить следующие шаги:

Открыть страницу https://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
Для этой задачи вам понадобится использовать атрибут .text для найденного элемента. Обратите внимание, что скобки здесь не нужны:

x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
x = x_element.text
y = calc(x)
Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. 
Например, text для данного элемента <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение".

Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало вашего скрипта:

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже. 
"""

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'https://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)

    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value') #нашли элемент с числом по id
    x = x_element.text
    
    answer = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x)) # нашли элемент ввода посчитанного значения

    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click() # нашли чекбокс 

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()# нашли радиобаттоны  

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(15)


finally:
    browser.close()
    time.sleep(2)
    browser.quit()