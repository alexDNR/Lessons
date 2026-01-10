"""
🟥 Перемещение красного блока и поиск секретного токена
В этом увлекательном испытании перед вами откроется мир виртуальных блоков и секретных токенов. 
Мы предлагаем вам не просто решить задачу, а пройти путь от внимательного исследования до получения заслуженной награды. 
Вход в виртуальный мир: Откройте указанный сайт с помощью Selenium, 
и погрузитесь в мир, где ваши действия определяют исход событий.
Задача перемещения: На сайте вас встретят два поля. В одном из них - красный блок, 
который ждет вашей помощи, чтобы пересечь границы и оказаться во втором поле. 
Используйте Selenium для написания скрипта, который аккуратно перетащит красный блок из первого поля во второе.
Появление токена: Как только блок достигнет своей цели, на сцене появится токен - 
символ вашего успеха и умения справляться с задачами. 
Ваша следующая миссия - взять этот токен и вставить его в поле для ответа, чтобы закрепить свою победу.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/draganddrop/1/index.html')
#     el1 = chrome.find_element(By.ID, 'draggable')
#     el2 = chrome.find_element(By.ID, 'field2')
#     action = ActionChains(chrome)
#     action.drag_and_drop(el1, el2).perform()
#     print(chrome.find_element(By.ID, 'result').text)


"""
🟦​ ​​​​​​Путешествие квадрата и проверочные точки
Приветствуем вас в захватывающем испытании, где каждое ваше действие переплетается с философией внимательности и точности. 
Сегодня перед вами стоит задача, которая обогатит ваш опыт работы с Selenium и 
придаст вашим навыкам программирования новую глубину и значимость.

Задание:
Открытие мира: Используйте Selenium для того, чтобы ступить на порог виртуального пространства, 
где синий квадрат ожидает своего часа, чтобы начать своё путешествие.
Синий путник и красные ориентиры: На вашем пути встретятся красные точки, 
которые будут служить ориентирами и проверочными пунктами. 
Ваша задача - написать скрипт, который возьмёт на себя роль проводника, 
и аккуратно и последовательно проведёт синий квадрат через все красные точки, следуя по оси X(слева направо).
Появление токена: После того как последняя красная точка будет покорена, 
на экране появится токен - символ вашего успеха и точности в выполнении задачи.
Завершение миссии: Вставьте полученный токен в поле для ответа, 
тем самым завершив своё путешествие и подтвердив свои навыки владения Selenium.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/draganddrop/3/index.html')
#     box = chrome.find_element(By.ID, 'block1')
#     action = ActionChains(chrome)
#     points = chrome.find_elements(By.CLASS_NAME, 'controlPoint')
#     for point in points:
#         action.drag_and_drop(box, point).release().perform()
#         action.drag_and_drop_by_offset(box, 10, 0).release().perform()
#     print(chrome.find_element(By.ID, 'message').text)    


"""
🟩​​ ​​​​​Движение зелёных квадратов
Вас приветствует уникальный мир, где зелёные квадраты стремятся к своему новому дому - серой области. 
Это не просто задача на перемещение элементов, это путешествие, полное смысла и важных уроков.

Задание:
Встреча с зелёными квадратами: При открытии сайта вы увидите 10 зелёных квадратов, каждый из которых готов к переезду. 
Ваша задача - помочь им в этом.
Путешествие к серой области: Перетаскивайте квадраты один за другим в серую область. 
Обратите внимание, каждый квадрат несет в себе частицу целого, и только объединив их в серой области, 
вы сможете увидеть полную картину.
Получение секретного кода: Как только последний зелёный квадрат окажется в серой области, 
перед вами откроется секретный код. Этот код символизирует успешное завершение задачи и ваше понимание важности каждого шага в путешествии.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.10/2/index.html')
#     action = ActionChains(chrome)
#     btns = chrome.find_elements(By.CLASS_NAME, 'draganddrop')
#     btns_field = chrome.find_element(By.CLASS_NAME, 'draganddrop_end')
#     for btn in btns:
#         action.drag_and_drop(btn, btns_field).release().perform()
#     print(chrome.find_element(By.ID, 'message').text)    


"""
 🟠 Путешествие оранжевого круга
