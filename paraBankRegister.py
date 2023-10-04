from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://parabank.parasoft.com/parabank/index.htm")
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Register'))).click()
wait.until(EC.presence_of_element_located((By.ID, 'customer.firstName'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.lastName'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.address.street'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.address.city'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.address.state'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.address.zipCode'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.phoneNumber'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.ssn'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.username'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'customer.password'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.ID, 'repeatedPassword'))).send_keys("s")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.button[value="Register"]'))).click()

time.sleep(5)

driver.quit()