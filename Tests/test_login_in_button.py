from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locator
from data import Data


class TestLoginButton:
    def test_login_button_private_account(self,driver):
        driver.find_element(By.XPATH, Locator.personal_account).click()
        driver.find_element(By.NAME, Locator.imput_name_login).send_keys(Data.email)
        driver.find_element(By.NAME, Locator.imput_password_login).send_keys(Data.password)
        driver.find_element(By.XPATH, Locator.button_login).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locator.place_an_order)))
        assert driver.current_url == Locator.home_page


    def test_login_button_personal_account(self,driver):
        driver.find_element(By.XPATH, Locator.personal_account).click()
        driver.find_element(By.NAME, Locator.imput_name_login).send_keys(Data.email)
        driver.find_element(By.NAME, Locator.imput_password_login).send_keys(Data.password)
        driver.find_element(By.XPATH, Locator.button_login).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locator.place_an_order)))
        assert driver.current_url == Locator.home_page

    def test_login_button_in_registration_form(self,driver):
        driver.find_element(By.XPATH, Locator.personal_account).click()
        driver.find_element(By.XPATH, Locator.register_button).click()
        driver.find_element(By.XPATH, Locator.button_login_1).click()
        driver.find_element(By.NAME, Locator.imput_name_login).send_keys(Data.email)
        driver.find_element(By.NAME, Locator.imput_password_login).send_keys(Data.password)
        driver.find_element(By.XPATH, Locator.button_login).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locator.place_an_order)))
        assert driver.current_url == Locator.home_page

    def test_login_button_in_password_recovery_form(self,driver):
        driver.find_element(By.XPATH, Locator.personal_account).click()
        driver.find_element(By.XPATH, Locator.button_recover_password).click()
        driver.find_element(By.XPATH, Locator.button_login_1).click()
        driver.find_element(By.NAME, Locator.imput_name_login).send_keys(Data.email)
        driver.find_element(By.NAME, Locator.imput_password_login).send_keys(Data.password)
        driver.find_element(By.XPATH, Locator.button_login).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locator.place_an_order)))
        assert driver.current_url == Locator.home_page
