from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage): 
    def should_be_login_link(self):
        assert self.is_element_present(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"), "Button BASTEK is not found"
        basket = self.browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        print("----- Текст на кнопке ------", basket.text)
        time.sleep(3)
        basket.click()
        self.solve_quiz_and_get_code()
        print("----- Решили уравнение -----")
        #time.sleep(30)

        #ловим алерты, если не сходятся значения в уведомлениях
        alert1 = self.browser.find_element_by_xpath("//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]").text
        print(alert1)
        #assert alert1 == "Coders at Work has been added to your basket.", "Ответ не соответствует"

        alert2 = self.browser.find_element_by_xpath("//div[@class='alert alert-safe alert-noicon alert-success  fade in'][2]").text
        print(alert2)
        #assert alert2 == "Your basket now qualifies for the Deferred benefit offer offer.", "Ответ не соответствует"

        # Определяем стоимость товара
        price = self.browser.find_element_by_xpath("//p[@class='price_color']").text
        print("Цена товара =", price)

        # находим сумму в корзине
        basket_total = self.browser.find_element_by_xpath("//div[@class='basket-mini pull-right hidden-xs']").text
        print(basket_total)
        basket_price = basket_total.split()[2] # выдилели только сумму в корзине
        print("Численное значение ИТОГО =", basket_price)
        time.sleep(3)

        assert basket_price == price, "Цена товара = цене в корзине" # проверка на равенство цен товара и корзины
        print("----- В корзине сумма равна цене книги -----")

