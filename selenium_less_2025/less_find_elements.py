"""
🔹 Задача: На планету Арракис🌕 напали враги. 
Активировать систему экстренной защиты можно лишь по Ключ-Коду🔑 который можно получить нажав кнопку "START" 
на странице активации системы безопасности. 
Проблема в том, что кнопку можно нажать только через автоматизированное ПО. Помогите жителям планеты, спасите их жизни🕊️.
💡 Совет: Не забудьте добавить задержку time.sleep() в ваш код, чтобы успеть скопировать Ключ-Код в ручную.
Вставьте полученный ключ в поле ниже между кавычек.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/3/3.2.1/index.html')
#     btn = chrome.find_element(By.XPATH, '//*[@id="clickButton"]').click()
#     time.sleep(10)


"""
🔹 Задача: Вы стоите перед магической дверью, которая ведёт в другой мир. 
Чтобы открыть её, нужно произнести имя самого могущественного дракона🐉 Дейенерис Таргариен. 
Зайдите на сайт-тренажер и введите имя её самого большого и сильного дракона, чтобы получить ключ. 
Этот ключ нужно ввести здесь, в поле ниже между кавычками.
💡 Совет: не забудьте добавить задержку time.sleep() в ваш код, чтобы успеть скопировать код вручную.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
#     enter_text = chrome.find_element(By.XPATH, '//*[@id="codeInput"]').send_keys('Дрогон')
#     btn_ok = chrome.find_element(By.XPATH, '//*[@id="clickButton"]').click()
#     time.sleep(10)


"""
🔹 Задача: Помогите мини-Том Крузу выполнить не выполнимую миссию! У вас есть всего 1.5 секунды, чтобы это сделать.
1️⃣ Зайдите на сайт-тренажер с помощью Selenium.
2️⃣ Нажмите кнопку "Начать миссию".
3️⃣ Получите пароль, который появится на экране (с помощью метода .text).
4️⃣ Введите этот пароль в поле и нажмите кнопку "Проверить".
5️⃣ Если пароль правильный, появится финальный ключ. Его нужно извлечь из элемента с id="text2". И вставить здесь в поле ниже между кавычек.
💡 Совет: выведите в print() финальный ключ, чтобы потом без проблем ввести его на Stepik.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
#     btn1 = chrome.find_element(By.XPATH, '//*[@id="showTextBtn"]').click()
#     text_after_click_btn1 = chrome.find_element(By.XPATH, '//*[@id="text1"]').text
#     enter_text = chrome.find_element(By.XPATH, '//*[@id="userInput"]').send_keys(text_after_click_btn1)
#     btn2 = chrome.find_element(By.XPATH, '//*[@id="checkBtn"]').click()
#     text_after_click_btn2 = chrome.find_element(By.XPATH, '//*[@id="text2"]').text
#     print(text_after_click_btn2)


"""
🔹 Задача:
Секретный ключ спрятан среди множества кнопок. Найдите нужную кнопку и получите заветный ключ 🔑.
1️⃣ Зайдите на сайт-тренажер с помощью Selenium.
2️⃣ Найдите кнопку по id со значением "secret-key-button".
3️⃣ Кликните по кнопке.
4️⃣ Извлеките значение атрибута data с помощью метода .get_attribute("data").
5️⃣ Вставьте полученный ключ в поле ниже между кавычек.
Совет: выведите извлеченное значение в print(), чтобы потом без проблем ввести его на Stepik.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
#     secret_btn = chrome.find_element(By.ID, 'secret-key-button').click()
#     secret_btn = chrome.find_element(By.ID, 'secret-key-button').get_attribute('data')
#     print(secret_btn)


"""
🔹 Задача: Империя наносит ответный удар. Сосчитайте количество штурмовиков в армии Империи.
1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
2️⃣ Найдите все элементы с тегом <a>.
3️⃣ Пройдитесь по каждому элементу <a> и проверьте значение атрибута stormtrooper. 
Суммируйте все числовые значения атрибута stormtrooper для получения общего количества штурмовиков.
4️⃣ Вставьте полученное значение всех штурмовиков на странице тренажера и нажмите кнопку "Проверить" , 
появится заветный пароль(в виде фразы), считайте его с помощью .text.
5️⃣ Вставьте пароль в поле ниже, между кавычками на Stepik.
💡 Совет: заведите переменную (счетчик) для подсчёта общего количества штурмовиков в армии.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# summ = 0
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/3/3.3.3/index.html#')
#     all_elements = chrome.find_elements(By.XPATH, '//a')
#     for i in all_elements:
#         if i.get_attribute('stormtrooper').isdigit():
#             summ += int(i.get_attribute('stormtrooper'))
            
#     enter_summ = chrome.find_element(By.ID, "inputNumber").send_keys(summ)
#     enter_summ_btn = chrome.find_element(By.ID, "checkBtn").click()
#     secret_key = chrome.find_element(By.ID, 'feedbackMessage').text
#     print(secret_key)    


"""
🔹 Задача: используя каскадный поиск найдите элемент на странице, кликните на него, и считайте появившийся атрибут в теге.
1️⃣ Зайти на сайт-тренажер с помощью Selenium.
2️⃣ Найти родительский элемент с идентификатором parent_id.
3️⃣ Внутри этого родительского элемента найти первый дочерний элемент с классом child_class и кликнуть его.
4️⃣ После клика в этом теге появится атрибут password, считать значение этого атрибута с помощью .get_attribute(), это и будет пароль.
5️⃣ Вставить полученный пароль в поле ниже между кавычек.
💡 Совет: выведите в print() значение атрибута password, чтобы потом без проблем ввести его на Stepik.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
#     parent = chrome.find_element(By.ID, 'parent_id')
#     child = parent.find_elements(By.CLASS_NAME, "child_class")[0].click()
#     child_pass = parent.find_elements(By.CLASS_NAME, "child_class")[0].get_attribute('password')
#     print(child_pass)


"""
🔹 Задача: прокликать все кнопки в блоках, и получить заветный пароль 🔓.
1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
2️⃣ Найти все элементы с class="block".
3️⃣ Пройтись по каждому элементу в цикле и кликнуть кнопку.
4️⃣ После того как все кнопки будут нажаты, появится заветный пароль в теге <password> — считать его с помощью .text.
5️⃣ Вставить полученный пароль в поле ниже, между кавычек.
💡 Совет: выведите в print() считанный пароль из тега <password>, чтобы потом без проблем ввести его на Stepik.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
#     buttons = chrome.find_elements(By.CLASS_NAME, 'button')
#     for btn in buttons:
#         btn.click()
#     passw = chrome.find_element(By.XPATH, "//password").text
#     print(passw)