from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
from test_data import EMAIL, PASSWORD


class Test_login():
    def test_login_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*locators.LOGIN_MAIN_PAGE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

        driver.find_element(*locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))

        assert driver.find_element(*locators.CHECKOUT).text == 'Оформить заказ'


    def test_login_via_personal_account_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(*locators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

        driver.find_element(*locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))

        assert driver.find_element(*locators.CHECKOUT).text == 'Оформить заказ'


    def test_login_via_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.REGISTER_TITLE))

        driver.find_element(*locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

        driver.find_element(*locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))

        assert driver.find_element(*locators.CHECKOUT).text == 'Оформить заказ'


    def test_login_via_forgot_password_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*locators.FORGOT_PASSWORD_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.FORGOT_PASSWORD_TITLE))

        driver.find_element(*locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

        driver.find_element(*locators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))

        assert driver.find_element(*locators.CHECKOUT).text == 'Оформить заказ'
