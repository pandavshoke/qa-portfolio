from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_title():
    driver = webdriver.Firefox()
    driver.get("https://djinni.co")
    assert "Джин" in driver.title
    driver.quit()
def test_login_form():
    driver = webdriver.Firefox()
    driver.get("https://djinni.co/login")
    assert driver.find_element(By.ID, "email").is_displayed()
    driver.quit()
def test_register_link():
    driver = webdriver.Firefox()
    driver.get("https://djinni.co/login")
    assert driver.find_element(By.LINK_TEXT, "Зареєструватись").is_displayed()
    driver.quit()