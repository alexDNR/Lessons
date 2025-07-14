from selenium import webdriver
import time
import traceback

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_xpath("//input[@type='text']")
    #find_elements_by_css_selector('input[type="text"]')  - вот так можно через css_selector
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
    trb = traceback.format_exc() 
    print(f'Произошла ошибка, вот её трэйсбэк: {trb}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла