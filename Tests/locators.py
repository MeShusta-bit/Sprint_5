class Locator:
    login_account = "//button[text() = 'Войти в аккаунт']"                                         # кнопка войти в аккаунт
    personal_account = '//p[text() ="Личный Кабинет"]'                                             # кнопка личный кабинет
    constructor = '//p[text()="Конструктор"]'                                                      # кнопка конструктор
    sousi = "//span[text()='Соусы']"                                                               # переход в раздел соусы
    nachinki = "//span[text()='Начинки']"                                                          # переход в раздел начинки
    bulki = "//span[text()='Булки']"                                                               # переход в раздел булки
    button_stellar = '//div[contains(@class, "AppHeader")]'                                        # кнопка Stellar Burgers
    imput_name_reg = "//label[contains(text(), 'Имя')]/following-sibling::input"                   # поле ввода имени при регистрации
    imput_email_reg = "//label[contains(text(), 'Email')]/following-sibling::input"                # поле ввода email при регистрации
    imput_password_reg = "//label[contains(text(), 'Пароль')]/following-sibling::input"            # поле ввода пароля при регистрации
    button_reg = '//button[text() = "Зарегистрироваться"]'                                         # кнопка зарегестрироваться
    invalid_password = '//p[text()="Некорректный пароль"]'                                         # всплывающая надпись "некорректный пароль"
    button_login_1 = '//a[text()="Войти"]'                                                         # кнопка войти в окне регистрации
    imput_name_login = 'name'                                                                      # поле ввода email при авторизации
    imput_password_login = 'Пароль'                                                                # поле ввода пароля при авторизации
    button_login = '//button[text() ="Войти"]'                                                     # кнопка войти в поле авторизации
    register_button = "//a[text() = 'Зарегистрироваться']"                                         # кнопка зарегестрироваться в поле авторизации
    button_recover_password = '//a[text()="Восстановить пароль"]'                                  # кнопка восстановить пароль в поле авторизации
    button_logout = '//button[text()="Выход"]'                                                     # кнопка выход в окне личного кабинета
    selected_object = '//span[contains(@class, "current")]'                                        # выбран вариант конструктора
    place_an_order = '//button[text()= "Оформить заказ"]'                                          # кнопка оформить заказ
    save_button = '//button[text()= "Сохранить"]'                                                  # кнопка сохранить
    sousi_spicy = '//p[text()="Соус Spicy-X"]'                                                    # соус Spicy-X
    meteorite = '//p[text()="Говяжий метеорит (отбивная)"]'                                       # Говяжий метеорит (отбивная)
    bulka = '//p[text()="Краторная булка N-200i"]'                                                # Краторная булка N-200i