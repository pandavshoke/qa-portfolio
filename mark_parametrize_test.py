from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest 

@pytest.mark.parametrize("username, password, expected_error",[
    ("standard_user", "wrongpassword", "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("", "", "Epic sadface: Username is required"),
    ])
def test_login_errors(driver, wait, username, password, expected_error):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert expected_error in error.text