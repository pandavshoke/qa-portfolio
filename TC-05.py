from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "user-name")))
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_visible_text("Name (Z to A)")
items = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
first_item = items[0]
assert "Test.allTheThings() T-Shirt (Red)" in first_item.text
print("Форма заполнена!")
input("Нажми Enter чтобы закрыть...")