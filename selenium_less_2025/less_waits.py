"""
⏳ Явные ожидания
🔹 Задача: Получить секретный пароль, используя WebDriverWait.
1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
2️⃣ На странице находятся 5 кнопок, первые 4 из которых активируется через случайный промежуток времени.
3️⃣ Используйте WebDriverWait, чтобы дождаться активации каждой кнопки и нажать её.
4️⃣ Финальная кнопка станет активной после нажатия всех предыдущих и откроет секретный пароль.
5️⃣ Считайте пароль и вставьте его в поле ниже на платформе Stepik.
🟢 Внимание: Пароль отобразится только при использовании Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.1.1/index.html')
#     btns = chrome.find_elements(By.XPATH, "//button")
#     for btn in btns:
#         WebDriverWait(chrome, 15).until(EC.element_to_be_clickable(btn)).click()
#     message1 = chrome.find_element(By.ID, "message").text
#     message2 = chrome.find_element(By.ID, "message2").text
#     print(message1, message2)


"""
📡 Сканирование доступа – ожидание title
🔹 Задача: Дождаться правильного title и получить секретный пароль.
1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
2️⃣ Нажмите кнопку "INITIATE SCAN" для запуска сканирования.
3️⃣ Title страницы начнёт динамически изменяться (пример: "Scanning..." → "Processing..." → "Access Granted").
4️⃣ Используйте WebDriverWait с title_is("Access Granted"), чтобы дождаться нужного заголовка.
5️⃣ Как только title изменится на "Access Granted", пароль появится на странице.
6️⃣ Считайте пароль из DOM и вставьте его в поле ниже на Stepik.
🟢 Внимание: Пароль отобразится только при использовании Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.2.1/index.html')
#     btn_scan = chrome.find_element(By.ID, "startScan").click()
#     WebDriverWait(chrome, 25).until(EC.title_is("Access Granted"))
#     password = chrome.find_element(By.CLASS_NAME, "password-container").text
#     print(password)


"""
🔤 Implicit waits ABCDE.
📌 Условие:
На сайте находится кнопка «Добавить элемент» (id="startButton"). При нажатии на неё поочерёдно появляются 5 кнопок с id="dynamicButton".
Кнопки появляются с разной случайной задержкой (от 2 до 6 секунд), а пароль отображается только после успешного нажатия на все 5 кнопок.
📢 Важно:
Если Selenium попытается кликнуть на кнопку до её появления, тест упадёт с ошибкой NoSuchElementException. 
Чтобы избежать этого, необходимо использовать неявное ожидание implicitly_wait().
🔹 Задача: Автоматизация последовательного нажатия динамических кнопок
1️⃣ Используйте .implicitly_wait()  для неявного ожидания.
2️⃣ С помощью Selenium зайдите на сайт-тренажёр.
3️⃣ Нажмите на  5 динамических кнопок (id="dynamicButton").
4️⃣ После нажатия всех 5 кнопок отобразится пароль в id="secretPassword".
5️⃣ Считайте пароль из DOM и вставьте его в поле ниже на Stepik.
🟢 Внимание: Пароль отобразится только при использовании Selenium.
🎯 Цель: применить неявное ожидание (implicitly_wait()) для работы с динамическими элементами.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.implicitly_wait(15)
#     chrome.get('https://parsinger.ru/selenium/9/9.3.1/index.html')
#     chrome.find_element(By.ID, "startButton").click()
#     for _ in range(5):
#         chrome.find_element(By.ID, "dynamicButton").click()
#     print(chrome.find_element(By.ID, "secretPassword").text)    


"""
🔑 Точный URL – ключ к успеху!
Точный URL – ключ к успеху! 🔑
🔹 Задача: Получить секретный пароль, используя WebDriverWait + EC.url_to_be().
1️⃣ Перейдите на главную страницу сайта-тренажёра через Selenium.
2️⃣ Перейти по кнопке  "Правильный путь".
3️⃣ Используя WebDriverWait и EC.url_to_be(), дождитесь смены ссылки на 
https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure, и только после этого извлекайте пароль.
4️⃣ Вставьте пароль в поле ниже на платформе Stepik.
🟢 Важно:
Ссылка для перехода на правильный путь отличается от финальной ссылки, которую вам нужно дождаться. 
Она изменится спустя 6 секунд после пребывания на сайте.
Пароль появится только при использовании Selenium, не пытайтесь использовать аргументы или средства которые скрывают Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
#     chrome.find_element(By.XPATH, '//a[5]').click()
#     WebDriverWait(chrome, 10).until(EC.url_to_be("https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure"))
#     print(chrome.find_element(By.ID, 'password').text)


