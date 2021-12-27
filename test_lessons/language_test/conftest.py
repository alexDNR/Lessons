# cofntest.py должен лежать в директории нужной группы тестов - через этот файл будем запускать браузер
# Встроенная фикстура request может получать данные о текущем запущенном тесте, что позволяет, например, сохранять дополнительные данные в отчёт, а также делать многие другие интересные вещи. 
# В этом шаге мы хотим показать, как можно настраивать тестовые окружения с помощью передачи параметров через командную строку. 
# Это делается с помощью встроенной функции pytest_addoption и фикстуры request. 
# Сначала добавляем в файле conftest обработчик опции в функции pytest_addoption, затем напишем фикстуру, которая будет обрабатывать переданные в опции данные. 
# Подробнее можно ознакомиться здесь: https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#создаём функцию парсера запроса, при запуске автотеста через командную строку, к примеру тут запрос будет такой pytest --browser_name=chrome --language=es test_items.py (указываем и браузер и язык для отображения)
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox") # парсинг опций браузера
    parser.addoption('--language', action='store', default='es', help="Choose lang") # парсинг опций языка

@pytest.fixture(scope="function")
def browser(request): # в функции указываем request - так как в этой фикстуре лежат данные о текущем тесте
    user_language = request.config.getoption("language") # в переменную записываем значения языка из запроса (--language=es)
    print("\n-------------------- start browser for test --------------------")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) # указываем язык для отображения записанный в переменной user_language
    browser = webdriver.Chrome(options=options) # инициализируем браузер
    yield browser
    print("\n-------------------- quit browser --------------------")
    browser.quit()