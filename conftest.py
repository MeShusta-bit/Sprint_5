import pytest
from selenium import webdriver



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')
    return driver
    driver.quit()