"""
🔄 Отследите изменение URL и получите пароль!
🔹 Задача: Получить секретный пароль, используя WebDriverWait + EC.url_changes().
1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ Нажмите кнопку "Начать", после чего откроется Тестовая страница. 
Зафиксируйте текущий URL current_url= browser.current_url.
3️⃣ Используйте WebDriverWait + EC.url_changes(), чтобы дождаться изменения текущего URL.
4️⃣ Как только условие из пункта 3 сработает и станет True, извлеките пароль.
5️⃣ Вставьте пароль в поле ниже на платформе Stepik.
🟢 Важно:
URL изменится автоматически через 5 секунд после перехода.
Пароль появится только при использовании Selenium WebDriver.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.4.4/index.html')
#     chrome.find_element(By.CLASS_NAME, 'btn').click()
#     current_url = chrome.current_url
#     WebDriverWait(chrome, 10).until(EC.url_changes(current_url))
#     print(chrome.find_element(By.ID, 'password').text)


"""
🍌 Абу и бананы 
🔹 🍌 Помогите Абу найти бананы и получите пароль! 
1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
2️⃣ На сайте есть кнопка "Искать бананы", которая при нажатии рандомно открывает копию страницы с другим URL.
3️⃣ Используйте метод .url_contains("...") дождитесь пока в URL будет эта строка текста "qLChv49", 
это будет сигналом, что вы попали на страницу с бананами.
4️⃣ Кликните по кнопке "Проверить улов" и извлеките пароль из тега <p>.
5️⃣ Вставьте пароль в поле ниже на платформе Stepik.
🟢 Внимание: Кнопка "Искать бананы" отобразится только при использовании Selenium!
📢 Важно: Напоминаю, как работает WebDriverWait(browser, 5).until(EC.url_contains("qLChv49")).
Если условие не вернёт True в течение 5 секунд (то есть, если URL не содержит "qLChv49"), 
эта строка кода вызовет исключение TimeoutException.

Внимание, спойлер!
Рекомендуется использовать while True, break, continue, try, except, 
потому что если WebDriverWait не найдёт совпадение в URL, он выбросит исключение TimeoutException. 
Вам нужно обработать его и перезапустить цикл.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     while True:
#         chrome.get('https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html')
#         chrome.find_element(By.CLASS_NAME, 'search-link').click()
#         try:
#             WebDriverWait(chrome, 3).until(EC.url_contains("qLChv49"))
#             chrome.find_element(By.CLASS_NAME, 'check-button').click()
#             print(chrome.find_element(By.ID, 'result').text)
#             break
#         except:
#             continue    


"""
🔢 Охота за числами
🔹 Задача: Автоматизируйте процесс сбора чисел с быстро сменяющихся страниц и получите пароль! 🏆
📌 Условия:
1️⃣ Запуск тренажёра
Перейдите на главную страницу тренажёра c помощью Selenium.
Нажмите кнопку "START". После этого начнётся автоматическая смена страниц каждую секунду.
2️⃣ Сбор чисел
На каждой странице в <div class="number"> будет появляться число.
Используйте url_matches() для отслеживания нужных страниц, создайте паттерн(в теории из прошлого урока).
Страницы которые подходят: https://parsinger.ru/selenium/9/9.4.2/ok/ok_7825915236.html цифры в URL могут быть любыми
При условии если паттерн совпал, собирайте цифры, можно сразу суммировать их.
3️⃣ Определение финальной страницы
Через 20 секунд откроется последняя страница с URL, содержащим "index_2".
На этой странице появится поле ввода и кнопка "Проверить".
4️⃣ Подсчёт и ввод суммы
Просуммируйте все числа, собранные с ok страниц
Введите полученный результат в поле и нажмите "Проверить".
5️⃣ Получение пароля
Если сумма введена правильно, появится пароль.
Скопируйте его и введите в поле ответа на платформе Stepik!
Важные моменты:
📢 WebDriverWait(browser, 5).until(EC.url_changes(previous_url)) отслеживает смену страниц.
📢 Используйте try-except для обработки возможных TimeoutException.
📢 Подумайте, как лучше организовать цикл для сбора данных. Можно использовать while или for.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import re
# with webdriver.Chrome() as chrome:
#     summ = 0
#     list_data = []
#     chrome.get('https://parsinger.ru/selenium/9/9.4.2/index.html')
#     chrome.find_element(By.ID, 'startButton').click()
#     while chrome.current_url != 'https://parsinger.ru/selenium/9/9.4.2/index_2.html':
#         try:
#             if re.match(r"^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$", chrome.current_url):
#                 list_data.append(int(chrome.find_element(By.CLASS_NAME, 'number').text))   
#         except:
#             continue     
#     for i in set(list_data):
#         summ += i
#     chrome.find_element(By.ID, 'sumInput').send_keys(summ)
#     chrome.find_element(By.ID, 'checkButton').click()
#     print(chrome.find_element(By.ID, 'result').text)        


"""
🏠 А есть ли элемент в DOM?
🔹 Задача: Получить ID для трекинга посылки.

