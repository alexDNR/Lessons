from selenium import webdriver
import time
import datetime
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def time_record():
    item_time = datetime.datetime.now().time()
    return item_time

def start():
    print("1. Начало автотеста --", time_record())
    browser.get(link)
    print("2. Загрузили страницу --", time_record())    

def go_next_page():
    go = browser.find_element_by_xpath("//button[@type = 'submit']")
    go_value = go.text
    print("3. Нашли кнопку --", "Значение в кнопке:", go_value ,time_record())
    go.click()
    print("4. Нажали на кнопку", time_record())
    time.sleep(3)

def result():
    x = browser.find_element_by_id("input_value").text
    print("6. Значение переменной --", x, time_record())
    y = calc(x)
    print("7. Значение результата --", y, time_record())
    #----
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    print("8. Ввели значение Y в поле --", time_record())

def submit():
    submit = browser.find_element_by_xpath("//button[@type = 'submit']")
    submit.click()
    print("9. Кликнули по кнопке Submit --", time_record())
    time.sleep(5)

try:
    browser = webdriver.Chrome()
    start()
    go_next_page()
    browser.switch_to.window(browser.window_handles[1])
    print("5. Перешли на новую вкладку", time_record())
    result()
    submit()
    browser.close() # закрыли активную вкладку
    print("10. Закрыли активную вкладку --", time_record())
    browser.switch_to.window(browser.window_handles[0])
    print("11. Вернулись на первую вкладку --", time_record())

finally:
    time.sleep(5)
    print("12. Закрываем браузер --", time_record())
    browser.quit()

    