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


"""
 Модальные окна.
🔹 Задача: Получить секретный пароль через правильное взаимодействие с различными типами модальных окон.
1️⃣ С помощью Selenium зайдите на сайт-тренажер.
2️⃣ На главной странице находятся три кнопки, каждая из которых вызывает модальное окно.
3️⃣ Выполните следующие действия:
Для окна Alert – кликните по кнопке и вызовите метод accept(), чтобы закрыть окно.
Для окна Prompt – кликните по соответствующей кнопке, 
введите точный текст «Alert»(не текст из окна Alert, а просто слово Alert) через .send_keys() , затем подтвердите ввод методом .accept()
Для окна Confirm – кликните по кнопке и нажмите ОК
4️⃣ Если все модальные окна обработаны правильно, на странице динамически отобразится секретный пароль.
5️⃣ Считайте пароль из DOM и вставьте его в поле ниже на платформе Stepik.
🟢 Внимание: Пароль отобразится только при использовании Selenium для автоматизации взаимодействия с модальными окнами.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/8/8.3.1/index.html')
#     chrome.find_element(By.ID, 'alertButton').click()
#     alert = chrome.switch_to.alert
#     alert.accept()
#     time.sleep(1)

#     chrome.find_element(By.ID, 'promptButton').click()
#     prompt = chrome.switch_to.alert
#     prompt.send_keys('Alert')
#     prompt.accept()
#     time.sleep(1)

#     chrome.find_element(By.ID, 'confirmButton').click()
#     confirm = chrome.switch_to.alert
#     confirm.accept()
#     time.sleep(5)

#     secret_key = chrome.find_element(By.XPATH, '//*[@id="secretKey"]').text
#     print(secret_key)


"""
👨‍💻 Работа с iFrame.
🔹 Задача: Извлечь спрятанное слово из iFrame, переключившись в него с помощью Selenium.
1️⃣ С помощью Selenium зайдите на сайт-тренажер.
2️⃣ На главной странице отображается iFrame с вложенным контентом.
3️⃣ Выполните следующие действия:

Найдите элемент iFrame и переключитесь в него, используя browser.switch_to.frame().
Получите HTML-код содержимого iFrame (browser.page_source).
Извлеките слово, спрятанное между символами * внутри текста.
(Например, в тексте могут встречаться разбросанные буквы *F*, *s* и т. д. 
Вам нужно извлечь каждую букву по порядку и соединить их воедино.)
4️⃣ Вставьте полученное слово в поле ниже на платформе Stepik.
🟢 Внимание: Секретное слово имеет формат СловоСлово — это два разных слова, начинающихся с большой буквы, без пробела.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# import re
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/8/8.4.1/')
#     iframe = chrome.find_element(By.XPATH, '//iframe')
#     chrome.switch_to.frame(iframe)

#     iframe_context = chrome.page_source
#     text = re.findall(r'\*(.*?)\*', iframe_context)
#     final_text = ''.join(text)
#     print(final_text)


