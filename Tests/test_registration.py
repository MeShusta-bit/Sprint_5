from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locator
from data import Data
from helpers import Generator



class TestRegistration:
    def test_registration_true(self,driver):
        driver.find_element(By.XPATH, Locator.login_account).click()
        driver.find_element(By.XPATH, Locator.register_button).click()
        driver.find_element(By.XPATH, Locator.imput_name_reg).send_keys(Data.name)
        driver.find_element(By.XPATH, Locator.imput_email_reg).send_keys(Generator.email_generator)
        driver.find_element(By.XPATH, Locator.imput_password_reg).send_keys(Data.password)
        driver.find_element(By.XPATH, Locator.button_reg).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locator.button_login)))
        assert driver.current_url == Locator.login_page

    def test_registration_invalid_password(self,driver):
        driver.find_element(By.XPATH, Locator.login_account).click()
        driver.find_element(By.XPATH, Locator.register_button).click()
        driver.find_element(By.XPATH, Locator.imput_name_reg).send_keys(Data.name)
        driver.find_element(By.XPATH, Locator.imput_email_reg).send_keys(Data.email)
        driver.find_element(By.NAME, Locator.imput_password_login).send_keys(Data.invalid_password)
        driver.find_element(By.XPATH, Locator.button_reg).click()
        assert driver.find_element(By.XPATH, Locator.invalid_password)
