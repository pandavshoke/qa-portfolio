from POM import LoginPage, InventoryPage
import pytest

def test_login(driver):
    page = LoginPage(driver)
    page.enter_username("standard_user")
    page.enter_password("secret_sauce")
    page.click_login()
    assert "Swag Labs" in driver.title