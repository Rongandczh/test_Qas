# from attr import s
from attr import s
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from data.test_data import TestData
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class TradePage(BasePage):
    marktes_label = (By.XPATH, "//div[contains(@class, 'e-tabs__nav-item') and contains(text(), 'Market')]")
    marktes_label_is_active = (By.XPATH, "//div[@class='e-tabs__nav-item active' and contains(text(), 'Market')]")
    # region stop limit and loss
    stop_limit_label = (By.XPATH, "//div[@class='e-tabs__nav-item' and contains(text(), 'Stop Limit')]")
    stop_limit_alert = (By.XPATH, "//div[@class='d-desc' and contains(text(),'A stop-limit order is to place a limit order to buy or sell a coin once the last traded price reaches a specified price (stop price). ')]")
    stop_limit_label_is_active = (By.XPATH, "//div[@class='e-tabs__nav-item active' and contains(text(), 'Stop Limit')]")
    stop_loss_label_is_active = (By.XPATH, "//div[@class='e-tabs__nav-item active' and contains(text(), 'Stop Loss')]")
    stop_loss_alert = (By.XPATH, "//div[@class='d-desc' and contains(text(),' A stop-loss order is to place a market order to buy or sell a coin once the last traded price reaches a specified price (stop price). ')]")
    drop_down_list = (By.XPATH, "//div[@class='advanced-dropdown-trigger']")
    drop_stop_limit = (By.XPATH, "//button[@class='sub-menu-item e-button e-button--primary e-button--medium is-block is-text' and contains(text(), 'Stop Limit')]")
    drop_stop_loss = (By.XPATH, "//button[@class='sub-menu-item e-button e-button--primary e-button--medium is-block is-text' and contains(text(), 'Stop Loss')]")
    
    Buy_CRO_text = (By.XPATH, "//span[contains(@class, 'trade-type') and contains(text(), 'Buy CRO')]")
    Sell_CRO_text = (By.XPATH, "//span[contains(@class, 'trade-type') and contains(text(), 'Sell CRO')]")
    sell_CRO_btn = (By.XPATH, "//div[@class='button-tab' and contains(text(),'Sell')]")
    price_input = (By.XPATH, "//input[contains(@id, 'buyPrice')]")
    amount_input = (By.XPATH, "//input[contains(@id, 'buyAmount')]")
    total_field = (By.XPATH, "//input[contains(@id, 'buyVolume')]")
    stop_limit_info = (By.XPATH, "//div[@class='advanced-dropdown-trigger']/*[@class='e-icon e-icon-info']")

    CRO_USDC_favorite = (By.XPATH, "//div[@class='trade-pair-list']/*[@class='favorite e-icon favorite']")
    CRO_USDC_favorite_on = (By.XPATH, "//div[@class='trade-pair-list']/*[@class='favorite e-icon favorite on']")
    
    body = (By.TAG_NAME,"body")

    # region tradeview
    five_m_line = (By.XPATH, "//span[@class='time-line']/i[contains(text(), '5m')]")
    five_m_line_active = (By.XPATH, "//span[@class='time-line active']/i[contains(text(), '5m')]")
    twelve_h_line = (By.XPATH, "//span[@class='time-line']/i[contains(text(), '12h')]")
    twelve_h_line_active = (By.XPATH, "//span[@class='time-line active']/i[contains(text(), '12h')]")
    
    # region order-nav
    orders_nav = (By.XPATH, "//div[@class='e-tabs__nav-item active' and contains(text(),'Open Orders')]")
    orders_history = (By.XPATH, "//div[@class='e-tabs__nav-item' and contains(text(),'Order History')]")
    orders_history_active = (By.XPATH, "//div[@class='e-tabs__nav-item active' and contains(text(),'Order History')]")
    funds_nav = (By.XPATH, "//div[@class='e-tabs__nav-item' and contains(text(),'Funds')]")
    funds_nav_active = (By.XPATH, "//div[@class='e-tabs__nav-item active' and contains(text(),'Funds')]")
    position_nav = (By.XPATH, "//div[@class='e-tabs__nav-item' and contains(text(),'Positions')]")
    position_nav_active = (By.XPATH, "//div[@class='e-tabs__nav-item active' and contains(text(),'Positions')]")
    
    def __init__(self, driver):
        super().__init__(driver)

    def check_trade_page_exist(self):
        assert self.is_visible(self.Buy_CRO_text)
    
    def check_sell_cro(self):
        self.send_keys(self.body, Keys.PAGE_UP)
        self.click_el(self.sell_CRO_btn)
        assert self.is_visible(self.Sell_CRO_text)

    def check_textfield(self, price, amount, total):
        self.click_btn(self.price_input)
        self.clear_input(self.price_input)
        self.clear_input(self.amount_input)
        self.send_keys(self.price_input, price)
        self.send_keys(self.amount_input, amount)
        self.clear_input(self.total_field)
        self.send_keys(self.total_field, total)
    
    def check_markets(self):
        self.click_btn(self.marktes_label)
        assert self.is_visible(self.marktes_label_is_active)
        

    def check_stop_limit(self):
        self.click_btn(self.stop_limit_label)
        sleep(3)
        assert self.is_visible(self.stop_limit_label_is_active)

    def check_stop_limit_info(self):
        self.click_btn(self.stop_limit_info)
        assert self.is_visible(self.stop_limit_alert)

    def check_stop_loss_info(self):
        self.click_btn(self.drop_down_list)
        self.click_btn(self.drop_stop_loss)
        self.click_btn(self.stop_limit_info)
        assert self.is_visible(self.stop_limit_alert)

    def check_stop_loss(self):
        self.click_btn(self.drop_down_list)
        self.click_btn(self.drop_stop_loss)
        assert self.is_visible(self.stop_loss_label_is_active)

    def add_CRO_USDC_into_favorite(self):
        self.is_visible(self.Buy_CRO_text)
        self.send_keys(self.body, Keys.PAGE_UP)
        self.click_el(self.CRO_USDC_favorite)
        assert self.is_visible(self.CRO_USDC_favorite_on)

    def check_5m_line(self):
        self.send_keys(self.body, Keys.PAGE_UP)
        self.click_el(self.five_m_line)
        assert self.is_visible(self.five_m_line_active)

    def check_12h_line(self):
        self.send_keys(self.body, Keys.PAGE_UP)
        self.click_el(self.twelve_h_line)
        assert self.is_visible(self.twelve_h_line_active)

    #open orders nav
    def check_open_orders(self):
        assert self.is_visible(self.orders_nav)

    def check_order_history(self):
        self.click_el(self.orders_history)
        assert self.is_visible(self.orders_history_active)
    
    def check_funds(self):
        self.click_el(self.funds_nav)
        assert self.is_visible(self.funds_nav_active)
    
    def check_positions(self):
        self.click_el(self.position_nav)
        assert self.is_visible(self.position_nav_active)