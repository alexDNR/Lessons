
#----------------------------------------------------------------------------------------------------------------
"""
Задачи
Секунды на Счетчике: У вас есть ровно 5 секунд, чтобы пройтись по ячейкам на странице и очистить только те, которые доступны для редактирования.
Проверка: Нажмите на кнопку "Проверить" на странице.
Секретный код: Из всплывающего алерт-окна скопируйте код и вставьте его в поле для ответа.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# #options.add_argument('--headless') # запуск драйвера без экрана браузера
# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
#     fields = browser.find_elements(By.CLASS_NAME, "text-field")
#     for i in fields:
#         if not i.get_attribute('disabled'):
#             i.clear()          
#     ok = browser.find_element(By.ID, "checkButton").click()
#     # Переключаемся на алерт и получаем его текст
#     print(browser.switch_to.alert.text)
#----------------------------------------------------------------------------------------------------------------    

"""
Кодовое имя: Операция "Бессмертный Печенюшка"
Ваша задача как кибердетектива — найти "Бессмертный Печенюшка" среди лабиринта из 42 разных ссылок. 
Этот мифический печенюшка не прост; он обладает самым долгим сроком жизни среди всех остальных на этих страницах. 
Ваши средства — мощные инструменты языка программирования, которые не оставят ему шанса скрыться от нас. Ваш ход, детектив.

Этапы миссии:
Следование за линками: На основной странице будет 42 ссылки. Открывайте каждую из них, чтобы исследовать и выяснить, какой из cookies имеет самый долгий срок жизни.
Вычисление жизнеспособности: Для каждой открытой страницы анализируйте срок жизни её cookie ['expiry']. Сохраняйте эти данные для последующего сравнения.
Коронация Бессмертного: После проверки всех 42 страниц определите, на какой из них находится cookie с самым долгим сроком жизни. 
    С этой страницы извлеките число которое лежит в  теге <p id="result">INT</p>.
Завершающий этап: Вставьте полученное число в специальное поле для степик. Поздравляем, вы нашли "Бессмертного Печенюшка" и преуспели в этой миссии!
"""
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# #options.add_argument('--headless') # запуск драйвера без экрана браузера
# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/methods/5/index.html')
#     links = browser.find_elements(By.XPATH, "//a")
#     list_expiry = []
#     for i in links:
#         i.click()  
#         for item in browser.get_cookies() :
#             list_expiry.append(item['expiry'])
#         browser.back()
    
#     for i in links:
#         if int(i.text) == list_expiry.index(max(list_expiry)) + 1:
#             i.click()
#             result = browser.find_element(By.ID, "result")
#             print(result.text)
#             browser.back()


"""
Кодовое имя: Операция "Освобождение Пути"
В вашем пути к завершению задачи на курсе внезапно возникла преграда: элемент, который вам необходимо кликнуть, 
    оказался перекрыт другим элементом. 
Вы столкнулись с ошибкой,и теперь вашей задачей является обойти это препятствие. 
Необходимо научиться получать фокус нужного элемента, даже если он перекрыт другими объектами на странице.

Этапы миссии:
Идентификация Элемента: Первым делом необходимо найти элемент, с которым вы хотите взаимодействовать.
# Пример поиска элемента по ID ==== browser.find_element(By.ID, 'btn')
Получение Фокуса: Воспользуйтесь методом scrollIntoView для того, чтобы прокрутить страницу так, чтобы нужный элемент оказался в видимой области.
# Пример получения фокуса элемента ==== element = browser.find_element(By.CLASS_NAME, 'btn')
                                        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
Клик по Элементу: Теперь, когда элемент в фокусе, попробуйте снова выполнить клик.
Проверка Результата: Убедитесь, что ваше взаимодействие с элементом привело к желаемому результату(
    в теге с  <p id="result">788544</p> появляется уникальное для каждой кнопки число).
Суммирование:  Суммируйте все полученные числа.
Завершающий этап: Вставьте полученную сумму в поле ответов на Степике.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# options = webdriver.ChromeOptions()
# #options.add_argument('--headless') # запуск драйвера без экрана браузера
# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/scroll/4/index.html')
#     sum = 0
#     btns = browser.find_elements(By.CLASS_NAME, "btn")
#     for i in btns:
#         browser.execute_script("return arguments[0].scrollIntoView(true);", i) # прокурутка элемента до попадания в фокус
#         i.click()
#         sum = sum + int(browser.find_element(By.ID, "result").text)
#     print(sum)


