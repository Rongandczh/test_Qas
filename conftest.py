import pytest
from selenium import webdriver
from page.crypto_page import CryptoPage
from page.markets_page import MarketsPage
from page.trade_page import TradePage




@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    
    if request.param == "chrome":
        web_driver = webdriver.Chrome() # executable_path=TestData.CHROME_PATH
    web_driver.maximize_window()
    web_driver.delete_all_cookies()
    request.cls.driver = web_driver
    request.cls.loginPage = CryptoPage(web_driver)
    request.cls.loginPage = MarketsPage(web_driver)
    request.cls.loginPage = TradePage(web_driver)
    yield
    web_driver.close()