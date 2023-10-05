import locators


def test_buns_tab(logged_user):
    driver = logged_user

    driver.find_element(*locators.SAUSES).click()
    driver.find_element(*locators.BUNS).click()

    assert driver.find_element(*locators.ACTIVE_TAB).text == 'Булки'

    driver.quit()


def test_sauses_tab(logged_user):
    driver = logged_user

    driver.find_element(*locators.SAUSES).click()

    assert driver.find_element(*locators.ACTIVE_TAB).text == 'Соусы'

    driver.quit()


def test_toppings_tab(logged_user):
    driver = logged_user

    driver.find_element(*locators.TOPPINGS).click()

    assert driver.find_element(*locators.ACTIVE_TAB).text == 'Начинки'

    driver.quit()
