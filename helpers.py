from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


ACTIVE_TAB = (
    By.XPATH,
    "//div[contains(@class, 'tab_tab_type_current')]//span",
)


def get_active_tab_text(driver):
    return WebDriverWait(driver, 5).until(
        lambda current_driver: current_driver.find_element(*ACTIVE_TAB)
    ).text


def wait_for_active_tab(driver, tab_name):
    tab_locator = (
        By.XPATH,
        f"//div[contains(@class, 'tab_tab_type_current')]//span[normalize-space()='{tab_name}']",
    )
    return WebDriverWait(driver, 5).until(
        lambda current_driver: current_driver.find_element(*tab_locator)
    )
