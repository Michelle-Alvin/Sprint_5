import pytest
import random
import locators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope='function')
def generate_user():
    name = "jamesloginov"
    login = f"jamesloginov{random.randint(100, 999)}@yandex.ru"
    password = "123456"
    return name, login, password


@pytest.fixture(scope='function')
def test_user():
    email = "lukinarseniy001@yandex.ru"
    password = "123456"
    return email, password


@pytest.fixture(scope='function')
def logged_user(test_user):
    email, password = test_user
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*locators.LOGIN_MAIN_PAGE).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

    driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))
    return driver
