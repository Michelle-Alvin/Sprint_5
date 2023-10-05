from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_registration_success(generate_user):
    name, email, password = generate_user
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*locators.PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.REGISTER_BUTTON))
    driver.find_element(*locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.REGISTER_TITLE))
    driver.find_element(*locators.REGISTER_NAME_INPUT).send_keys(name)
    driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.REGISTER_SEND).click()

    login_page = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

    assert 'Вход' == login_page.text

    driver.quit()


def test_registration_incorrect_password(generate_user):
    name, email, _ = generate_user

    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*locators.PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.REGISTER_BUTTON))
    driver.find_element(*locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.REGISTER_TITLE))
    driver.find_element(*locators.REGISTER_NAME_INPUT).send_keys(name)
    driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys("123")
    driver.find_element(*locators.REGISTER_SEND).click()

    assert driver.find_element(*locators.INCORRECT_PASSWORD).text == 'Некорректный пароль'

    driver.quit()
