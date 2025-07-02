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



"""
🔹 Задача: с помощью Selenium выполните прокрутку страницы.
1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
2️⃣ Вычислите высоту страницы.
3️⃣ Прокрутите страницу на значение, полученное в шаге 2.
4️⃣ Извлеките появившийся пароль. Пароль появится в виде текста в элементе с id="secret-container".
5️⃣ Вставьте пароль в поле ниже, между кавычками.
💡 Совет: обязательно добавьте time.sleep() после прокрутки, так как пароль появляется не сразу.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.1/index.html')
#     height = chrome.execute_script("return document.body.scrollHeight") # получение высоты страницы
#     chrome.execute_script(f"window.scrollBy(0,{height})")
#     time.sleep(5)
#     sekret_key = chrome.find_element(By.ID, "secret-container").text
#     print(sekret_key)


"""
🔹 Задача: с помощью Selenium заполните все поля и получите пароль.
1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
2️⃣ Заполните любым текстом каждое появляющееся поле. После ввода текста нажмите Enter, чтобы подтвердить заполнение поля.
3️⃣ После заполнения каждого поля нажмите ArrowDown, чтобы перейти к следующему полю. Новые поля будут появляться динамически.
4️⃣ Повторяйте процесс, пока не будет заполнено 100 полей.
5️⃣ После заполнения всех полей и подтверждения, пароль появится в элементе с id="hidden-password".
6️⃣ Извлеките текст пароля и вставьте его в поле ниже между кавычками.
💡 Совет:  в данном задании можно обойтись без ActionChains. Ну и как обычно выводите пароль в print()
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.2/index.html')
#     for i in range(1, 101):
#         wrapper = chrome.find_element(By.XPATH, f'//div[{i}]/input')
#         wrapper.send_keys(i)
#         wrapper.send_keys(Keys.ENTER)
#         wrapper.send_keys(Keys.ARROW_DOWN)
#     secret_key = chrome.find_element(By.ID, 'hidden-password').text
#     print(secret_key)


"""
🔹 Задача: помогите Питеру Гриффину добраться до бассейна, термометр показывает +35🌡️.
1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
2️⃣ Перетащите мистера Гриффина в бассейн и получите пароль в виде фразы. 
3️⃣ Извлеките текст пароля из появившегося элемента с id="password" и вставьте его в поле ниже между кавычками.
⚠️Внимание перетаскивание работает только через Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.3.1/index.html')
#     griffin = chrome.find_element(By.ID, "draggable")
#     target = chrome.find_element(By.ID, "target")
#     actions = ActionChains(chrome)
#     actions.drag_and_drop_by_offset(griffin, 0, -220).perform()
#     secret_key = chrome.find_element(By.ID, "password").text
#     print(secret_key)


"""
🔹 Задача: учимся даблкликать по элементу. 
1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
2️⃣ Выполните двойной клик по заданному элементу, чтобы получить пароль в виде фразы.
3️⃣ Извлеките текст пароля из появившегося элемента с id="password" и вставьте его в поле ниже между кавычками.
🟢Внимание даблклик сработает только через Selenium.
 Важно: Обычный одиночный клик не сработает! Не пытайтесь обмануть систему. 
 Два последовательных вызова метода click() не генерируют событие dblclick, 
 которое слушается в JavaScript.
Используйте двойной клик (double_click). 🖱️➡️🖱️
"""
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.3.2/index.html')
#     db_click_btn = chrome.find_element(By.ID, "dblclick-area")
#     actions = ActionChains(chrome)
#     actions.double_click(db_click_btn).perform()
#     secret_key = chrome.find_element(By.ID, 'passwordContainer').text
#     print(secret_key)


"""
🔹 Задача: нажмите комбинацию клавиш CTRL + ALT + SHIFT + T, чтобы получить секретный пароль.
1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
2️⃣ Используя метод key_down(), создайте цепочку событий, которая имитирует зажатие клавиш CTRL + ALT + SHIFT + T.
3️⃣ Используя key_up() в той же цепочке событий, отожмите клавиши CTRL + ALT + SHIFT+T
4️⃣ Извлеките пароль из появившегося элемента с атрибутом key="access_code" и вставьте его в поле ниже между кавычками.
🟢Внимание тренажер работает только через Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.3.3/index.html')
#     actions = ActionChains(chrome)
#     actions.key_down(Keys.CONTROL) \
#     .key_down(Keys.ALT) \
#     .key_down(Keys.SHIFT) \
#     .key_down('T') \
#     .key_up(Keys.CONTROL) \
#     .key_up(Keys.ALT) \
#     .key_up(Keys.SHIFT) \
#     .perform()
#     time.sleep(2)
#     secret_key = chrome.find_element(By.XPATH, "//p/span").text
#     print(secret_key)


