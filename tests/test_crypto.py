import pytest
from data.test_data import TestData
from page.crypto_page import CryptoPage
from page.markets_page import MarketsPage
from page.trade_page import TradePage

@pytest.mark.usefixtures("init_driver")
class TestCrypto(object):

    def setup_method(self):
        self.cry = CryptoPage(self.driver)
        self.cry.click_markets()
        self.markets = MarketsPage(self.driver)
        self.markets.click_usdc()
        self.markets.click_CRO_USDC()
        self.trade = TradePage(self.driver)

    def test_trade_page_is_loaded(self):
        self.trade.check_trade_page_exist()

    def test_sell_cro_label(self):
        self.trade.check_sell_cro()

    def test_add_CRO_USDC_into_favorite(self):
        self.trade.add_CRO_USDC_into_favorite()

    def test_is_able_to_input(self):
        self.trade.check_textfield(TestData.PRICE, TestData.AMOUNT, TestData.BUY_TOTAL)

    def test__markets_label_is_active(self):
        self.trade.check_markets()

    def test_stop_limit_is_active(self):
        self.trade.check_stop_limit()

    def test_stop_limit_info(self):
        self.trade.check_stop_limit_info()

    def test_stop_loss_is_active(self):
        self.trade.check_stop_loss()

    def test_stop_loss_info(self):
        self.trade.check_stop_loss_info()
    
    def test_5m_line_is_active(self):
        self.trade.check_5m_line()

    def test_12h_line_is_active(self):
        self.trade.check_12h_line()

    # open order history
    def test_etab(self):
        self.trade.check_open_orders()
        self.trade.check_order_history()