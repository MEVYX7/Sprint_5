from helpers import wait_for_active_tab
from locators import Locators
from urls import Urls


class TestConstructor:
    def test_constructor_navigation_buns(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.BUNS).click()

        assert wait_for_active_tab(driver, "Булки").is_displayed()

    def test_constructor_navigation_fillings(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.FILLINGS).click()

        assert wait_for_active_tab(driver, "Начинки").is_displayed()

    def test_constructor_navigation_sauces(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.SAUCES).click()

        assert wait_for_active_tab(driver, "Соусы").is_displayed()
