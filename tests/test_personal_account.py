from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


class Test_personal_account():
    def test_go_to_personal_account(self, logged_user):
        driver = logged_user

        driver.find_element(*locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ORDERS_HISTORY))

        assert driver.find_element(*locators.ORDERS_HISTORY).text == 'История заказов'

    def test_from_personal_account_to_constructor_via_tab(self, logged_user):
        driver = logged_user

        driver.find_element(*locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ORDERS_HISTORY))

        driver.find_element(*locators.CONSTRUCTOR_TAB).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))

        assert driver.find_element(*locators.CHECKOUT).text == 'Оформить заказ'

    def test_from_personal_account_to_constructor_via_logo(self, logged_user):
        driver = logged_user

        driver.find_element(*locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ORDERS_HISTORY))

        driver.find_element(*locators.LOGO).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.CHECKOUT))

        assert driver.find_element(*locators.CHECKOUT).text == 'Оформить заказ'

    def test_logout(self, logged_user):
        driver = logged_user

        driver.find_element(*locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ORDERS_HISTORY))

        driver.find_element(*locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.LOGIN_TITLE)))

        assert driver.find_element(*locators.LOGIN_TITLE).text == 'Вход'