"""
Туда и обратно.
🔹 Задача: Помогите Морфиусу, сделать первый звонок Нео, найдите пароль от матрицы. 
Учимся переключаться на фреймы, затем возвращаться к основному контенту.
1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
2️⃣ На главной странице находится iframe 1, внутри которого расположена кнопка, 
при нажатии на которую, появиться следующий iframe 2, 
внутри которого так же будет кнопка при нажатии которой появляется новый iframe 3, 
и так до iframe 4 в котором будет лежать пароль.
3️⃣ Для каждого iframe выполните следующие действия:
🔹 Переключитесь в iframe 1 .switch_to.frame(тут селектор iframe) и нажмите кнопку «Разблокировать следующий уровень».
🔹 Вернитесь в основной контент .switch_to.default_content(), затем переключитесь в iframe 2 и снова нажмите кнопку.
🔹 Повторите процесс для iframe 3.
🔹 После активации iframe 4, получите секретный пароль, который появится на экране.
4️⃣ Считайте код из DOM и вставьте его в поле ниже на платформе Stepik.
🟢 Внимание: Пароль отобразится только при использовании Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/8/8.4.2/index.html')
#     frames_list = ['frame1', 'frame2', 'frame3']
#     for frame in frames_list:
#         chrome.switch_to.frame(frame)  # если у frame есть атрибут id или name, то можно к этому фрэйму обращаться прям вот так
#         chrome.find_element(By.CLASS_NAME, 'unlock-button').click()
#         chrome.switch_to.default_content()
#         time.sleep(1)

#     chrome.switch_to.frame('frame4')
#     secret_key = chrome.find_element(By.XPATH, "/html/body/h2").text
#     print(secret_key)    


"""
Вложенные iframes: путь вглубь… 🌀
🔹 Задача: Пробраться сквозь лабиринт вложенных iframes и добыть секретный пароль в виде фразы, 
которую произносят вновь прибывшие при посвящении в адепты iframe!

1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ На главной странице расположен iframe 1. 
Переключитесь в iframe 1 с помощью .switch_to.frame(...) и нажмите кнопку. 
Внутри iframe 1 динамически погрузится iframe 2.
3️⃣ Повторите действия, добравшись до iframe 4. 
В iframe 4 спрятан пароль. Найдите его и заберите! 🏆
4️⃣ Считайте фразу-пароль и вставьте её в поле ниже на платформе Stepik.
🟢 Внимание: Пароль отобразится только при использовании Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/8/8.4.3/index.html')

#     frame1 = chrome.find_element(By.CLASS_NAME, 'frame')
#     chrome.switch_to.frame(frame1)
#     chrome.find_element(By.CLASS_NAME, 'button').click()

#     frame2 = chrome.find_element(By.XPATH, '//iframe')
#     chrome.switch_to.frame(frame2)
#     chrome.find_element(By.CLASS_NAME, 'button').click()

#     frame3 = chrome.find_element(By.XPATH, '//iframe')
#     chrome.switch_to.frame(frame3)
#     chrome.find_element(By.CLASS_NAME, 'button').click()

#     frame4 = chrome.find_element(By.XPATH, '//iframe')
#     chrome.switch_to.frame(frame4)
#     chrome.find_element(By.CLASS_NAME, 'button').click()

#     secret_ket = chrome.find_element(By.CLASS_NAME, 'password-container').text
#     print(secret_ket)

#---------------------------------------------------------------------------------
# ЗАДАЧИ ПО ОКНАМ
"""
🗝️ Поиск секретного кода
В мире программирования и тестирования иногда нас ставят перед загадками и головоломками, 
разгадка которых может открыть новые горизонты знаний или даже вести к сокровищам. 
Сегодня ваша задача — найти секретный код на веб-сайте. 
Но есть подвох: код скрыт среди множества кнопок, и только одна из них может его открыть.

Задание
Запуск: Откройте указанный веб-сайт с использованием Selenium.
Исследование: На странице размещено 100 кнопок. Отправьтесь в путешествие, 
кликая по каждой из них, чтобы понять, какая из них прячет желаемый код.
Обнаружение: При активации правильной кнопки, секретный код появится в теге: <p id="result">Code</p>.
Финальный штрих: Скопируйте этот код и вставьте его в специальное поле для ответа на степик.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.8/1/index.html')
#     btns = chrome.find_elements(By.CLASS_NAME, 'buttons')
#     for btn in btns:
#         btn.click()
#         chrome.switch_to.alert.accept()
#         time.sleep(0.5)
#         if chrome.find_element(By.ID, 'result').text != '':
#             print(chrome.find_element(By.ID, 'result').text)    


"""
💳 Поиск секретных пин-кодов
В мире программирования часто встречаются тайны и загадки, которые ждут своего решения. 
Сегодня вы столкнетесь с одной из таких тайн. 
Представьте себя в роли брутфорса, который ищет секретный пин-код среди множества ложных следов.