"""
🔹 Задача: выполните правый клик по заданному элементу, чтобы вызвать кастомное контекстное меню с вариантами. 
Затем  выберите из этого меню пункт "Получить пароль" – именно этот выбор должен привести к появлению секретного пароля.
1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
2️⃣ Используя метод context_click(), выполните правый клик по элементу с id="context-area", чтобы отобразилось кастомное контекстное меню.
3️⃣ В появившемся меню, используя поиск по CSS-селектору, найдите пункт с атрибутом data-action="get_password" и кликните по нему.
4️⃣ Извлеките пароль из появившегося элемента с атрибутом key="access_code" и вставьте его в поле ниже между кавычками.
🟢 Внимание: тренажёр работает только через Selenium — кастомное меню активируется именно при эмуляции правого клика с WebDriver.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.3.4/index.html')
#     btn_for_r_click = chrome.find_element(By.ID, "context-area")
#     actions = ActionChains(chrome)
#     actions.context_click(btn_for_r_click).perform()
#     time.sleep(1)
#     el_menu = chrome.find_element(By.CSS_SELECTOR, '[data-action="get_password"]').click()
#     secret_key = chrome.find_element(By.CSS_SELECTOR, '[key="access_code"]').text
#     print(secret_key)


"""
🔹 Задача: прокрутить оба контейнера до конца и считать пароль.
1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
2️⃣Под каждым контейнером находится статусный блок, который изначально показывает «Статус: не прокручено». 
С помощью ActionChains используя метод отправки клавиши END, прокрутить содержимое каждого контейнера до самого низа. 
Как только содержимое контейнера прокручено до конца, соответствующий статусный блок должен обновиться: 
    текст изменится на «Прокручено!», а фон изменится на зелёный (подсветка).
3️⃣После того как оба контейнера прокручены до конца, ниже появляется блок с секретным паролем. 
Извлеките пароль из элемента, где он отображается (элемент имеет атрибут key="access_code").
4️⃣ Вставьте пароль здесь в поле ниже.
🟢 Внимание:
Данный тренажёр работает только через Selenium – функционал появления пароля активен только если браузер запущен через WebDriver.
💡Подсказка
Для того чтобы END сработал, сначала нужно взять контейнер в фокус, то есть кликнуть по нему:
actions.click(container)...и далее цепочку с END
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.3.5/index.html')
#     actions = ActionChains(chrome)
#     scroll_obj_1 = chrome.find_element(By.ID, "scrollable-container-left")
#     scroll_obj_2 = chrome.find_element(By.ID, "scrollable-container-right")
#     actions.click(scroll_obj_1).send_keys(Keys.END).perform()
#     time.sleep(1)
#     actions.click(scroll_obj_2).send_keys(Keys.END).perform()
#     time.sleep(1)
#     secret_key = chrome.find_element(By.CSS_SELECTOR, '[key="access_code"]').text
#     print(secret_key)


