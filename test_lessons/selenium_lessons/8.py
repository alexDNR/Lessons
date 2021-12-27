from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    if (browser.find_element_by_xpath("//input[@class='form-control second']")):
        first_name = browser.find_element_by_xpath("//input[@class='form-control first']")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_xpath("//input[@class='form-control second']")
        last_name.send_keys("Petrov")
        Email = browser.find_element_by_xpath("//input[@class='form-control third']")
        Email.send_keys("test@mail.ru")
    else:
        first_name = browser.find_element_by_xpath("//input[@class='form-control first']")
        first_name.send_keys("Ivan")
        Email = browser.find_element_by_xpath("//input[@class='form-control third']")
        Email.send_keys("test@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()