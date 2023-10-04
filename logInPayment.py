from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_example():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("s")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("s")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"].button[value="Log In"]'))).click()

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Bill Pay'))).click()
    wait.until(EC.presence_of_element_located((By.NAME, 'payee.name'))).send_keys("s")
    wait.until(EC.presence_of_element_located((By.NAME, 'payee.address.street'))).send_keys("s")
    wait.until(EC.presence_of_element_located((By.NAME, 'payee.address.city'))).send_keys("s")
    wait.until(EC.presence_of_element_located((By.NAME, 'payee.address.state'))).send_keys("s")
    wait.until(EC.presence_of_element_located((By.NAME, 'payee.address.zipCode'))).send_keys("s")
    wait.until(EC.presence_of_element_located((By.NAME, 'payee.phoneNumber'))).send_keys("s")
    wait.until(EC.presence_of_element_located((By.NAME, 'payee.accountNumber'))).send_keys("1")
    wait.until(EC.presence_of_element_located((By.NAME, 'verifyAccount'))).send_keys("1")
    wait.until(EC.presence_of_element_located((By.NAME, 'amount'))).send_keys("1")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.button[value="Send Payment"]'))).click()

    time.sleep(5)

    driver.quit()

test_example()