Цель
Доступ к месту преступления: Используйте Selenium, чтобы получить доступ к веб-сайту, где спрятаны улики.
Внимательное расследование: На сайте находится 100 кнопок. 
Каждая из них при нажатии активирует всплывающее alert окно с пин-кодом.
Расшифровка: Под кнопками расположено текстовое поле, которое проверяет пин-коды. 
Ваша задача — ввести пин-код и проверить его. Если пин-код верный, вы получите секретный код.
Завершение задачи: Вставьте полученный секретный код в специальное поле для ответа на степик.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.8/2/index.html')
#     btns = chrome.find_elements(By.CLASS_NAME, 'buttons')
#     for btn in btns:
#         pin_code = ''
#         btn.click()
#         alert = chrome.switch_to.alert
#         pin_code = alert.text
#         alert.accept()
#         input_pin_code = chrome.find_element(By.ID, 'input').send_keys(pin_code)
#         btn_check = chrome.find_element(By.ID, 'check').click()

#         if chrome.find_element(By.ID, 'result').text != 'Неверный пин-код':
#             print(chrome.find_element(By.ID, 'result').text)

"""
🕵️‍♂️ Секретный код: Кибер-расследование
Внимание, будущий кибераналитик! Перед вами стоит интересная и несколько запутанная задача, 
связанная с поиском секретного кода.  Вы окажетесь на месте преступления с множеством улик, 
но лишь одна из них окажется правильной. Будьте внимательными и удачи в расследовании!

Цель
Место преступления: Откройте указанный сайт с помощью Selenium.
Улики на месте: На сайте вы найдете список пин-кодов. Однако среди них лишь один правильный.
Расшифровка: Для проверки каждого пин-кода используйте кнопку "Проверить". 
При верном пин-коде вы получите секретный код.
Доклад о проведенной работе: Вставьте полученный секретный код в специальное поле для на степик.
Важные заметки
1. Если в Chrome при вводе текста в prompt значение не отображается визуально — это нормально, 
такая особенность (баг браузера), на работу кода она не влияет.
2. Проанализировав обратную связь студентов, было выявлено, 
что многие из них делают одну и ту же ошибку при попытке отправить пин-код. 
Чтобы избежать этой ошибки, следуйте примеру ниже:

Правильный способ:
for pin in pin_codes:
    extracted_text = pin.text
    browser.send_keys(extracted_text)
           
Неправильный способ:
for pin in pin_codes:
    browser.send_keys(pin.text)
                 
В мире кибербезопасности детали имеют значение. Правильное решение этой задачи покажет вам, 
насколько важно внимание к деталям. Удачи в расследовании, агент! 🔍🔐
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.8/3/index.html')
#     check = chrome.find_element(By.ID, 'check')
#     pins = chrome.find_elements(By.XPATH, '//span')
#     for pin in pins:
#         extracted_text = pin.text
#         check.click()
#         prompt = chrome.switch_to.alert
#         prompt.send_keys(extracted_text)
#         prompt.accept()
#         if chrome.find_element(By.ID, 'result').text != 'Неверный пин-код':
#            print(chrome.find_element(By.ID, 'result').text)


"""
Настройка вьюпорта браузера

Цель: Проанализировать содержимое сайта, имея строгие рамки видимой области браузера.

Шаги к решению:
Инициализация: Запустите браузер через Selenium и загрузите страницу.
Настройка размеров: Откройте окно браузера так, чтобы рабочая (видимая) 
область страницы точно соответствовала 555x555 пикселям. 
Не забудьте учесть размеры рамок и панелей браузера при расчете!
Анализ: Когда условие будет выполнено секретный ключ появится в id="result";
Действие: Извлеките содержимое данного элемента и вставьте в поле для ответа.
Подсказка: Убедитесь, что учли все элементы интерфейса браузера при настройке размера окна. 
Размеры рамок и панелей могут влиять на видимую область, и их необходимо учитывать в вашем решении.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.set_window_size(571, 702) # рамка (16, 147)
#     chrome.get('https://parsinger.ru/window_size/1/')
#     print(chrome.find_element(By.ID, 'result').text)

