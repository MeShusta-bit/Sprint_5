from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestClickTransition(Locator):
    def test_click_transition_Sousi(self,driver):
        driver.find_element(By.XPATH, self.sousi).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.sousi_spicy)))
        assert driver.find_element(By.XPATH,'//div[contains(@class, "current")]')

    def test_click_transition_Nachinki(self,driver):
        driver.find_element(By.XPATH, self.nachinki).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.meteorite)))
        assert driver.find_element(By.XPATH,'//div[contains(@class, "current")]')

    def test_click_transition_bulki(self,driver):
        driver.find_element(By.XPATH, self.sousi).click()
        driver.find_element(By.XPATH, self.bulki).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.bulka)))
        assert driver.find_element(By.XPATH,'//div[contains(@class, "current")]')
