'''
Поиск чисел
Добро пожаловать в удивительный мир веб-скрапинга, где информация иногда прячется в самых неожиданных местах! 
Ваша задача сегодня — вычислить и собрать числа, которые могут появиться на веб-странице. 
Они могут быть ключами к более сложным задачам или даже просто интересным головоломкам.
Цель
Инициализация: Откройте заданный веб-сайт с помощью Selenium.

Обнаружение чекбоксов: На сайте будет 100 чекбоксов. Если кликнуть на чекбокс, может появится число в теге span 
​​​​​​​<span id="result1">954</span>

Вычисление: Соберите все эти числа и сложите их. 
Отправка ответа: Введите сумму всех чисел, в поле ответа на Stepik.
'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# options = webdriver.ChromeOptions()
# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/scroll/2/index.html')

#     summ = 0

#     divs = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
#     for i in range (0, len(divs)):
#         divs[i].click()
#         time.sleep(1)
#         value = browser.find_element(By.XPATH, f"//div[{i+1}]/div/p/span").text
#         if value == '':
#             continue
#         print(i, value)
#         summ += int(value)

# print(summ)


'''
Infinite scroll
Представьте себя хакером данных в виртуальном мире, где информация хранится не в обычных файлах, 
а в скрытых элементах на веб-страницах. Чтобы добраться до этой информации, вам нужно использовать S
elenium и скрипт Python для автоматизации скроллинга по бесконечному списку элементов. 
Вам предстоит собрать все числа из этих элементов и сложить их.

Цель
Инициализация: Используя Selenium, откройте заданный веб-сайт.
Скроллинг: На сайте имеется список из 100 элементов, который расширяется при скроллинге (infinity scroll).
Сбор данных: Скрольте по интерактивным элементам, чтобы раскрыть все 100 элементов списка. 
Используйте Keys.DOWN или методы ActionChains(driver).
Агрегация: Извлеките все числовые значения из этих элементов и сложите их.
Отправка ответа: Вставьте собранную сумму чисел в предназначенное поле на сайте.

Подсказки и заметки
Помните о задержках при загрузке элементов.
Последний элемент списка имеет класс last-of-list. Используйте это для прерывания цикла скроллинга.
'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# options = webdriver.ChromeOptions()

# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_1/')

#     scroll_field = browser.find_element(By.XPATH, "//*[@id='scroll-container']/div")
#     for i in range(10):
#         ActionChains(browser).move_to_element(scroll_field).scroll_by_amount(1, 1000).perform()
#         time.sleep(1)
    
#     summ = 0
#     fileds = browser.find_elements(By.XPATH, "//div[1]/span")
#     for i in fileds:
#         print(i.text)
#         summ += int(i.text)

#     print(f'sum = {summ}')


'''
Задача
Инициализация: Откройте заданный веб-сайт с помощью Selenium.
Техника скроллинга: Сайт содержит список из 100 элементов, которые появляются только при скроллинге. 
Стандартные элементы типа чекбоксов или другие элементы для "зацепления" тут отсутствуют.
Навигация: Прокрутите страницу до самого низа, используя ActionChains.
Сбор информации: Извлеките все числовые значения из появившихся элементов и сложите их.
Отправка результата: Вставьте полученную сумму в соответствующее поле для ответа на степик.
'''

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# options = webdriver.ChromeOptions()

# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')

#     scroll_field = browser.find_element(By.XPATH, "//*[@id='scroll-container']/div")
#     for i in range(10):
#         ActionChains(browser).move_to_element(scroll_field).scroll_by_amount(1, 1000).perform()
#         time.sleep(1)
    
#     summ = 0
#     fileds = browser.find_elements(By.XPATH, "//div[1]/p")
#     for i in fileds:
#         summ += int(i.text)

#     print(f'sum = {summ}')


"""
Операция "Пятерка": Одновременный Глубокий Скроллинг
Задача
Инициализация: Откройте заданный веб-сайт с помощью Selenium.
Множественная навигация: На сайте есть 5 разных окон, 
в каждом из которых подгружается по 100 элементов при скроллинге.
Техника скроллинга: Для каждого окна прокрутите страницу до самого низа. 
Здесь можно использовать ActionChains для эффективного скроллинга.
Сбор информации: Из каждого окна извлеките все числовые значения и сложите их. Суммируйте данные из всех окон.
Отправка результата: Вставьте полученную сумму в соответствующее поле для ответа на сайте.
"""
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# options = webdriver.ChromeOptions()

# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_3/')
#     all_sum = 0
#     wrappers = browser.find_elements(By.XPATH, "/html/body/div/div")
#     for i in range(0, len(wrappers)):
#         scroll_field = browser.find_element(By.XPATH, f"//*[@id='scroll-container_{i+1}']/div")
#         for _ in range(10):
#             ActionChains(browser).move_to_element(scroll_field).scroll_by_amount(1, 300).perform()
#             time.sleep(0.5) 
#         summ = 0
#         fileds = browser.find_elements(By.XPATH, f"//div[{i+1}]/div[1]/span")
#         for j in fileds:
#             summ += int(j.text)
#         print(f"sum = {summ} элемента scroll-container_{i+1}")  
#         all_sum += summ
#     print(all_sum)   