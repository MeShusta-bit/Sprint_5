import pytest
from selenium import webdriver
import secrets


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')
    return driver
    driver.quit()

@pytest.fixture
def email_generator():
    return f"{secrets.token_hex(8)}@gmail.com"





