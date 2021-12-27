import time
from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    #запускаем веб_драйвер
    browser = webdriver.Chrome()
    #переходим по ссылке
    browser.get(link)

    first_name = browser.find_element_by_name("first_name").send_keys("test1@gmail.com")
    time.sleep(2)

    last_name = browser.find_element_by_name("last_name").send_keys("password123")
    time.sleep(2)

    city = browser.find_element_by_name("firstname").send_keys("Test_city")
    time.sleep(2)

    country = browser.find_element_by_id('country').send_keys("Test_country")
    time.sleep(2)

    button = browser.find_element_by_id("submit_button")
    button.click()

finally:
    #браузер закрывается
    browser.quit()