"""
Числовая Добыча: Операция 'Чекбокс'
Задачи
Случайная Локация: Откройте указанный сайт с помощью Selenium. Здесь вас встретят 100 текстовых полей, 
    и рядом с некоторыми из них будут чекбоксы. Главная загвоздка: чекбоксы и их состояние ("checked" или нет) определяются случайным образом.

Числовая Сборка: Пройдитесь по всем 100 текстовым полям и соберите числа только из тех, которые имеют рядом "checked" чекбоксы.

Особенности и Условности
Поля и чекбоксы могут загружаться в разных комбинациях, поэтому рассчитывать на конкретную последовательность или паттерн не стоит.
Чекбоксы могут быть в двух состояниях: checked (отмечены) и unchecked (не отмечены). Мы интересуемся только числами из полей с отмеченными чекбоксами.
Собранные числа необходимо суммировать и полученный результат вставить в поле ответа степик.

Для проверки состояния чекбокса используйте метод: .is_selected()
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# options = webdriver.ChromeOptions()
# #options.add_argument('--headless') # запуск драйвера без экрана браузера
# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
#     sum = 0
#     fields = browser.find_elements(By.CLASS_NAME, "parent")
#     for i in range(1, len(fields)):
#         checkbox = browser.find_element(By.XPATH, f"//div[{i}]/input")
#         if checkbox.is_selected():
#             textarea = browser.find_element(By.XPATH, f"//div[{i}]/textarea").text
#             sum += int(textarea)
#     print(sum)        


"""
Операция "Цветовая Синхронизация"
Задачи
Исследование Территории: Откройте веб-сайт с помощью Selenium. Проанализируйте поля, с которыми предстоит работать.
Миссия "Синхронизация": На странице находятся 100 текстовых полей: 50 серых и 50 синих. Ваша задача — перенести числа из серых полей в синие.
 Проверка и Контроль: Нажмите на кнопку "Проверить". Если перенос чисел прошёл успешно, поля станут зелёными.
Получение Кода: Секретный код появится только в том случае, если все поля успешно стали зелёными.
Секретный код нужно будет вставить в поле для ответа на степик.
"""
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# options = webdriver.ChromeOptions()
# #options.add_argument('--headless') # запуск драйвера без экрана браузера
# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
#     fields = browser.find_elements(By.CLASS_NAME, "parent")
#     for i in range(1, len(fields)+1):
#         textarea_gray = browser.find_element(By.XPATH, f"//div[{i}]/textarea[1]")
#         text_gray = textarea_gray.text
#         textarea_gray.clear()
#         textarea_blue = browser.find_element(By.XPATH, f"//div[{i}]/textarea[2]").send_keys(text_gray)
#         btn_ok = browser.find_element(By.XPATH, f"//div[{i}]/button").click()
#     time.sleep(3)
#     check_all = browser.find_element(By.ID, "checkAll").click()
#     time.sleep(3)
#     result = browser.find_element(By.ID, "congrats")
#     print(result.text) 

"""
Что вас ждёт на странице.
50 уникальных контейнеров (div), каждый с собственным случайным фоновым HEX цветом.
В каждом блоке присутствует выпадающий список с множеством HEX цветов.
Кнопки с разными цветами и уникальным атрибутом data-hex=.
Чек-боксы и текстовые поля, которые также хотят участвовать в этой великой красочной головоломке.

Что нужно сделать
Загрузка Страницы: Откройте страницу с помощью Selenium. 
Используйте эту страницу с двумя элементами для тренировки.
Коды Цветов: Получите цвет в формате HEX из каждого элемента <span>.
Выбор в Списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и у родительского контейнера.
Кнопочная Магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера.
Чек-Бокс Челлендж: Поставьте галочку в чек-боксе на странице.
Текстовое Поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.
Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".
Повторение: Повторите все эти шаги для каждого найденного на странице контейнера.
Финальный Шаг: После выполнения всех действий, нажмите на кнопку "Проверить все элементы", кнопка расположена в самом низу, появится alert если все условия соблюдены.
Секретный Код: Из алерт-окна получите числовой код и вставьте его в поле ответа степик.
"""
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
# options = webdriver.ChromeOptions()
# #options.add_argument('--headless') # запуск драйвера без экрана браузера
# with webdriver.Chrome(options=options) as browser:
#     browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
#     blocks = browser.find_elements(By.XPATH, '//*[@id="main-container"]/div')
#     for i in range(1, len(blocks) + 1):
#         span = browser.find_element(By.XPATH, f'//*[@id="main-container"]/div[{i}]/span').text
#         select = browser.find_element(By.XPATH, f'//*[@id="main-container"]/div[{i}]/select').click()
#         options = browser.find_elements(By.XPATH, f'//*[@id="main-container"]/div[{i}]/select/option')
#         for o in options:
#             if o.text == span:
#                 o.click()
#         buttons = browser.find_elements(By.XPATH, f'//*[@id="main-container"]/div[{i}]/div/button')
#         for btn in buttons:
#             if btn.get_attribute('data-hex') == span:
#                 btn.click()
#         checkbox = browser.find_element(By.XPATH, f'//*[@id="main-container"]/div[{i}]/input[1]').click()
#         textarea = browser.find_element(By.XPATH, f'//*[@id="main-container"]/div[{i}]/input[2]').send_keys(span)
#         ok = browser.find_element(By.XPATH, f'//*[@id="main-container"]/div[{i}]/button').click() 
#         time.sleep(1)
#     check_all = browser.find_element(By.XPATH, "//body/button").click()
#     alert = Alert(browser)
#     print(alert.text)
#     alert.accept() 


 