"""
Поиск секретного сочетания размера окна
Цель: Определить уникальное сочетание размеров из двух списков, которое активирует скрытый контент на странице.

Инициализация: Используя Selenium, откройте заданный сайт.
Анализ списков размеров: У вас есть два списка размеров – window_size_x и window_size_y.

Тестирование: Примените каждое сочетание размеров из этих списков к окну вашего браузера.

Поиск результата: После каждой установки размера проверяйте содержимое элемента с идентификатором id="result" на странице.

Извлечение данных: Как только найдете уникальное сочетание, 
при котором на странице появляется число, скопируйте его и вставьте в поле для ответа.
Подсказка: Размеры рамок и панелей браузера могут влиять на видимую область страницы. 
Убедитесь, что учли этот фактор при настройке размера окна.

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# options = webdriver.ChromeOptions()
# options.add_argument('headless') # запуск драйвера без экрана браузера
# window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# with webdriver.Chrome(options) as chrome:
#         for i in range(len(window_size_x)):
#             for y in range(len(window_size_y)):       
#                 chrome.set_window_size(window_size_x[i]+16, window_size_y[y]+147) # рамка (16, 147)
#                 chrome.get('https://parsinger.ru/window_size/2/index.html')        
#                 if chrome.find_element(By.ID, 'result').text != '':
#                     print(chrome.find_element(By.ID, 'result').text)


"""
Таинственные размеры окна
Для этой задачи потребуется код с прошлого степа.
Откройте сайт с помощью selenium;
У вас есть 2 списка с размера окон size_x и size_y;
Цель: определить размер окна, при котором,  в id="result" появляется число;
Результат должен быть в виде словаря {'width': size_x, 'height': size_y}
ps. При написании кода, учитывайте размер рамок браузера.

Метод .get_window_size() возвращает словарь с размерами окна.
Размеры рамок могут зависеть от вашего разрешения и масштабирования экрана. Задача составлена при 100% масштабировании, 
масштабирование можно проверить в настройках дисплея. 
window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]              
На вход ожидается словарь  {'width': 000, 'height': 000} где размеры указаны без учёта размеров рамок браузера, 
т.е. необходимо указать размер рабочей области браузера.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# options = webdriver.ChromeOptions()
# options.add_argument('headless') # запуск драйвера без экрана браузера
# window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# with webdriver.Chrome(options) as chrome:
#         for i in range(len(window_size_x)):
#             for y in range(len(window_size_y)):       
#                 chrome.set_window_size(window_size_x[i]+16, window_size_y[y]+147) # рамка (16, 147)
#                 chrome.get('https://parsinger.ru/window_size/2/index.html')        
#                 if chrome.find_element(By.ID, 'result').text != '':
#                     print(window_size_x[i], window_size_y[y])


"""
Охотник за загадочными числами
В недрах интернета скрываются многие тайны, и одна из них ждёт вас на этом сайте. 
Вам предстоит взять роль исследователя, добывающего коды из множества вкладок, 
каждая из которых раскрывает лишь часть большой загадки.

Шаги к решению:
Погружение: Откройте сайт с помощью Selenium.
Активация тайных порталов: Нажимая на каждую из 10 кнопок, вы активируете ворота в другую вкладку. 
Это ваш шанс найти одну из частей кода.
Исследование: В каждой новой вкладке ищите в title число — ваш ключ к решению.
Сбор информации: Соберите все 10 чисел и сложите их.
Завершение миссии: Вставьте итоговую сумму в поле для ответа на исходной странице.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# summ = 0
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/blank/3/index.html')
#     btns = chrome.find_elements(By.CLASS_NAME, 'buttons')
#     for btn in btns:
#         btn.click()
#         time.sleep(1)
#         handles = chrome.window_handles
#         chrome.switch_to.window(handles[1])
#         summ += int(chrome.title)
#         chrome.close()
#         chrome.switch_to.window(handles[0])
#         time.sleep(1)

# print(f"Сумма всех title = {summ}")    


"""
🔓 Откройте сокровища интернета 
Цель: Найти скрытые коды на списках сайтов, обработать их и получить конечный результат.

