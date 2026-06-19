from POM import LoginPage, InventoryPage, CartPage
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import Select

def test_login(driver):
    page = LoginPage(driver)
    page.enter_username("standard_user")
    page.enter_password("secret_sauce")
    page.click_login()
    assert "Swag Labs" in driver.title
def test_sorting(driver):
    page = LoginPage(driver)
    page.enter_username("standard_user")
    page.enter_password("secret_sauce")
    page.click_login()
    page2 = InventoryPage(driver)
    page2.sort_by("Name (Z to A)")
    result = page2.get_first_item_name()
    assert "Test.allTheThings() T-Shirt (Red)" in result
def test_cart_page(driver):
    page = LoginPage(driver)
    page.enter_username("standard_user")
    page.enter_password("secret_sauce")
    page.click_login()
    page2 = InventoryPage(driver)
    page2.add_to_cart("sauce-labs-bolt-t-shirt")
    page2.go_to_cart()
    page3 = CartPage(driver)
    result = page3.get_cart_items()
    assert "Sauce Labs Bolt T-Shirt" in result

