from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def time_record():
    item_time = datetime.datetime.now().time()
    return item_time

try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)
    print("1. Запустили автотест --", time_record())
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    print("2. Загрузили страницу --", time_record())

    #нужно сделать так, чтобы тест ждал пока станет активной кнопка, чтобы сделать клик
    button = browser.find_element(by=By.ID, value="book")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) # ждём тут и только после этого кликаем на кнопку
    print("3. Подождали пока цена упала до 100$ --", time_record())
    button.click()
    print("4. Кликнули на кнопку - Book --", time_record())

    browser.execute_script("window.scrollTo(0, 100)") # скроллим вниз стриницу

    x = browser.find_element(by=By.ID, value="input_value").text
    print("5. Значение переменной Х =", x, " -- ", time_record())
    y = calc(x)
    print("6. Значение переменной Y =", y, " -- ", time_record())
    answer = browser.find_element(by=By.ID, value="answer")
    answer.send_keys(y)
    print("7. Вписали ответ --", time_record())

    submit = browser.find_element(by=By.ID, value="solve")
    submit.click()
    print("8. Кликнули по кнопке --", time_record())
    time.sleep(5)

finally:
    time.sleep(5)
    print("9. Закрываем браузер --", time_record())
    browser.quit()