Сюжет: В глубинах интернета расположены сайты, каждый из которых хранит свой уникальный код. 
Этот код – лишь часть большой головоломки, которую вам предстоит разгадать.

Шаги к решению:
Подготовка: Загрузите список сайтов, на которых скрыты коды.
Открытие вкладок: Используя Selenium, откройте каждый сайт в отдельной вкладке.
Поиск кодов: Пройдитесь по всем вкладкам и найдите чекбокс. Нажмите на него, чтобы получить код.
Обработка данных: Для каждого полученного кода найдите его квадратный корень.
Суммирование: Сложите все полученные корни.
Финальное преобразование: Округлите конечную сумму до 9 знаков после запятой.
Результат: Вставьте полученное значение в поле для ответа.
Подсказки:

Верный ответ имеет вид 000000.000000000. Используйте функцию round().
Не ищите лёгких путей! Освоение работы с вкладками – это ключевой навык веб-автоматизации.
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# summ = 0
# sites = ['http://parsinger.ru/blank/1/1.html', 
#          'http://parsinger.ru/blank/1/2.html', 
#          'http://parsinger.ru/blank/1/3.html',
#          'http://parsinger.ru/blank/1/4.html', 
#          'http://parsinger.ru/blank/1/5.html', 
#          'http://parsinger.ru/blank/1/6.html',]
# with webdriver.Chrome() as chrome:
#     for site in sites:
#         chrome.switch_to.new_window('tab')
#         chrome.get(site)
#         chrome.find_element(By.CLASS_NAME, 'checkbox_class').click()
#         result= math.sqrt(int(chrome.find_element(By.ID, 'result').text))
#         summ += result
# print(round(summ, 9))


"""
Погружение во фреймы
Вы — кибердетектив, и перед вами стоит необычная загадка. 
В цифровом мире скрыт ключ к таинственному сейфу. 
Этот ключ спрятан в одной из цифровых комнат — iframe'ах. 
Ваша задача — проявить свои навыки и найти этот ключ. Но будьте осторожны, не каждая комната даст вам ответ!

Цель
Погружение в кибермир: Используя Selenium, перейдите на указанный сайт.
Поиск зеркальных комнат: На сайте вы обнаружите 9 iframe. В каждом из них скрыта кнопка.
Сбор информации: Нажмите на кнопку в каждом iframe, чтобы получить число. 
Но помните, с вероятностью 1/9 это число окажется тем самым ключом к сейфу.
Открытие тайны: Вставьте полученное число в поле для проверки. 
Если удача на вашей стороне, то это число откроет перед вами секретный код в alert.
Вставьте полученный код из alert в поле ответа степик.

Подсказка
# Пареключится на iframe
browser.switch_to.frame(iframe)

# Вернутся к базовому контенту страницы
browser.switch_to.default_content()
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.8/5/index.html')
#     iframes = chrome.find_elements(By.XPATH, '//iframe')
#     for iframe in iframes:
#         chrome.switch_to.frame(iframe)
#         chrome.find_element(By.XPATH, '//button').click()
#         secret_key = chrome.find_element(By.ID, 'numberDisplay').text
#         chrome.switch_to.default_content()
#         input_secret_key = chrome.find_element(By.ID, 'guessInput').send_keys(secret_key)
#         chrome.find_element(By.ID, 'checkBtn').click()
#         try:
#             alert = chrome.switch_to.alert
#             print(alert.text)
#             alert.accept()
#             break
#         except: 
#             chrome.find_element(By.ID, 'guessInput').clear()