"""
Представьте ситуацию: вы открываете веб-страницу, но нужный элемент отсутствует в DOM-дереве. 
Единственный способ его загрузить — прокрутить страницу вниз, после чего элемент появится в DOM, и с ним можно будет взаимодействовать.
🔹 Задача:
1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
2️⃣ Используя метод scroll_by_amount(x, y), прокрутите страницу вниз и считайте код, который появится спустя 3 секунды.
3️⃣ Прокрутите страницу ещё раз, введите полученный на предыдущем шаге код и нажмите кнопку «Проверить».
4️⃣ Если всё выполнено правильно, появится пароль. Вставьте этот пароль в поле ответа степик.
🟢 Внимание: данный тренажёр работает только через Selenium. Также разрешения могут отличаться — подберите правильный y под себя.
🔥 Пока работу с ожиданиями мы еще не прошли, поэтому работаем через time.sleep(). Кто уже знает, как работать с ожиданиями — welcome! 
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.4.1/index.html')
#     ActionChains(chrome).scroll_by_amount(0, 1000).perform()
#     time.sleep(5)
#     scroll1 = chrome.find_element(By.XPATH, '//div[2]/div').text.replace('Код: ', '')
#     time.sleep(1)
#     ActionChains(chrome).scroll_by_amount(0, 1000).perform()
#     time.sleep(1)
#     input_code = chrome.find_element(By.XPATH, "//div[2]/input").send_keys(scroll1)
#     btn = chrome.find_element(By.XPATH, "//div[2]/button").click()
#     time.sleep(1)
#     secrte_key = chrome.find_element(By.ID, "final-key").text
#     print(secrte_key)


"""
🌌 Кодовое имя: Космическая чистка урана
Космические просторы, бескрайние и непредсказуемые. 
Ваш корабль потерпел крушение, и теперь весь ценный груз — кусочки урана — беспорядочно плавают в открытом космосе. 
Но у вас есть инструменты, чтобы помочь своей команде и вернуть уран обратно.
Используя возможности Selenium, напишите скрипт, который найдет и "соберет" все кусочки урана, кликнув по ним. 
Как только последний кусочек урана будет собран, вы получите в alert секретный код. 
Этот код — ваш билет на базу. Найдите его и используйте.

Задачи:
Стартовая Позиция: Запустите Selenium и откройте данный веб-сайт. Убедитесь, что ваша станция готова к операции.
Сбор Урана: Пройдитесь по каждому кусочку урана на странице и кликните по нему. Это поможет нам вернуть его обратно на корабль.
#Подсказка
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
Получение Секретного Кода: Как только в открытом космосе не останется ни одного кусочка урана, команда пришлёт вам в alert-окне секретный код.
#Подсказка
alert_text = browser.switch_to.alert.text
Финальный Этап: Вставьте полученный секретный код в необходимое поле для завершения операции.
Подсказки и заметки:
Будьте быстрыми и точными. Космос не будет ждать!
Используйте уже знакомые методы поиска элементов в Selenium, чтобы точно найти все кусочки урана.
Удачи курсант!
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.7/1/index.html')
#     uranus_btn = chrome.find_elements(By.XPATH, "//button")
#     for i in uranus_btn:
#         i.click()
#         time.sleep(0.1)
#     alert_text = chrome.switch_to.alert.text   
#     print(alert_text)


"""
Операция: Зелёный Лотос
🕰️ Представьте себе момент, когда время замирает, и все вокруг зависает в ожидании вашего действия. 
Вы стоите перед четырьмя кнопками, каждая из которых — ваш шанс изменить ход событий. 
Но в этой задаче важно не только нажать, но и удерживать. Да-да, вы не ослышались. 

Чтобы пройти эту задачу, вам нужно приручить каждую кнопку, удерживая её до тех пор, пока она не станет зелёной. 
Значение value="N" каждой кнопки указывает на минимальное время в секундах(float()), которое необходимо выдержать.

🔮 Как только все кнопки обретут изумрудный оттенок, ваше терпение будет вознаграждено: 
появится сообщение в alert, скрывающее в себе ключ к следующему испытанию. 
Этот ключ нужно вставить в поле ответа на Stepiк, чтобы продвинуться дальше по курсу.

Задача
Откройте сайт с помощью Selenium.
Найдите все четыре кнопки на странице.
Определите значение value каждой кнопки. Это время, которое необходимо удерживать кнопку.
Как только все кнопки станут зелёными, вы получите сообщение в alert. Скопируйте это сообщение.
Вставьте полученное сообщение в поле ответа на Stepik.
💡Подсказка
Вам потребуется использовать методы вроде ActionChains для удержания кнопки
# Пример
actions.click_and_hold(button).pause(hold_time).release(button).perform()
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.7/5/index.html')
#     actions = ActionChains(chrome)
#     buttons = chrome.find_elements(By.CLASS_NAME, 'timer_button')
#     for btn in buttons:
#         btn_time_pause = float(btn.text)
#         actions.click_and_hold(btn).pause(btn_time_pause).release(btn).perform()
#     alert_text = chrome.switch_to.alert.text   
#     print(alert_text)


"""
♻️ Чётный выбор: Бесконечный чекбоксовый список
🔥 Добро пожаловать, кибернетические ниндзя! 
🐱‍💻 Сегодня перед вами стоит задача, которую можно сравнить с поиском иглы в стоге сена. 
Но не просто иглы, а золотой иглы с серийным номером, затерянной в бездонном океане информации.

