"""
Задание
На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

Добавьте в самый верх своего кода import math
Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой: 
str(math.ceil(math.pow(math.pi, math.e)*10000))
(можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде) 

Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации

Заполните скриптом форму так же как вы делали в предыдущем шаге урока

После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
Важно! Поиск по тексту ссылки бывает очень удобным, так часто тексты меняются реже, чем атрибуты элементов. 
Но лучше избегать такого метода поиска. Например, если приложение имеет несколько языков интерфейса, ваши тесты будут проходить только с определенным языком интерфейса. 
Применяйте этот метод с осторожностью и помните про возможные ограничения. 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/find_link_text'

a = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)

    link = browser.find_element(By.LINK_TEXT, a).click()

    first_name = browser.find_element(By.NAME, 'first_name').send_keys('Ivan')
    last_name = browser.find_element(By.NAME, 'last_name').send_keys('Petrov')
    city = browser.find_element(By.NAME, 'firstname').send_keys('Smolensk')
    country = browser.find_element(By.ID, 'country').send_keys('Russia')
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(10)

finally:
    browser.close()
    time.sleep(2)
    browser.quit()