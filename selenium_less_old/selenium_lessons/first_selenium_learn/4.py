from selenium import webdriver
import math
import time
import traceback

url = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = str(math.ceil(math.pow(math.pi, math.e)*10000)) #значение = 224592
    print(x)

    link = browser.find_element_by_link_text(x).click()

    # вводим авторизационные данные
    input1 = browser.find_element_by_name("first_name").send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name").send_keys("Petrov")
    input3 = browser.find_element_by_name("firstname").send_keys("Smolensk")
    input4 = browser.find_element_by_id("country").send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn").click()
    time.sleep(5)

except Exception as error:
    trb = traceback.format_exc() 
    print(f'Произошла ошибка, вот её трэйсбэк: {trb}')

finally:
    time.sleep(10)
    browser.quit()    