from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locator
from data import Data


class TestExitCustomer:
    def test_click_exit_customer_account(self,driver):
        driver.find_element(By.XPATH, Locator.login_account).click()
        driver.find_element(By.NAME, Locator.imput_name_login).send_keys(Data.email)
        driver.find_element(By.NAME, Locator.imput_password_login).send_keys(Data.password)
        driver.find_element(By.XPATH, Locator.button_login).click()
        driver.find_element(By.XPATH, Locator.personal_account).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locator.button_logout)))
        driver.find_element(By.XPATH, Locator.button_logout).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locator.button_login)))
        assert driver.current_url == Locator.login_page