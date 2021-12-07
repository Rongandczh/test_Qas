from page.base_page import BasePage
from selenium.webdriver.common.by import By
from data.test_data import TestData
from time import sleep


class MarketsPage(BasePage):

    USDC_label = (By.XPATH, "//div[contains(@class, 'e-tabs__nav-item') and contains(text(), 'USDC')]")
    CRO_USDC_label = (By.XPATH, "//div[contains(@class, 'instrument-name')]//span[contains(text(), 'CRO')]")

    def __init__(self, driver):
        super().__init__(driver)


    def click_usdc(self):
        self.click_btn(self.USDC_label)
    
    def click_CRO_USDC(self):
        self.click_btn(self.CRO_USDC_label)