1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ Дождитесь появления кода отслеживания.
3️⃣ Извлеките ID из элемента и выведите его в консоль.
4️⃣ Вставьте ID-код отслеживания в поле ниже на платформе Stepik.
🟢 Важно:
ID появится только при использовании Selenium.
Код отслеживания появится автоматически через несколько секунд после загрузки страницы.
Метод presence_of_element_located() гарантирует, что элемент есть в DOM, но не проверяет, видим он или нет.
💡 Подсказка
Если элемент не появляется, попробуйте увеличить таймаут в WebDriverWait.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.5.1/index.html')
#     id = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.ID, 'loading-text')))
#     time.sleep(5)
#     print(id.text)
#     time.sleep(10)


"""
👻 Кнопка-призрак
🔹 Задача: Получить секретный пароль, используя WebDriverWait + EC.visibility_of_element_located().
📋 Сценарий:
На странице есть кнопка "Показать пароль", которая изначально скрыта (display: none).
Через 5 секунд после загрузки страницы кнопка становится видимой, но она не изменяет своё присутствие в DOM.
Пароль появится только после нажатия на кнопку "Показать пароль".
1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ Найдите кнопку "Показать пароль" и дождитесь, пока она станет видимой
3️⃣ После появления кнопки кликните по ней.
4️⃣ Извлеките появившийся пароль и вставьте его в поле на платформе Stepik.
🟢 Важно:
Пароль появится только при использовании Selenium.
Кнопка присутствует в DOM с самого начала, но невидима (display: none).
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.5.2/index.html')
#     WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.ID, 'ghost-button'))).click()
#     print(chrome.find_element(By.ID, 'password-display').text)


"""
🛒⏳ Терпеливый покупатель: ждем загрузки товаров.
🔹 Задача: Получить секретный пароль, используя WebDriverWait + EC.visibility_of_all_elements_located().

📋 Сценарий:
На странице есть кнопка "Load Products", которая загружает товары с разной задержкой (от 1 до 5 секунд).
Кнопка "Проверить" видна на странице с самого начала, но при использовании Selenium она не будет кликабельна, 
пока все товары не загрузятся.

Для получения пароля нужно подсчитать общую сумму всех товаров и ввести её в поле проверки.

1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ Нажмите на кнопку "Load Products" для начала загрузки товаров.
3️⃣ Дождитесь, пока все товары станут видимыми, используя WebDriverWait + .visibility_of_all_elements_located().
4️⃣ Подсчитайте общую сумму всех товаров (сложите цены всех товаров).
5️⃣ Введите полученную сумму в поле ввода и нажмите кнопку "Проверить".
6️⃣ Извлеките появившийся пароль и вставьте его в поле на платформе Stepik.
🟢 Важно:
Пароль появится только при использовании Selenium.
Кнопка "Проверить" видна с самого начала, но Selenium не сможет с ней взаимодействовать, 
пока все товары не загрузятся.
Для правильного подсчёта суммы(int - целое число) нужно удалить символы "$" и "," из текста цены. 
Секретное сообщение с паролем появится с небольшой задержкой после нажатия кнопки "Проверить".
💡Подсказка:
Используйте WebDriverWait дважды: сначала для ожидания загрузки всех товаров, 
а затем для ожидания появления секретного сообщения.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.5.3/index.html')
#     chrome.find_element(By.ID, 'showProducts').click()
#     WebDriverWait(chrome, 15).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'product')))
#     summ = 0
#     time.sleep(5)
#     for i in chrome.find_elements(By.CLASS_NAME, 'price'):
#         summ += int(i.text.replace('$', ''))
#     chrome.find_element(By.ID, "sumInput").send_keys(summ)
#     chrome.find_element(By.ID, 'checkSum').click()
#     time.sleep(5)
#     print(chrome.find_element(By.ID, 'passwordBlock').text)

"""
📈 Мониторинг курса валют 
🔹 Задача: Получить секретный код, который появляется при достижении курсом доллара определенного значения.
1️⃣ Запустите Selenium и откройте сайт-тренажёр с мониторингом курса валют.
2️⃣ Дождитесь, когда курс доллара (USD) достигнет значения "75.50 ₽".
3️⃣ После достижения целевого курса дождитесь появления элемента с секретным кодом.
4️⃣ Извлеките секретный код из элемента.
5️⃣ Вставьте полученный секретный код в поле ниже на платформе Stepik.
🟢 Важно:

Секретный код появится только при использовании Selenium.
Курс доллара постепенно растет до достижения целевого значения.
Элемент с секретным кодом добавляется в DOM динамически только после достижения целевого курса.
Для успешного решения задачи необходимо использовать два типа ожиданий: 
ожидание текста в элементе и ожидание появления нового элемента.
💡 Подсказка:
Если секретный код не появляется, попробуйте увеличить таймаут в WebDriverWait.
Обратите внимание на ID элементов: "usd-rate" для курса доллара и "secret-code" для секретного кода.
Используйте .text_to_be_present_in_element()
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.6.1/index.html')
#     try:
#         WebDriverWait(chrome, 35).until(EC.text_to_be_present_in_element((By.ID, 'usd-rate'), '75.50 ₽'))
#         print(chrome.find_element(By.ID, 'code-container').text)
#     except TimeoutError:
#         print('TimeOut')

"""
 🧪 Забытый рецепт
