from locators import Locators
from data import Data
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProfile:

    def test_go_to_profile(self):
        driver = webdriver.Chrome()
        driver.get(Data.BASE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))

        driver.find_element(*Locators.PROFILE_BUTTON).click()

        assert "profile" in driver.current_url
        driver.quit()
    
    def test_logo_and_constructor(self):
        driver = webdriver.Chrome()
        driver.get(Data.BASE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        assert driver.current_url == Data.BASE_URL

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()

        assert driver.current_url == Data.BASE_URL
        driver.quit()

    def test_logout(self):
        driver = webdriver.Chrome()
        driver.get(Data.BASE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(Data.VALID_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(Data.VALID_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()
        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        login_sumbit = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_SUBMIT))
        assert login_sumbit.is_displayed()
        driver.quit()
