from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com")
wait= WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "user-name")))
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
assert "Swag Labs" in driver.title
print("Форма заполнена!")
input("Нажми Enter чтобы закрыть...")
