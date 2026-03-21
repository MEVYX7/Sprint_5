from locators import Locators
from data import Data
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def test_login_main_button(self):
        driver = webdriver.Chrome()
        driver.get(Data.BASE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        profile_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert profile_button.is_displayed()
        driver.quit()

    def test_login_personal_account_button(self):
        driver = webdriver.Chrome()
        driver.get(Data.BASE_URL)

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        profile_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert profile_button.is_displayed()
        driver.quit()

    def test_login_register_button(self):
        driver = webdriver.Chrome()
        driver.get(Data.BASE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.LOGIN_ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        profile_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert profile_button.is_displayed()
        driver.quit()

    def test_login_recovery_button(self):
        driver = webdriver.Chrome()
        driver.get(Data.BASE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.LOGIN_RECOVERY_BUTTON).click()
        driver.find_element(*Locators.LOGIN_ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        profile_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert profile_button.is_displayed()
        driver.quit()
