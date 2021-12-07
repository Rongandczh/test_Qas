from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as ec



class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_el(self, locator):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator)).click()

    def click_btn(self, locator):
        WebDriverWait(self.driver, 15).until(ec.presence_of_element_located(locator)).click()

    def clear_input(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).clear()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        return bool(element)