🔹 Задача: Геральт из Ривии не может вспомнить название редкого эликсира, 
который ему срочно нужно приготовить перед охотой на чудовище. 
Его друг Лютик может помочь вспомнить название, но ему потребуется время. Ваша задача - дождаться, 
когда Лютик полностью вспомнит название эликсира, и получить секретный пароль для подтверждения задания.
1️⃣ Запустите Selenium и откройте сайт-тренажёр с книгой алхимических рецептов Геральта.
2️⃣ Нажмите на кнопку "Попросить Лютика вспомнить название эликсира".
3️⃣ Дождитесь, когда в поле ввода полностью появится текст "Селениумий".
4️⃣ После появления полного названия эликсира дождитесь появления элемента с секретным паролем.
5️⃣ Извлеките секретный пароль из элемента.
6️⃣ Вставьте полученный пароль в поле ниже на платформе Stepik.
🟢 Важно:
Секретный пароль появится только при использовании Selenium WebDriver.
Лютик вспоминает название эликсира постепенно, по одному символу.
Элемент с секретным паролем добавляется в DOM динамически только после того, как название эликсира будет полностью введено.
Для успешного решения задачи необходимо использовать метод 
text_to_be_present_in_element_value() для ожидания появления полного текста в поле ввода.
💡 Подсказка:
Если секретный пароль не появляется, попробуйте увеличить таймаут в WebDriverWait.
Обратите внимание на ID элементов: "recipe_field" для поля с названием эликсира и "password" для секретного пароля.
Для ожидания появления полного текста в поле ввода используйте EC.text_to_be_present_in_element_value().
Для ожидания появления элемента с паролем используйте EC.visibility_of_element_located().
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.6.2/index.html')
#     chrome.find_element(By.ID, 'ask-jaskier').click()
#     try:
#         WebDriverWait(chrome, 40).until(EC.text_to_be_present_in_element_value((By.ID, 'recipe_field'), 'Селениумий'))
#     except TimeoutError:
#         print('TimeOutError')    

#     try:
#         WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
#         print(chrome.find_element(By.ID, 'password').text)
#     except TimeoutError:
#         print('TimeOutError') 


"""
🔥 Активация нанокостюма: докажи, что ты достойный! 🦾
🔹 Задача: Твой костюм Железного Человека не активирован! 
Он заряжается нестабильным источником энергии, и никто не знает, когда он будет полностью готов. 
Когда уровень заряда станет достаточным, атрибут изображения костюма изменится. 
Дождаться полной зарядки костюма и получить секретный пароль.
1️⃣ Открыть сайт-тренажёр через Selenium.
2️⃣ Использовать WebDriverWait + EC.text_to_be_present_in_element_attribute(), 
чтобы дождаться изменения атрибута src у изображения костюма (он изменится на success).
3️⃣ После изменения кликнуть по костюму, чтобы активировать его.
4️⃣ Если активация успешна, на сайте появится секретный пароль.
5️⃣ Извлечь пароль и вставить его в поле ниже на Stepik.
🟢 Важно:
Атрибут src изменяется случайно в течение 5-15 секунд.
Если ты просто подождёшь sleep(10), можешь не успеть — нужно использовать WebDriverWait!
 Не угадывай! Если попробуешь кликнуть раньше — костюм не запустится.
Не используйте методы скрытия Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.6.3/index.html')
#     try:
#         WebDriverWait(chrome, 20).until(EC.text_to_be_present_in_element_attribute((By.ID, 'main-image'), 'class', 'charged'))
#         chrome.find_element(By.ID, 'main-image').click()
#         time.sleep(5)
#         print(chrome.find_element(By.ID, 'password-section').text)      
#     except TimeoutError:
#         print('TimeoutError')  


"""
🔥 Миссия "Подтверждение бронирования": докажи, что ты мастер ожидания! 🧙‍♂
🔹 Задача: Твоё бронирование находится в подвешенном состоянии! 
Система обрабатывает данные, и никто не знает, когда она подтвердит твой номер. 
Когда обработка завершится, у элемента с номером бронирования появится атрибут "confirmed". 
Твоя задача - дождаться подтверждения и получить секретный пароль.
1️⃣ Открыть сайт-тренажёр через Selenium.
2️⃣ Используйте WebDriverWait и element_attribute_to_include, 
чтобы дождаться появления атрибута "confirmed" у элемента с id="booking-number".
3️⃣ После появления атрибута введите номер бронирования, отображаемый на странице, в соответствующее поле.
4️⃣ Нажмите кнопку "Проверить статус".
5️⃣ Извлечь пароль и вставить его в поле ниже на Stepik.
🟢 Важно:
Ввод номера бронирования должен происходить только после появления атрибута "confirmed".
Не используйте методы скрытия Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.6.4/index.html')
#     WebDriverWait(chrome, 20).until(EC.element_attribute_to_include((By.ID, 'booking-number'), 'confirmed'))
#     time.sleep(5)
#     text = chrome.find_element(By.ID, 'booking-number').text
#     chrome.find_element(By.ID, 'booking-input').send_keys(text)
#     chrome.find_element(By.ID, 'check-button').click()
#     print(chrome.find_element(By.ID, 'secret-password').text)


