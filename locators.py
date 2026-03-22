from selenium.webdriver.common.by import By

class Locators:

    # Регистрация
    REGISTER_BUTTON = (By.CSS_SELECTOR, "a[href='/register']")  # Кнопка регистрации

    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")  # Поле имени
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")  # Поле email
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")  # Поле пароля

    SUBMIT_REGISTER = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")  # Кнопка отправки формы
    ERROR_PASSWORD = (By.XPATH, "//p[contains(normalize-space(),'Некорректный пароль')]")  # Ошибка пароля

    # Логин
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")  # Кнопка входа на главной
    LOGIN_ENTRANCE_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")  # Кнопка входа на регистрации
    LOGIN_RECOVERY_BUTTON = (By.CSS_SELECTOR, "a[href='/forgot-password']")  # Кнопка восстановления пароля
    LOGIN_EMAIL = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")  # Поле Email
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[type='password']")  # Поле Пароль
    LOGIN_SUBMIT = (By.XPATH, "//button[normalize-space()='Войти']")  # Кнопка входа

    # Личный кабинет
    PROFILE_BUTTON = (By.XPATH, "//p[normalize-space()='Личный Кабинет']")  # Кнопка личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")  # Кнопка выхода

    # Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[normalize-space()='Конструктор']")  # Кнопка конструктора
    LOGO = (By.CSS_SELECTOR, "a[href='/']")  # Логотип

    # Разделы
    BUNS = (By.XPATH, "//span[normalize-space()='Булки']")  # Раздел Булки
    SAUCES = (By.XPATH, "//span[normalize-space()='Соусы']")  # Раздел Соусы
    FILLINGS = (By.XPATH, "//span[normalize-space()='Начинки']")  # Раздел Начинки
