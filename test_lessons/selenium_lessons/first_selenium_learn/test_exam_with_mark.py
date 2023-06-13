# Структура
# 1. Фикстура функции browser. как в предыдущих примерах.
# 2. Класс который начинается на Test. Как в предыдущих примерах.
# 3. Для функции автотеста прописываем функцию с parametrize( где указываем сущность которую будем передавать и масив ссылок)
# 4. Запускаем функцию автотеста, там:
#   4.1. Записываем в переменную link - ссылку на страницу
#   4.2. Запускаем браузер по ссылке
#   4.3. Находим поле в которое вводим значени переменной, расчитаной через функцию calc()
#   4.4. Находим кнопку "Отправить" и кликаем (можно это сделать через WebDriverWait, но так пока проще)
#   4.5. Пауза
#   4.6. Ищем поле с результатом, записываем текст в переменную result
#   4.7. Через assert сравниваем значение переменной result c ответом - 'Correct!'. Если ошибка - формируем ответ

import pytest
from selenium import webdriver
import time
import math

def calc():
    answer = math.log(int(time.time() + 0.8 ))
    return answer

url_sites = ["https://stepik.org/lesson/236895/step/1", 
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="function")
def browser():
    print("\n-------------------- start browser for test --------------------")
    browser = webdriver.Chrome()
    yield browser
    print("\n-------------------- quit browser --------------------")
    browser.quit()

@pytest.mark.parametrize('url', url_sites)
def test_exam(browser, url):
    link = f"{url}"
    browser.get(link)
    time.sleep(3)
    print(calc())
    text = browser.find_element_by_xpath("//textarea[@class='ember-text-area ember-view textarea string-quiz__textarea']") 
    text.send_keys(str(calc()))
    ok_button = browser.find_element_by_xpath("//button[@class='submit-submission']")
    ok_button.click()
    time.sleep(10)
    result = browser.find_element_by_xpath("//pre[@class = 'smart-hints__hint']")
    result_text = result.text
    print(result_text)
    assert result_text == "Correct!", f"В автотесте по URL = {link}, найдена ошибка {result_text}" 


# запуск автотеста через консоль - pytest -s -v test_exam_with_mark.py