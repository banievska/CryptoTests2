class EthPage:

    def __init__(self, driver):
        self.driver = driver

        self.calcInputEth = "//div[contains(@class, 'cp-coin__calculator-inputs')]//div[1]/input"
        self.calcPrice = "//div[contains(@class, 'cp-coin__calculator-inputs')]//div[3]/input"

    def enterValue(self, value):
        self.driver.find_element_by_xpath(self.calcInputEth).send_keys(value)

    def checkPrice(self, price):
        priceValue = self.driver.find_element_by_xpath(self.calcPrice).text()
        newPrice = int(priceValue)
        if newPrice > price:
            assert True
        else:
            assert False