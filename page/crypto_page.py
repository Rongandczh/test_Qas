from page.base_page import BasePage
from selenium.webdriver.common.by import By
from data.test_data import TestData
from time import sleep


class CryptoPage(BasePage):


    markets_label = (By.XPATH, "//button[contains(@class, 'link-btn e-button e-button--primary e-button--medium is-text') and contains(text(), 'Markets')]")
    USDC_label = (By.XPATH, "//div[contains(@class, 'e-tabs__nav-item') and contains(text(), 'USDC')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOST)

    def click_markets(self):
        self.click_btn(self.markets_label)
        