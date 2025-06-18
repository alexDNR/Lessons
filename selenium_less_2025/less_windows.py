"""
Задача: Открыть 2 вкладки в новом окне, считать их title, преобразовать числа, и вставить полученное число на степик.

1️⃣ С помощью Selenium запустите сначала браузер с пустой вкладкой about:blank.
2️⃣ Используйте метод .new_window("tab") откройте сайт 1 в новой вкладке.
3️⃣ Получите из title числовое значение, затем удалите из него все числа 4, 3, 9,  сохраните обработанное число в num1.
4️⃣ Откройте сайт 2 в новой вкладке тем же методом.
5️⃣ Получите из title числовое значение, затем удалите из него все числа 7, 8, 0,  сохраните обработанное число в num2.
6️⃣ Суммируйте полученные ранее числа num1 + num2, полученное значение вставьте в поле ниже на степик.
"""

# from  selenium import webdriver
# import time

# with webdriver.Chrome() as chrome:
#     chrome.switch_to.new_window('tab1')
#     chrome.get('https://parsinger.ru/selenium/8/8.1/site1/')
#     time.sleep(3)
#     str1 = chrome.title
#     print(str1)
#     str1 = str1.replace('4', '').replace('3', '').replace('9','')
#     print(str1)

#     chrome.switch_to.new_window('tab2')
#     chrome.get('https://parsinger.ru/selenium/8/8.1/site2/')
#     time.sleep(3)
#     str2 = chrome.title
#     print(str2)
#     str2 = str2.replace('7', '').replace('8', '').replace('0','')
#     print(str2)

#     print(int(str1) + int(str2))


"""
🔹 Задача: Получить секретный ключ, суммируя числа, появляющиеся на 5 страницах, и вставить итог в поле на главной странице. Если вы все сделали правильно, система выдаст пароль.

1️⃣ С помощью Selenium запустите браузер и откройте главную страницу сайта-тренажера
2️⃣ На главной странице соберите 5 ссылок и откройте их в новых вкладках.
🟢Примечание: Главная страница доступна даже без Selenium, но для остальных страниц требуется управление через Selenium! (https://parsinger.ru/selenium/8/8.1.2/index.html)

3️⃣ Спустя 3 сек, на каждой странице появится по 3 числа, соберите их и получите сумму всех чисел.
4️⃣ Вернитесь на главную страницу и вставьте полученное значение в поле и нажмите кнопку "Проверить"
5️⃣ Если вы все сделали правильно, система выдаст пароль. Считайте его и введите на степик в поле ниже между кавычками.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# result = 0
# with webdriver.Chrome() as chrome:
#     for index in range (1,6):
#         sum_tab = 0
#         print('Порядковый номер страницы - ', index)
#         chrome.get(f'https://parsinger.ru/selenium/8/8.1.2/page{index}.html')
#         time.sleep(4)
#         elements = chrome.find_elements(By.XPATH, "//*[@id='codePlaceholder']/div/div")
#         for i in elements:
#             sum_tab += int(i.text)
#         print(sum_tab)   
#         result += sum_tab
#         print(result)


"""
Настраиваем размер окна.
🔹 Задача: Настройка размера окна и получение секретного пароля
1️⃣ С помощью Selenium зайдите на сайт-тренажер. (https://parsinger.ru/selenium/8/8.2.1/index.html)
2️⃣ Установите размер окна браузера на 1200×720
3️⃣ Нажмите на кнопку "Проверить размер". Если размеры окна установлены корректно (с учетом допустимого отклонения), на странице появится скрытый пароль.
4️⃣ Считайте из DOM полученный пароль.
5️⃣ Вставьте пароль в поле ниже на степик.
"""

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/8/8.2.1/index.html')
#     chrome.set_window_size(1200, 720)
#     print(f'Получили окно с размерами {chrome.get_window_size()}')
#     btn = chrome.find_element(By.XPATH, '//*[@id="checkSizeBtn"]').click()
#     key = chrome.find_element(By.XPATH, '//*[@id="secret"]').text
#     print(key)


"""
🔹 Задача: Получить секретный пароль через правильное вычисление суммы размеров окна браузера.
1️⃣ С помощью Selenium зайдите на сайт-тренажер (https://parsinger.ru/selenium/8/8.2.2/index.html).
2️⃣ Получите размеры окна браузера.
3️⃣ Сложите значения.
4️⃣ Введите полученную сумму в поле на сайте тренажере и нажмите кнопку «Проверить».
5️⃣ Если ответ верный (с учетом небольшого допуска), на странице отобразится секретный пароль.
6️⃣ Вставьте пароль в поле ниже на степик.
🟢 Внимание: данный тренажёр работает только через Selenium. 
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/8/8.2.2/index.html')
#     print(chrome.get_window_size())
#     summ = int(chrome.get_window_size().get('width')) + int(chrome.get_window_size().get('height'))
#     answer = chrome.find_element(By.XPATH, '//*[@id="answer"]').send_keys(summ)
#     btn_answer = chrome.find_element(By.XPATH, '//*[@id="checkBtn"]').click()
#     key = chrome.find_element(By.XPATH, '//*[@id="resultMessage"]').text
#     print(key)    
