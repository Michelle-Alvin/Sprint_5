import pytest
import locators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_data import EMAIL, PASSWORD

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def logged_user(driver):

    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*locators.LOGIN_MAIN_PAGE).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

    driver.find_element(*locators.EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))
    yield driver
    driver.quit()
