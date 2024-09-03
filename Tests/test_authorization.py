from selenium.webdriver.common.by import By
from time import sleep


def test_registration_true(driver):
    driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
    driver.find_element(By.XPATH, "//a[text() = 'Зарегистрироваться']").click()
    driver.find_element(By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input").send_keys("Миша")
    driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input").send_keys("Mikhail_Trishin_10qogorta_123@ya.ru")
    driver.find_element(By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input").send_keys("123123")
    driver.find_element(By.XPATH,'//button[text() = "Зарегистрироваться"]').click()
    sleep(2)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

def test_registration_invalid_rassword(driver):
    driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
    driver.find_element(By.XPATH, "//a[text() = 'Зарегистрироваться']").click()
    driver.find_element(By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input").send_keys("Миша")
    driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input").send_keys("Mikhail_Trishin_10qogorta_123@ya.ru")
    driver.find_element(By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input").send_keys("123")
    driver.find_element(By.XPATH,'//button[text() = "Зарегистрироваться"]').click()
    assert driver.find_element(By.XPATH,'//p[text()="Некорректный пароль"]')
    driver.quit()
