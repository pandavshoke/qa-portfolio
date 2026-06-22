from POM import LoginPage, InventoryPage, CartPage, CheckoutPage
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
def test_checkout(driver):
    page = LoginPage(driver)
    page.enter_username("standard_user")
    page.enter_password("secret_sauce")
    page.click_login()
    page2 = InventoryPage(driver)
    page2.add_to_cart("sauce-labs-bolt-t-shirt")
    page2.go_to_cart()
    page3 = CartPage(driver)
    page3.click_checkout()
    page4 = CheckoutPage(driver)
    page4.firstName("panda")
    page4.lastName("vshoke")
    page4.postalCode("88000")
    page4.click_continue()
    page4.click_finish()
    result = page4.get_success_message()
    assert "Thank you for your order" in result


  

