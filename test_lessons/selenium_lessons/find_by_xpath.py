from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("first_name").send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name").send_keys("Petrov")
    input3 = browser.find_element_by_name("firstname").send_keys("Smolensk")
    input4 = browser.find_element_by_id("country").send_keys("Russia")

    button = browser.find_element_by_xpath("//button[@type ='submit']").click() # сработало


finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла