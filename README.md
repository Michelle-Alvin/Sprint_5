# SPRINT 5

Проект по тестированию сайта `https://stellarburgers.nomoreparties.site/`.

## Структура проекта:

- Локаторы locators.py
- Константы test_data.py
- Фикстуры в `conftest.py`:
    - **generate_user** - создание пользователей для сценариев регистрации
    - **test_user** - тестовый пользователь для сценариев авторизации
    - **logged_user** - функция выполнения авторизации для снижения дублирования кода


- Тестовые блоки сценариев в папке `tests`:
    - **test_registration.py**
    - **test_login.py**
    - **test_personal_account.py**
    - **test_constructor.py**