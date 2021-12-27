#import unittest
import pytest
from selenium import webdriver
import time

#----------------------------------------------------------
def test_registration1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        first_name = browser.find_element_by_xpath("//input[@class='form-control first']")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_xpath("//input[@class='form-control second']")
        last_name.send_keys("Petrov")
        email = browser.find_element_by_xpath("//input[@class='form-control third']")
        email.send_keys("test@mail.ru")
        button = browser.find_element_by_css_selector("button.btn") # Отправляем заполненную форму
        button.click()
        time.sleep(3)
        welcome_text_elt = browser.find_element_by_tag_name("h1") # находим элемент, содержащий текст
        welcome_text = welcome_text_elt.text # записываем в переменную welcome_text текст из элемента welcome_text_elt
        assert welcome_text == "Congratulations! You have successfully registered!",  "Not click button registration1"
        time.sleep(3)
    finally:    
        browser.quit()
#----------------------------------------------------------
def test_registration2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        first_name = browser.find_element_by_xpath("//input[@class='form-control first']")
        first_name.send_keys("Ivan")
        email = browser.find_element_by_xpath("//input[@class='form-control third']")
        email.send_keys("test@mail.ru")              
        button = browser.find_element_by_css_selector("button.btn") # Отправляем заполненную форму
        button.click()
        time.sleep(3)        
        welcome_text_elt = browser.find_element_by_tag_name("h1") # находим элемент, содержащий текст
        welcome_text = welcome_text_elt.text # записываем в переменную welcome_text текст из элемента welcome_text_elt
        assert welcome_text == "Congratulations! You have successfully registered!",  "Not click button registration2"   
        time.sleep(3)
    finally:
        browser.quit()
#----------------------------------------------------------
