from selenium import webdriver
import time
import math
import datetime
from selenium.webdriver.support.ui import Select

def time_record():
    item_time = datetime.datetime.now().time()
    return item_time

try: 
    print("Начало автотеста --", time_record())
    browser = webdriver.Chrome() #options = op
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)

    x_value = browser.find_element_by_id("num1")
    x = int(x_value.text)
    print("Первая переменная х =", x, "----", time_record())
    y_value = browser.find_element_by_id("num2")
    y = int(y_value.text)
    print("Первая переменная y =", y, "----" ,time_record())

    answer = x + y
    print("х + y =", answer, "----" ,time_record())

    select_value = Select(browser.find_element_by_tag_name("select"))
    select_value.select_by_visible_text(str(answer))

    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()
    print("клинкули на Submit", time_record())
    time.sleep(5)

finally:
    time.sleep(5)
    print("Закрываем браузер", time_record())  
    browser.quit()


#Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index). 
# Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python")