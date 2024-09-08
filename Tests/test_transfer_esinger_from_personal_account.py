from selenium.webdriver.common.by import By
from locators import *
from data import *

class TestCustomerAccount(Locator,Data):
    def test_click_desinger_customer_account(self,driver):
        driver.find_element(By.XPATH, self.login_account).click()
        driver.find_element(By.NAME, self.imput_name_login).send_keys(self.name)
        driver.find_element(By.NAME, self.imput_password_login).send_keys(self.password)
        driver.find_element(By.XPATH,self.button_login).click()
        driver.find_element(By.XPATH, self.personal_account).click()
        driver.find_element(By.XPATH, self.constructor).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_click_logo_customer_account(self,driver):
        driver.find_element(By.XPATH, self.login_account).click()
        driver.find_element(By.NAME, self.imput_name_login).send_keys(self.name)
        driver.find_element(By.NAME, self.imput_password_login).send_keys(self.password)
        driver.find_element(By.XPATH, self.button_login).click()
        driver.find_element(By.XPATH, self.personal_account).click()
        driver.find_element(By.XPATH, self.button_stellar).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