"""
🛒 Оформление заказа с многоступенчатой загрузкой
🔹 Задача: Получить секретный код подтверждения, который появляется после успешного оформления заказа.
1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ Заполните форму заказа:
Введите адрес доставки (минимум 5 символов)
Выберите способ оплаты из выпадающего списка(.click())
3️⃣ Нажмите кнопку "Подтвердить заказ" и дождитесь исчезновения спиннера загрузки.
4️⃣ В появившемся модальном окне нажмите кнопку "Да" для подтверждения адреса и дождитесь исчезновения модального окна.
5️⃣ Нажмите кнопку "Получить код подтверждения", которая появится после закрытия модального окна.
6️⃣ Извлеките секретный код из элемента с ID "result".
7️⃣ Вставьте полученный секретный код в поле ниже на платформе Stepik.
🟢 Важно:
Секретный код появится только при использовании Selenium
Спиннер загрузки отображается случайное время (3-7 секунд).
Модальное окно закрывается через случайное время (2-4 секунды) после нажатия кнопки "Да".
Для успешного решения задачи необходимо использовать ожидания исчезновения элементов.
💡Подсказка:
Используйте EC.invisibility_of_element_located() для ожидания исчезновения спиннера и модального окна.
Используйте EC.element_to_be_clickable() для ожидания возможности клика по кнопкам.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.7.1/index.html')
#     chrome.find_element(By.ID, 'address').send_keys('Москва')
#     chrome.find_element(By.ID, 'payment').click()
#     chrome.find_element(By.XPATH, '//*[@id="payment"]/option[2]').click()
#     chrome.find_element(By.ID, 'submit-order').click()
#     WebDriverWait(chrome, 10).until(EC.invisibility_of_element_located((By.ID, 'spinner')))
#     chrome.find_element(By.ID, 'confirm-address').click()
#     WebDriverWait(chrome, 10).until(EC.invisibility_of_element_located((By.ID, 'modal')))
#     WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.ID, 'get-code')))
#     chrome.find_element(By.ID, 'get-code').click()
#     print(chrome.find_element(By.ID, 'result').text)


"""
🔍 Поиск с динамическим обновлением результатов 
🔹 Задача: Получить секретный пароль, который появляется после обновления результатов поиска.
1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ Выполните поиск:
Введите любой поисковый запрос в поле ввода (например, "test")
Нажмите кнопку "Поиск в Fungle"
3️⃣ Дождитесь появления старого результата с обратным отсчётом и сохраните ссылку на этот элемент. Он находиться в элементе div id="old-result"
4️⃣ Дождитесь, пока старый результат полностью исчезнет из DOM (когда обратный отсчёт дойдёт до 0).
5️⃣ В появившемся новом результате нажмите кнопку "Показать секрет"
6️⃣ Извлеките секретный пароль из элемента с ID "result".
7️⃣ Вставьте полученный секретный пароль в поле ниже на платформе Stepik.
🟢 Важно:

Секретный код появится только при использовании Selenium
Старый результат исчезает через 5 секунд после появления.
Новый результат появляется сразу после исчезновения старого.
💡Подсказка:
Используйте EC.staleness_of() для ожидания полного исчезновения старого результата из DOM.
Используйте EC.element_to_be_clickable() для ожидания возможности клика по кнопке "Показать секрет".
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.7.2/index.html')
#     chrome.find_element(By.CLASS_NAME, 'search-box').send_keys('test')
#     chrome.find_element(By.ID, 'search-button').click()
#     WebDriverWait(chrome, 10).until(EC.staleness_of(chrome.find_element(By.ID, 'old-result')))
#     WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.ID, 'secret-button'))).click()
#     chrome.find_element(By.ID, 'secret-button').click()
#     print(chrome.find_element(By.ID, 'result').text)


