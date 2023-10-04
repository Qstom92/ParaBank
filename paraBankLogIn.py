from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://parabank.parasoft.com/parabank/index.htm")
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("s")
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("s")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"].button[value="Log In"]'))).click()

time.sleep(5)

driver.quit()