"""
Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. 
Отправьте полученное число в качестве ответа для этого задания.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test_file.txt') # добавляем к этому пути имя файла 

url = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url=url)

try:
    first_name = browser.find_element(By.NAME, 'firstname').send_keys('first name')
    last_name = browser.find_element(By.NAME, 'lastname').send_keys('last name')
    email = browser.find_element(By.NAME, 'email').send_keys('email')

    load_file = browser.find_element(By.ID, 'file').send_keys(file_path) # нашли поле выбора файла для загрузки и указали ему путь к файлу

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(10)

finally:
    browser.close()
    time.sleep(1)
    browser.quit()    