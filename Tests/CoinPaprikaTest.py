import unittest
from selenium import webdriver
from Config import config
from Pages.HomePage import HomePage
from Pages.BtcPage import BtcPage
from Pages.EthPage import EthPage


class CryptoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get(config.url)

    def test_checkPrice(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.closePopup()
        homePage.closeCookiesPolicy()
        homePage.selectCurrency()
        homePage.checkPrice(3000)

    def test_checkButtons(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.closePopup()
        homePage.closeCookiesPolicy()
        driver.get('https://coinpaprika.com/coin/btc-bitcoin/')
        btcPage = BtcPage(driver)
        btcPage.verifyIfButtonsAppear()

    def test_ethCalc(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.closePopup()
        homePage.closeCookiesPolicy()
        driver.get('https://coinpaprika.com/coin/eth-ethereum/')
        ethPage = EthPage(driver)
        ethPage.enterValue("1")
        ethPage.checkPrice(100)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


