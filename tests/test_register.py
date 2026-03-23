from locators import Locators
from data import Data
from urls import Urls
from generators import Generators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegister:
    def test_register_success(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        email = Generators.generate_email()
        password = Generators.generate_password()

        driver.find_element(*Locators.NAME_INPUT).send_keys(Data.VALID_NAME)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_REGISTER).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_SUBMIT))

        assert driver.current_url == Urls.LOGIN_URL

    def test_register_invalid_password(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys(Data.VALID_NAME)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Generators.generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.INVALID_PASSWORD)
        driver.find_element(*Locators.SUBMIT_REGISTER).click()

        error_password = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_PASSWORD))
        assert error_password.is_displayed()
