from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_first_item_name(self):
       items = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
       first_item = items[0]
       return first_item.text
    def sort_by(self, option):
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_visible_text(option)
    def add_to_cart(self, item_name):
        self.driver.find_element(By.CSS_SELECTOR, f"[data-test='add-to-cart-{item_name}']").click()
    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()
class CartPage:
    def __init__(self, driver):
        self.driver = driver
    def get_cart_items(self):
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
        return [item.text for item in cart_items]
    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
    