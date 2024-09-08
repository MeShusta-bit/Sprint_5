from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration(Locator):
    def test_registration_true(self,driver,email_generator):
        driver.find_element(By.XPATH, self.login_account).click()
        driver.find_element(By.XPATH, self.register_button).click()
        driver.find_element(By.XPATH, self.imput_name_reg).send_keys("Миша")
        driver.find_element(By.XPATH, self.imput_email_reg).send_keys(email_generator)
        driver.find_element(By.XPATH, self.imput_password_reg).send_keys("123123")
        driver.find_element(By.XPATH, self.button_reg).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.button_login)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_invalid_rassword(self,driver):
        driver.find_element(By.XPATH, self.login_account).click()
        driver.find_element(By.XPATH, self.register_button).click()
        driver.find_element(By.XPATH, self.imput_name_reg).send_keys("Миша")
        driver.find_element(By.XPATH, self.imput_email_reg).send_keys("Mikhail_Trishin_10qogorta_123@ya.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("123")
        driver.find_element(By.XPATH, self.button_reg).click()
        assert driver.find_element(By.XPATH,'//p[text()="Некорректный пароль"]')
