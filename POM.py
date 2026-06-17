from selenium.webdriver.common.by import By


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