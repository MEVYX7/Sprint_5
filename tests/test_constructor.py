from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from urls import Urls


class TestConstructor:
    @staticmethod
    def _wait_for_active_tab(driver, tab_name):
        tab_locator = (
            By.XPATH,
            f"//div[contains(@class, 'tab_tab_type_current')]//span[normalize-space()='{tab_name}']",
        )
        return WebDriverWait(driver, 5).until(
            lambda current_driver: current_driver.find_element(*tab_locator)
        )

    def test_constructor_navigation_buns(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.BUNS).click()

        assert self._wait_for_active_tab(driver, "Булки").is_displayed()

    def test_constructor_navigation_fillings(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.FILLINGS).click()

        assert self._wait_for_active_tab(driver, "Начинки").is_displayed()

    def test_constructor_navigation_sauces(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.SAUCES).click()

        assert self._wait_for_active_tab(driver, "Соусы").is_displayed()
