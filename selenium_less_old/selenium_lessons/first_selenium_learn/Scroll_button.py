from selenium import webdriver
import time
import math
import datetime

def time_record():
    item_time = datetime.datetime.now().time()
    return item_time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    print("Начало автотеста --", time_record())
    browser = webdriver.Chrome() #options = op
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    #browser.maximize_window()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    print("Посчитали переменную", x, time_record())

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    print("Ввели переменную", answer, time_record())

    browser.execute_script("window.scrollBy(0, 50);") # скролл на 50 пикселей вниз

    i_robot = browser.find_element_by_id("robotCheckbox")
    i_robot.click()
    print("кликнули на checkbox", time_record())

    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()
    print("кликнули на radiobutton", time_record())

    submit = browser.find_element_by_xpath("//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
    print("клинкули на Submit", time_record())
    time.sleep(5)

finally:
    time.sleep(10)
    print("Закрываем браузер", time_record())  
    browser.quit()

