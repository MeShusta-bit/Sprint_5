from selenium.webdriver.common.by import By
from selenium import webdriver



def test_click_transition_Sousi(driver):
    driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
    assert driver.find_element(By.XPATH,'//div[contains(@class, "current")]')
    driver.quit()

def test_click_transition_Nachinki(driver):
    driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
    assert driver.find_element(By.XPATH,'//div[contains(@class, "current")]')
    driver.quit()

def test_click_transition_Bulki(driver):
    driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
    driver.find_element(By.XPATH, "//span[text()='Булки']").click()
    assert driver.find_element(By.XPATH,'//div[contains(@class, "current")]')
    driver.quit()