"""
🕰️ Окно возможностей: лови момент! 
🔹 Задача: Получить секретный пароль, который появляется при открытии определенного количества окон.
1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ После нажатия на кнопку "Призвать страницу" с рандомной задержкой начнут открываться новые окна в новых вкладках. 
Вам не нужно работать с фокусом. Визуально вы будете находиться на шаблоне новой странице, но в коде работать с главной страницей.
3️⃣ Дождитесь, пока откроется ровно 5 окон (включая основное). 
4️⃣ Нажмите кнопку "Выдать пароль" в момент, когда открыто ровно 5 окон.
5️⃣ Извлеките секретный пароль из появившегося alert-сообщения.(alertтоже всплывает с задержкой 2-5 сек)
6️⃣ Вставьте полученный пароль в поле ниже на платформе Stepik.
🟢 Важно:
Секретный пароль и открытие вкладок работает только при использовании Selenium WebDriver
Окна открываются с разной скоростью (от 1 до 1.5 секунд между окнами)
Между 4-м и 5-м окном есть пауза (2-3 секунды)
После 5-го окна продолжают открываться дополнительные окна
Пароль будет выдан только если нажать на кнопку "Выдать пароль" когда открыто ровно 5 окон
Если нажать на кнопку раньше, появится сообщение "Рано!"
Если нажать на кнопку позже, появится сообщение "Поздно!"
💡Подсказка:
Используйте WebDriverWait с методом number_of_windows_to_be(5) для точного определения момента, когда открыто ровно 5 окон
Используйте poll_frequency=0.01 для более частой проверки условия
Используйте EC.alert_is_present() для ожидания появления alert с паролем
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/9/9.7.3/index.html')
#     chrome.find_element(By.ID, 'summonBtn').click()
#     WebDriverWait(chrome, 10, poll_frequency=0.01).until(EC.number_of_windows_to_be(5))
#     chrome.find_element(By.ID, 'passwordBtn').click()
#     alert = WebDriverWait(chrome, 10).until(EC.alert_is_present())
#     text = alert.text
#     alert.accept()
#     print(text)



# ЗАДАЧИ ПО РАЗДЕЛУ 9 !!!!!!!!!!

"""
⏳ Ожидание title
Вам поручили важное дело. Ваш источник сообщил о сайте, 
на котором спрятан код, который может открыть доступ к ценной информации. 
Однако этот код не так просто забрать!
Вход на сайт: Откройте загадочный сайт с помощью Selenium.
Ожидание: На сайте есть кнопка, но она не активна сразу. 
Она "пробуждается" в случайный момент времени, в течение 1-3 секунд после загрузки.
Быстрый рефлекс: После нажатия на эту кнопку, начните наблюдение за заголовком страницы (title). 
Он будет меняться, и вам нужно действовать стремительно!
Момент правды: Когда заголовок страницы станет "345FDG3245SFD", быстро извлеките код из элемента с id="result".
Финиш: Завершите задачу, вставив полученный код в поле для ответа. 
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/expectations/3/index.html')
#     btn = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.ID, "btn")))
#     btn.click()
#     WebDriverWait(chrome, 30).until(EC.title_is("345FDG3245SFD"))
#     password = chrome.find_element(By.ID, "result").text
#     print(password)
    

"""
🕵️‍♂️ Тайный заголовок
Говорят, что в сети интернет существуют скрытые порталы, доступ к которым можно получить только зная определенный код. 
Этот код спрятан на одной из страниц, и ваша задача – найти его.
Начало пути: Запустите браузер с помощью Selenium и посетите таинственный сайт.
Терпение – ключ к успеху: Обратите внимание на кнопку, которая оживает после загрузки страницы. 
Время, которое потребуется для её активации, варьируется от 1 до 3 секунд.
Секретные коды: Нажмите на кнопку, и начните слежение за заголовком страницы. 
Коды будут мелькать в этом заголовке с промежутками от 0,1 до 0,6 секунды.
Открывайте глаза: Ваша цель - не просто просмотреть коды. Вам нужно отловить тот момент, когда в заголовке появится фраза "JK8HQ".
Секретный знак: При обнаружении этой фразы в заголовке, используйте знакомый вам метод title_contains('JK8HQ'). 
Если он вернет True, сохраните полный текст этого заголовка.
Финальный шаг: Представьте найденный вами заголовок в качестве ответа на задачу.
"""    
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/expectations/4/index.html')
#     btn_generator = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.ID, "btn")))
#     btn_generator.click()
#     WebDriverWait(chrome, 30, poll_frequency=0.1).until(EC.title_contains("JK8HQ"))
#     print(chrome.title)


"""
🌬️ Мимолётные теги
В мире программирования каждая строчка кода имеет свою ценность. 
Но где-то там, в глубине интернет-пространства, находятся символы, обладающие особым значением. 
Эти символы — ключ к мастерству, и только истинный программист сможет их найти. Готовы ли вы принять вызов?
Задание:
Врата в Неизведанное: Ваше путешествие начнется с открытия сайта с помощью Selenium. На этом сайте вас ждет кнопка.
Танец Элементов: После нажатия на эту кнопку, страница начнет игру с вами — на экране появится множество элементов с различными классами.
Испытание Откровения: Среди этого множества элементов вашей задачей будет отыскать тот единственный, 
который мерцает классом "BMH21YY". Но не пытайтесь обмануть судьбу, 
делая это вручную — ваша цель — применить метод presence_of_element_located(locator) и дождаться момента его появления.
Секретные Глифы: Как только этот таинственный элемент обнаружен, извлеките его содержимое и внесите в поле для ответа.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/expectations/6/index.html')
#     btn_generator = WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
#     text = WebDriverWait(chrome, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "BMH21YY"))).text
#     print(text)


"""
🔍 Охота на таинственный Блок
В неком виртуальном мире есть сайт, который, по слухам, является порталом к забытым знаниям. 
На этом сайте происходят невероятные вещи: блоки появляются и исчезают, словно духи в старом особняке. 
Особенный из них – ключ к забытому сокровищу.

