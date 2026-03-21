from locators import Locators
from data import Data
from selenium import webdriver

class TestConstructor:
    def test_constructor_navigation(self):
        driver = webdriver.Chrome()
        driver.get(Data.BASE_URL)

        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.BUNS).click()

        assert driver.find_element(*Locators.BUNS).is_displayed()
        driver.quit()
