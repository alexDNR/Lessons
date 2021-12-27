from selenium import webdriver
import time 
import os
import datetime

def time_record():
    item_time = datetime.datetime.now().time()
    return item_time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #browser.maximize_window()

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Ivan")
    print("Ввели имя пользователя --", first_name, time_record())
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Petrov")
    print("Ввели фамилию пользователя --", first_name, time_record())
    email = browser.find_element_by_name("email")
    email.send_keys("test@mail.ru")
    print("Ввели почту пользователя --", first_name, time_record())

    file_button = browser.find_element_by_xpath("//input[@type='file']")
    #current_dir = os.path.abspath(os.path.dirname(__file__)) 
    #file_path = os.path.join(current_dir, 'file.txt')
    file_button.click()
    file_button.send_keys("C:\\Selenium_course\\lessons\\file.txt")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла