class BtcPage:
    def __init__(self, driver):
        self.driver = driver

        self.wallet = "//span[contains(text(), 'Wallet')]"
        self.buy = "//span[contains(text(), 'Buy')]"
        self.sell = "//span[contains(text(), 'Sell')]"
        self.exchange = "//span[contains(text(), 'Exchange')]"

    def verifyIfButtonsAppear(self):
        assert self.driver.find_element_by_xpath(self.wallet).is_displayed()
        assert self.driver.find_element_by_xpath(self.buy).is_displayed()
        assert self.driver.find_element_by_xpath(self.sell).is_displayed()
        assert self.driver.find_element_by_xpath(self.exchange).is_displayed()