from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest 


def test_login_form(driver, wait):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "Swag Labs" in driver.title
def test_wrong_password(driver, wait):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Epic sadface: Username and password do not match any user in this service" in  error.text
def test_empty_space(driver, wait):
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert  "Epic sadface: Username is required" in error.text
def test_locked_user(driver, wait):
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Epic sadface: Sorry, this user has been locked out." in error.text
def test_sorting(driver, wait):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_visible_text("Name (Z to A)")
    items = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    first_item = items[0]
    assert "Test.allTheThings() T-Shirt (Red)" in first_item.text