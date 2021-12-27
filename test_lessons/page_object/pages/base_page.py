import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)

#Теперь в этом же классе реализуем метод is_element_present, 
# в котором будем перехватывать исключение. 
# В него будем передавать два аргумента: 
# как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
    def is_element_present(self, by, what):
        try:
            self.browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']") 
        except ("NoSuchElementException"):
            return False
        return True        

    # метод расчёта значения Х в alert при нажатии кнопки - "Добавить в корзину"
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

