from selenium.webdriver.common.by import By
from locators import Locator
from data import Data


class TestCustomerAccount:
    def test_click_desinger_customer_account(self,driver):
        driver.find_element(By.XPATH, Locator.login_account).click()
        driver.find_element(By.NAME, Locator.imput_name_login).send_keys(Data.email)
        driver.find_element(By.NAME, Locator.imput_password_login).send_keys(Data.password)
        driver.find_element(By.XPATH,Locator.button_login).click()
        driver.find_element(By.XPATH, Locator.personal_account).click()
        driver.find_element(By.XPATH, Locator.constructor).click()
        assert driver.current_url == Locator.home_page

    def test_click_logo_customer_account(self,driver):
        driver.find_element(By.XPATH, Locator.login_account).click()
        driver.find_element(By.NAME, Locator.imput_name_login).send_keys(Data.email)
        driver.find_element(By.NAME, Locator.imput_password_login).send_keys(Data.password)
        driver.find_element(By.XPATH, Locator.button_login).click()
        driver.find_element(By.XPATH, Locator.personal_account).click()
        driver.find_element(By.XPATH, Locator.button_stellar).click()
        assert driver.current_url == Locator.home_page
