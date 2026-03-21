from selenium.webdriver.common.by import By

class Locators:

    # Регистрация
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Кнопка регистрации
    NAME_INPUT = (By.XPATH, "//*/fieldset[1]/div/div/input")  # Поле имени
    EMAIL_INPUT = (By.XPATH, "//*/fieldset[2]/div/div/input")  # Поле email
    PASSWORD_INPUT = (By.XPATH, "//*/fieldset[3]/div/div/input")  # Поле пароля
    SUBMIT_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка отправки формы
    ERROR_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")  # Ошибка пароля

    # Логин
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка входа на главной
    LOGIN_ENTRANCE_BUTTON = (By.XPATH, "//a[text()='Войти']")  # Кнопка входа на регистрации
    LOGIN_RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")  # Кнопка личного кабинета
    LOGIN_EMAIL = (By.NAME, "name")  # Поле Email
    LOGIN_PASSWORD = (By.NAME, "Пароль")  # Поле Пароль
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа
    
    # Личный кабинет
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода

    # Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка конструктора
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип

    # Разделы 
    BUNS = (By.XPATH, "//span[text()='Булки']")  # Раздел Булки
    SAUCES = (By.XPATH, "//span[text()='Соусы']")  # Раздел Соусы
    FILLINGS = (By.XPATH, "//span[text()='Начинки']")  # Раздел Начинки