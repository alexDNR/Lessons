from selenium import webdriver
import time
import datetime
import math

link = "http://suninjuly.github.io/alert_accept.html"

def cacl(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def time_record():
    item_time = datetime.datetime.now().time()
    return item_time

try:
    print("1. Начало автотеста --", time_record())
    browser = webdriver.Chrome()
    browser.get(link)
    #browser.maximize_window()
    print("2. Загрузили страницу --", time_record())

    go = browser.find_element_by_xpath("//button[@type = 'submit']")
    go_value = go.text
    print("3. нашли кнопку --", "Значение в кнопке:", go_value ,time_record())
    go.click()
    print("4. Нажали на кнопку", time_record())

    confirm = browser.switch_to.alert # это нажимает на кнопку OK всплывающего окна
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    print("5. Значение переменной --", x, time_record())
    y = cacl(x)
    print("6. Значение результата --", y, time_record())

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    print("7. Ввели значение Y в поле --", time_record())

    submit = browser.find_element_by_xpath("//button[@type = 'submit']")
    submit.click()
    print("8. Кликнули по кнопке Submit --", time_record())


finally:
    time.sleep(5)
    print("9. Закрываем браузер --", time_record())
    browser.quit()