🕵️‍♀️ Ваша миссия, если вы примете её, — проникнуть в лабиринт бесконечных чекбоксов, появляющихся как грибы после дождя. 
Каждый чекбокс — миниатюрный замок, открывающийся только при выполнении одного условия: значение его value должно быть чётным.
🚀 Стоит вам ошибиться, и ваша миссия провалена. Но если у вас всё получится, вас ждёт не просто поздравление в чате. 
Внизу появится таинственная кнопка с классом alert_button, дарующая вам секретный код. 
Этот код — ключ к нашей следующей операции, так что, ниндзя, у вас нет права на ошибку.

Задача
Инициализация: Откройте заданный веб-сайт с помощью Selenium.
Бесконечный Скроллинг: На сайте есть блок с бесконечной подгрузкой чекбоксов. Всего 100 контейнеров и в каждом контейнере 10 чек боксов.
Чётный Выбор: Устанавливайте чекбоксы только с чётным значением атрибута value.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.7/4/index.html')
#     div_block = chrome.find_element(By.ID, "main_container")
#     last_len_div_block = chrome.execute_script("return arguments[0].scrollHeight", div_block) # замер высоты окна вначале
#     while True:
#         chrome.execute_script(f"arguments[0].scrollTop = {last_len_div_block}", div_block) # крутим объект 'div_block' на высоту 'last_len_div_block' вниз
#         time.sleep(0.5)
#         new_len_div_block = chrome.execute_script("return arguments[0].scrollHeight", div_block) # новый замер высоты объекта 'div_block'
#         if new_len_div_block == last_len_div_block: # если новая высота равна старой - значит достигни конца скролла объекта
#             chrome.execute_script(f"arguments[0].scrollTo(0,0)", div_block) # скроллим в самый верх объекта
#             time.sleep(1)
#             break
#         last_len_div_block = new_len_div_block 

#     # простановка галочек в нужных инпутах
#     input_list = chrome.find_elements(By.XPATH, '//*[@id="main_container"]//input')
#     for i in input_list:
#         value = int(i.get_attribute('value'))
#         if value % 2 == 0:
#             i.click()
#     time.sleep(1)
#     btn_ok = chrome.find_element(By.CLASS_NAME, 'alert_button').click()
#     alert_text = chrome.switch_to.alert.text   
#     print(alert_text)    


"""
Жми LIKE 👍.Представьте, что вы хотите написать скрипт, который пролайкает все комментарии на странице. 
В этом тренажёре мы воссоздали такую ситуацию и предлагаем вам написать 🤖 скрипт-автолайкер 👍.

🔹 Задача: пролайкать каждую карточку и собрать сумму чисел.
1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
2️⃣ Нажмите лайк на каждой карточке и считайте появившееся число (имеет зеленый цвет).
3️⃣ Вставьте сумму всех считанных чисел в поле ниже на степик, между кавычками.
💡 Вы можете использовать любой метод, который поможет вам достичь желаемых результатов. Удачи 🍀
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/7/7.5/index.html')
#     div_block = chrome.find_element(By.ID, "container")
#     over_sum = 0
#     # часть кода отвечающий за скроллинг 
#     last_len_div_block = chrome.execute_script("return arguments[0].scrollHeight", div_block)
#     while True:
#         chrome.execute_script(f"arguments[0].scrollTop = {last_len_div_block}", div_block)
#         time.sleep(0.5)
#         new_len_div_block = chrome.execute_script("return arguments[0].scrollHeight", div_block) 
#         if new_len_div_block == last_len_div_block:
#             chrome.execute_script(f"arguments[0].scrollTo(0,0)", div_block)
#             time.sleep(0.5)
#             break
#         last_len_div_block = new_len_div_block     
#     # закончили скроллить до конца

#     cards = chrome.find_elements(By.CLASS_NAME, 'card')
#     for card in cards:
#         card.find_element(By.CLASS_NAME, 'like-btn').click()
#         number = card.find_element(By.CLASS_NAME, 'big-number').text
#         over_sum += int(number)
#     print(over_sum)