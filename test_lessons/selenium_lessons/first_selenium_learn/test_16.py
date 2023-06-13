from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/" # ссылка на страницу для автотеста

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\n--start browser for test -- testMainPage1")
        self.browser = webdriver.Chrome()

    @classmethod    
    def teardown_class(self):
        print("--quit browser for test -- testMainPage1")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_id("login_link").click()
        
    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_xpath("//a[@class='btn btn-default']").click()


class TestMainPage2():

    def setup_method(self):
        print("start browser for test.. -- testMainPage2")
        self.browser = webdriver.Chrome()

    def teardown(self):
        print("quit browser for test -- testMainPage2")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_id("login_link").click()
        
    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_xpath("//a[@class='btn btn-default']").click()        

