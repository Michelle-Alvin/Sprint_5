import locators


class Test_constructor():
    def test_buns_tab(self, logged_user):
        driver = logged_user

        driver.find_element(*locators.SAUSES).click()

        assert driver.find_element(*locators.ACTIVE_TAB).text == 'Соусы', 'Вкладка не переключилась на Соусы'
        driver.find_element(*locators.BUNS).click()

        assert driver.find_element(*locators.ACTIVE_TAB).text == 'Булки', 'Активная вкладка не Булки'

    def test_sauses_tab(self, logged_user):
        driver = logged_user

        driver.find_element(*locators.SAUSES).click()

        assert driver.find_element(*locators.ACTIVE_TAB).text == 'Соусы'

    def test_toppings_tab(self, logged_user):
        driver = logged_user

        driver.find_element(*locators.TOPPINGS).click()

        assert driver.find_element(*locators.ACTIVE_TAB).text == 'Начинки'
