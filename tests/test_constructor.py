from locators import Locators
from urls import Urls

class TestConstructor:
    def test_constructor_navigation_buns(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.BUNS).click()

        assert driver.find_element(*Locators.BUNS).is_displayed()

    def test_constructor_navigation_fillings(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.FILLINGS).click()

        assert driver.find_element(*Locators.FILLINGS).is_displayed()

    def test_constructor_navigation_sauces(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.SAUCES).click()

        assert driver.find_element(*Locators.SAUCES).is_displayed()