Добро пожаловать в удивительный мир цифрового пространства, 
где каждый элемент имеет свою роль и место. 
Ваш герой сегодня - оранжевый круг, который ждёт своего часа, 
чтобы начать своё путешествие по миру пронумерованных блоков.

Сценарий:
Начало путешествия: Войдите на указанный сайт с помощью Selenium, 
где четыре пронумерованных блока ужe ждут своего героя - оранжевого круга.
Миссия перемещения: Ваша задача - написать скрипт, который возьмёт на себя роль проводника и 
поможет оранжевому кругу посетить каждый из этих блоков, перетаскивая его поочерёдно в каждый из них.
Токен победы: Как только оранжевый круг посетит все блоки, 
на сцене появится токен - символ вашего успеха и завершения миссии. 
Этот токен необходимо будет вставить в поле для ответа, чтобы закрепить ваш успех и завершить задание.
Значение путешествия: Получив токен, вы не просто завершите задачу. 
Вы докажете себе и миру, что способны направлять и поддерживать, 
что у вас есть терпение и внимательность, чтобы помочь даже маленькому оранжевому кругу найти своё место в этом мире.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/draganddrop/2/index.html')
#     action = ActionChains(chrome)
#     circle = chrome.find_element(By.ID, 'draggable')
#     boxs = chrome.find_elements(By.CLASS_NAME, 'box')
#     for box in boxs:
#         action.drag_and_drop(circle, box).release().perform()
#     print(chrome.find_element(By.ID, 'message').text) 


"""
Найдите пару
Добро пожаловать в мир гармонии и цвета, где каждый блок ищет свою пару, 
чтобы создать вместе неповторимую мелодию счастья и равновесия. 
Это не просто задача поиск и соединение элементов, это задача, в которой каждый шаг наполнен смыслом и красотой.

Задание:
Встреча с цветными блоками: Посетите указанный сайт и вы увидите множество цветных блоков, 
каждый из которых ждет своего момента, чтобы встретить свою пару.
Танец пар: Ваша задача - написать скрипт на Selenium, который поможет каждому блоку найти и соединиться со своей парой. 
Пара определяется по цвету блока, и именно цвет будет вашим проводником в этом танце.
Сообщение победы: Как только все пары найдены и соединены, на экране появится сообщение. 
Это сообщение не просто говорит о том, что задача выполнена, 
оно несет в себе глубинный смысл и радость от успешно завершенного путешествия.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.color import Color
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.10/3/index.html')
#     action = ActionChains(chrome)
#     boxs = chrome.find_elements(By.CLASS_NAME, 'draganddrop')
#     box_fields = chrome.find_elements(By.CLASS_NAME, 'draganddrop_end')
#     for box in boxs:
#         box_color = Color.from_string(box.value_of_css_property("background-color")).rgb
        
#         for box_field in box_fields:
#             square_color = Color.from_string(box_field.value_of_css_property("border-color")).rgb
#             if box_color == square_color:
#                 action.drag_and_drop(box, box_field).release().perform()

#     print(chrome.find_element(By.ID, 'message').text) 


"""
📏 Бросок на правильное расстояние
Добро пожаловать в виртуальный сад чудес, полный цветных грядок и загадочных кусочков, 
каждый из которых ищет своё место в этом мире. Здесь, в этом цифровом раю, 
законы физики и пространства играют по своим правилам, и только тот, кто способен понять их язык, сможет достичь успеха.

Открытие мира: Используйте Selenium для того, чтобы открыть сайт.
Миссия броска: В вашем распоряжении 8 кусочков и 8 цветных грядок. 
Каждая грядка обладает своей уникальной чертой - расстоянием, на которое необходимо бросить кусочек, 
чтобы он оказался в своей грядке. Ваша задача - написать скрипт, который с точностью и вниманием к деталям осуществит эти броски.
Код победы: Как только все кусочки окажутся на своих грядках, появится код - 
символ вашего успеха и завершения задачи. Этот код необходимо будет ввести в поле для ответа, чтобы подтвердить вашу победу.
Подсказка:
# Используйте 
.drag_and_drop_by_offset()
# или 
click_and_hold(elem).move_by_offset()
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.10/8/index.html')
#     action = ActionChains(chrome)
#     pieces = chrome.find_elements(By.CLASS_NAME, 'piece')
#     for piece in pieces:
#         action.drag_and_drop_by_offset(piece, int(piece.get_attribute('id').replace('piece_', ''))+10, 0).release().perform()
#         time.sleep(1)
#     print(chrome.find_element(By.ID, 'message').text)     


