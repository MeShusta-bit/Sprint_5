from selenium.webdriver.common.by import By
from locators import *
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLoginButton(Locator,Data):
    def test_click_customer_account(self,driver):
        driver.find_element(By.XPATH, self.login_account).click()
        driver.find_element(By.NAME, self.imput_name_login).send_keys(
        self.name)
        driver.find_element(By.NAME, self.imput_password_login).send_keys(self.password)
        driver.find_element(By.XPATH, self.button_login).click()
        driver.find_element(By.XPATH, self.personal_account).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.save_button)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

