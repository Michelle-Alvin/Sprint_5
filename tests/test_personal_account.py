from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


def test_go_to_personal_account(logged_user):
    driver = logged_user

    driver.find_element(*locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ORDERS_HISTORY))

    assert driver.find_element(*locators.ORDERS_HISTORY).text == 'История заказов'

    driver.quit()


def test_from_personal_account_to_constructor_via_tab(logged_user):
    driver = logged_user

    driver.find_element(*locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ORDERS_HISTORY))

    driver.find_element(*locators.CONSTRUCTOR_TAB).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))

    assert driver.find_element(*locators.CHECKOUT).text == 'Оформить заказ'

    driver.quit()


def test_from_personal_account_to_constructor_via_logo(logged_user):
    driver = logged_user

    driver.find_element(*locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ORDERS_HISTORY))

    driver.find_element(*locators.LOGO).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))

    assert driver.find_element(*locators.CHECKOUT).text == 'Оформить заказ'

    driver.quit()


def test_logout(logged_user):
    driver = logged_user

    driver.find_element(*locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ORDERS_HISTORY))

    driver.find_element(*locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.LOGIN_TITLE)))

    assert driver.find_element(*locators.LOGIN_TITLE).text == 'Вход'

    driver.quit()
