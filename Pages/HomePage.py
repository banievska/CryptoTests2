class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.currencyDropdown = "//button[contains(@class,'quote-selector')]"
        self.currencyUSD = "//span[text()='usd']"
        self.popupCloseBtn = "//span[contains(@class,'popup__close--home')]"
        self.cookiesPolicyCloseBtn = "//div[contains(@class,'cookie-banner')]/span[contains(@class,'icon-close-coins')]"
        self.priceValue = "//*[@id='virtualScroll']/div[1]/div[2]/div/div[2]/div[1]/text()"

    def selectCurrency(self):
        self.driver.find_element_by_xpath(self.currencyDropdown).click()
        self.driver.find_element_by_xpath(self.currencyUSD).click()

    def closePopup(self):
        self.driver.find_element_by_xpath(self.popupCloseBtn).click()

    def closeCookiesPolicy(self):
        self.driver.find_element_by_xpath(self.cookiesPolicyCloseBtn).click()

    def checkPrice(self, myPrice):
        price = self.driver.find_element_by_xpath(self.priceValue).text()
        new_price = price.replace("$", "")
        new_price = new_price.replace(" ", "")
        new_price = int(new_price)
        if new_price > myPrice:
            assert True
        else:
            assert False
