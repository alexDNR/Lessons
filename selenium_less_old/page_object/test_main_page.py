import pytest
from .pages.main_page import MainPage

# запуск автоетста через запрос "pytest -v --tb=line --language=en test_main_page.py

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])

def test_guest_can_go_to_login_page(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() # открываем страницу
    page.should_be_login_link() # выполняем метод страницы — переходим на страницу логина

