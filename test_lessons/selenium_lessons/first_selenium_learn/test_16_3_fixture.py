import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    #этот код выполнится после завершения теста
    print("\nclose browser")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("что-то тут трутутук")

class TestMainPage1():
    #вызываем фикстуру в тесте, передав её как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        login = browser.find_element_by_id("login_link")
        login.click()

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        basket = browser.find_element_by_xpath("//a[@class='btn btn-default']")
        basket.click()   