Задание:
Портал В Неизвестное: Ваш первый шаг - зайти на сайт и стать свидетелем этого волшебства: блоки появляются и исчезают, как призраки.
Легенда о Таинственном Блоке: Среди множества блоков есть один особенный. Его ID "qQm9y1rk", и он – ключ к забытым знаниям.
Сражение с Временем: Проблема в том, что никто не знает, когда и где этот блок решит показать себя. 
Он может мелькнуть на долю секунды или вовсе остаться в тени. Но если вы его увидите, действуйте быстро!
Ключевой Момент: Как только вы обнаружите блок с ID "qQm9y1rk", мгновенно кликните по нему. 
Ведь этот блок не привык к вниманию и быстро исчезнет.
Сокровище Знаний: Если вам удастся кликнуть по блоку, вы будете вознаграждены: 
в alert-окне появится секретный код, который приведет вас к решению задачи.
Совет: Не дайте себя увлечь этим магическим балетом блоков. Сосредоточьтесь на своей цели, и сокровище будет вашим!

Подсказка:
EC.presence_of_element_located
# или
EC.presence_of_all_elements_located
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.9/2/index.html')
#     WebDriverWait(chrome, 30, poll_frequency=0.1).until(EC.presence_of_element_located((By.ID, "qQm9y1rk"))).click()
#     alert = chrome.switch_to.alert
#     text = alert.text
#     print(text)
#     alert.accept()


"""
🧠 Познание атрибута display
В глубинах Вселенной интернета находится загадочный Замок Семи Порталов. 
В каждом портале замка скрыт фрагмент древнего кода. 
Но не все порталы откроются с первой попытки. Вам предстоит проявить ловкость и внимательность, чтобы отыскать все части кода.

Задание:
Загадочный Замок: Начните свою экспедицию, открыв сайт с помощью Selenium. 
Таинственные Блоки: Блоки с появляются благодаря магии атрибута display. 
Ваш щит и меч в этом бою – метод EC.visibility_of(element) или EC.visibility_of_element_located(locator)
Карта Ключей: С вами список ID ids_to_find. 
Эти ID – не просто случайные символы, это карта к древнему коду, 
вам необходимо дождаться появления и кликнуть по блокам именно с этими ID.

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', 
'8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw', 
'25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
              
Испытание Ловкости: Но будьте внимательны! Каждый клик вне списка ids_to_find обнуляет ваши успехи, 
и вам придется начать все сначала. Так что меряйте семь раз, прежде чем кликнуть!
Испытание Терпения: Остерегайтесь ловушек! Каждый элемент на вашем пути может появиться в самый неожиданный момент. 
Ваша задача – быть настороже и дождаться момента, когда ключевые элементы покажут себя.
Секретный Код: Если вы правильно активируете все нужные порталы, 
перед вами раскроется алерт с древним кодом. Этот код – залог вашего успеха в решении задачи.
Совет: Помните, каждый шаг на пути к коду требует вашего внимания и терпения. 
Не унывайте, если не удастся сразу разгадать все тайны. Великие знания требуют великих усилий!
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.9/3/index.html')
#     ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 
#                    'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw', 
#                    '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
#     wait = WebDriverWait(chrome, 50)
#     for id in ids_to_find:
#         locator = (By.ID, f'{id}')
#         wait.until(EC.visibility_of_element_located(locator)).click()
#     alert = wait.until(EC.alert_is_present())
#     print(chrome.switch_to.alert.text)



"""
📢 Триумф над рекламным Заговором
В мире интернета рекламные баннеры зачастую становятся источником раздражения и отвлекают нас от главной цели. 
Но сегодня у вас есть шанс взять реванш и показать, что выше любой хитрости и уловок.

Миссия:
Врата Веба: С помощью Selenium, откройте сайт, который является ареной вашего сражения.
Баннер Ненависти: Как только страница откроется, вас встретит назойливый рекламный баннер, 
покрывающий собой содержимое сайта. Ваша цель — дождаться появления крестика закрытия страницы(5 секунд) и нажать его.
Терпение и Внимание: Однако, этот баннер обладает способностью исчезать в течении длительно времени, 
не давая вашему скрипту добраться до цели сразу. Вам нужно проявить терпение и внимание, 
чтобы дождаться момента, когда баннер наконец исчезнет полностью. 
Используйте .invisibility_of_element_located() из прошлого степа, чтобы удостовериться в его исчезновении.
Финальный Клик: После того как баннер исчезнет, ваш путь будет свободен. 
Найдите кнопку, которая теперь доступна для нажатия, и кликните по ней, чтобы раскрыть секретное значение.
Секретный код появиться только при использовании Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.9/4/index.html')
#     WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.ID, 'closeBtn'))).click()
#     WebDriverWait(chrome, 10).until(EC.invisibility_of_element_located((By.ID, 'ad')))
#     WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, '//button'))).click()
#     print(chrome.find_element(By.ID, 'message').text)


