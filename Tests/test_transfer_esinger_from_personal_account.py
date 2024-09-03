from selenium.webdriver.common.by import By
from time import sleep


def test_click_desinger_customer_account(driver):
    driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
    driver.find_element(By.NAME, "name").send_keys(
        "Mikhail_Trishin_10qogorta_123@gmail.ru")
    driver.find_element(By.NAME, "Пароль").send_keys("123123")
    driver.find_element(By.XPATH,'//button[text() ="Войти"]').click()
    driver.find_element(By.XPATH, '//p[text() = "Личный Кабинет"]').click()
    driver.find_element(By.XPATH, '//p[text()="Конструктор"]').click()
    sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_click_logo_customer_account(driver):
    driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
    driver.find_element(By.NAME, "name").send_keys(
        "Mikhail_Trishin_10qogorta_123@gmail.ru")
    driver.find_element(By.NAME, "Пароль").send_keys("123123")
    driver.find_element(By.XPATH, '//button[text() ="Войти"]').click()
    driver.find_element(By.XPATH, '//p[text() = "Личный Кабинет"]').click()
    driver.find_element(By.XPATH,'//div[contains(@class, "AppHeader")]').click()
    sleep(1)
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

