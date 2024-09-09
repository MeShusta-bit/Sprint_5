from selenium.webdriver.common.by import By
from locators import Locator



class TestClickTransition:
    def test_click_transition_Sousi(self,driver):
        driver.find_element(By.XPATH, Locator.sousi).click()
        assert driver.find_element(By.XPATH, (Locator.sousi and Locator.section_selected))

    def test_click_transition_Nachinki(self,driver):
        driver.find_element(By.XPATH, Locator.nachinki).click()
        assert driver.find_element(By.XPATH,(Locator.nachinki and Locator.section_selected))

    def test_click_transition_bulki(self,driver):
        driver.find_element(By.XPATH, Locator.sousi).click()
        driver.find_element(By.XPATH, Locator.bulki).click()
        assert driver.find_element(By.XPATH,(Locator.bulki and Locator.section_selected))