"""
📜 Коллекционер секретных рун
В мире веб-путешествий вы встретили магическую страницу, охраняемую девятью рунными-стражами. 
Каждый из стражей хранит уникальный секрет, но не торопитесь – за секретами следят назойливые стражи-рекламы.
Задание:

Первый Шаг: Откройте таинственный сайт с помощью Selenium, готовьтесь встретиться лицом к лицу с девятью рунными-стражами.
Битва с Рекламой: Нажмите на любую кнопку, и как только это произойдет, перед вами появится назойливое рекламное окно. 
Ваша задача – быстро и решительно закрыть его, не давая ему нарушить ваш путь к секретам.
Поиски Секретов: Как только реклама будет побеждена, обратите внимание на кнопку, которую вы только что освободили. 
На ней появятся подобные символы "01V5" – фрагмент древнего кода.
Создание Ключа: Скопируйте символы и соберите из них длинный ключ в формате "YS93-R9R3-S019-PPI7-OS80-012C". 
Разделители "-" помогут вам организовать код и сделать его готовым к использованию.
Порядок: Кликать можно в любом порядке, но собирать и "склеивать" его, необходимо в определённом порядке.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# code = ''
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.9/5/index.html')
#     btns = chrome.find_elements(By.CLASS_NAME, 'box_button')
#     for btn in btns:
#         btn.click()
#         chrome.find_element(By.ID, 'close_ad').click()
#         time.sleep(7)
#         code += btn.text + '-'
#     print(code)    


"""
✨ Мерцающий Чек Бокс Мистерии
Добро пожаловать в мир непредсказуемости и волшебства Selenium! 
Сегодня ваш путь ляжет через веб-страницу, полную таинств и секретов. 
Ваш путеводитель - с вами, а ваша задача - покорить Мерцающий Чек Бокс Мистерии.

Задание:
Вход в Мир Таинства: Используйте Selenium для открытия указанного сайта 
и подготовьтесь к встрече с чек боксом, обладающим свойствами непредсказуемости.
Погоня за Мгновением: Чек бокс, который вы встретите, 
обладает уникальной способностью внезапно появляться и исчезать. 
Он не любит, когда его ловят на месте, и потому ваша задача - быть настолько внимательным 
и быстрым, чтобы ухватить его в момент активации.
Методы Ожидания: Вооружитесь методами ожидания Selenium, 
ибо только они помогут вам в этой неравной битве со временем и неопределенностью. 
Дождитесь момента, когда чек бокс активируется, и в тот же миг нажмите на кнопку "Проверить".
.element_to_be_selected()
# ИЛИ
.element_located_to_be_selected()
            
Доказательство Мастерства: Если вы справитесь с задачей, и проверка пройдет успешно, 
вы получите секретный код. Код, который станет вашим трофеем и доказательством того, 
что даже в мире неопределенности вы можете найти уверенность и решимость.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.9/6/index.html')
#     WebDriverWait(chrome, 10).until(EC.text_to_be_present_in_element_attribute((By.ID, 'myCheckbox'), 'class', 'active'))
#     chrome.find_element(By.XPATH, '//button').click()
#     print(chrome.find_element(By.ID, 'result').text)


"""
🎄 Гирлянда чекбоксов
Добро пожаловать в мир, где элементы интерфейса ведут себя как огоньки на новогодней елке, 
мерцая и играя в непредсказуемом танце. Ваша задача на этот раз - стать частью этого танца, 
используя инструменты Selenium.

Задание:
Вход в Светящийся Мир: Откройте сайт с помощью Selenium и подготовьтесь к встрече с чек боксами и кнопками, 
которые готовы вас встретить в своем танце мерцания.
Поиск Своей Пары: В этом танце каждая кнопка имеет свою пару - чек бокс. 
Ваша задача - следить за этими парами и ловить момент, когда чек бокс рядом с кнопкой перейдет в состояние "checked".
Точное Время для Действия: Как только вы заметите, что чек бокс активировался, 
немедленно кликайте по соответствующей кнопке. 
Будьте внимательны и быстры, ведь светящиеся элементы не терпят медлительности.
Поиски Секретного Кода: После успешного клика по каждой кнопке, извлеките секретный код, 
который откроется перед вами в теге <p id="result"></p> . 
Этот код - ключ к разгадке загадки и ваш билет к следующему этапу приключения.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.9/7/index.html')
#     wait = WebDriverWait(chrome, 15)
#     checkboxes = chrome.find_elements(By.TAG_NAME, 'input')
#     buttons = chrome.find_elements(By.TAG_NAME, 'button')
#     for checkbox, button in zip(checkboxes, buttons):
#         if wait.until(EC.element_to_be_selected(checkbox)):
#             button.click()
#     print(wait.until(EC.visibility_of(chrome.find_element(By.ID, 'result'))).text)