"""
🕵️‍♂️ Движение слайдеров и тайный код
Приветствуем вас в мире слайдеров и точности, где каждое ваше действие влияет на исход событий. 
Это не просто задача на перемещение ползунков, это задача на внимание, точность и умение видеть детали.

Задание:
Мир слайдеров: Войдите на сайт с помощью Selenium, и вы окажетесь в мире, 
где 10 слайдеров ждут вашего внимания. Они как музыканты в оркестре, 
каждый из которых должен быть настроен точно, чтобы сыграть гармоничную мелодию.
Задача точности: Ваша задача - внимательно и аккуратно передвинуть каждый слайдер на позицию, указанную в правом столбце.                                                                 

Получение сообщения: Как только все слайдеры окажутся на своих местах, на сцене появится сообщение. 
Это сообщение - ключ к решению вашей задачи, тайный код, который откроет перед вами новые горизонты.
Смысл задачи: Получив тайный код, вы не просто выполните задание. 
Вы докажете, что способны работать с точностью ювелира, 
что у вас есть терпение и умение доводить дело до конца, несмотря на все трудности.
Подсказка:

# Получить текущее значение слайдера
current_value = int(slider.get_attribute("value"))

# Увеличиваем значение
slider.send_keys(Keys.ARROW_RIGHT)

# Уменьшаем значение
 slider.send_keys(Keys.ARROW_LEFT)
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/selenium/5.10/6/index.html')
#     action = ActionChains(chrome)
#     sliders = chrome.find_elements(By.CSS_SELECTOR, '.volume-slider')
#     target_values = chrome.find_elements(By.CSS_SELECTOR, '.target-value')

#     for slider, target_value in zip(sliders, target_values):
#         target_value = int(target_value.text)
#         current_value = int(slider.get_attribute('value'))

#         while current_value != target_value:
#             if current_value < target_value:
#                 slider.send_keys(Keys.ARROW_RIGHT)
#                 current_value += 1
#             elif current_value > target_value:
#                 slider.send_keys(Keys.ARROW_LEFT)
#                 current_value -= 1

#     result = chrome.find_element(By.CSS_SELECTOR, '#message').text
#     print(result)


"""
Волшебное слово
Добро пожаловать на цифровое "Поле Чудес"! Здесь не вращают барабан, 
а точность и автоматизация ведут к победе. Это испытание не только для вашего знания Selenium, 
но и для вашей способности управлять хаосом букв.

Задание:
С помощью Selenium распахните врата этого испытания, загрузив страницу тренажера.
В центре внимания – слово, которое вам предстоит собрать. Внимательно считайте его, ведь это ваш путеводный маяк в лабиринте букв.
Каждая буква готова к перемещению, но лишь правильная последовательность приведет к успеху.
Ваша миссия – написать скрипт, который, словно невидимая рука мастера:
Считает слово для сборки id="target-word".
Найдет каждую его букву в алфавите id="alphabet".
С ювелирной точностью перенесет каждую букву в соответствующий 
ей слот наверху id="letter-slots". Порядок имеет значение!
Когда последняя буква займет свое место, завершая слово, 
на экране проявится скрытый код в теге id="password" – ваша награда и подтверждение мастерства.
Этот код – цель вашего путешествия. Вставьте его в поле ниже на Stepik.
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# import time
# with webdriver.Chrome() as chrome:
#     chrome.get('https://parsinger.ru/draganddrop/4/index.html')
#     action = ActionChains(chrome)
#     word = chrome.find_element(By.ID, 'target-word').text

#     alp_word = chrome.find_elements(By.CLASS_NAME, 'draggable-letter')
#     letters = chrome.find_elements(By.CLASS_NAME, 'letter-slot')

#     for i in range(0, len(word)):
#         print(word[i])
#         for l in alp_word:
#             if l.text == word[i]:
#                 action.drag_and_drop(l, letters[i]).perform()
#                 time.sleep(1)    
    
#     result = chrome.find_element(By.ID, 'password-container').text
#     print(result)

