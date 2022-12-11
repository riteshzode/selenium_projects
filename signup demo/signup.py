from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\Development\chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

# this link is dead so this will not work
driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, "fName")
name.send_keys("Ritesh")

surname = driver.find_element(By.NAME, "lName")
surname.send_keys("singh")

email = driver.find_element(By.NAME, "email")
email.send_keys("ritesh143@gmail.com")

# enter = driver.find_element(By.CSS_SELECTOR, ".btn")
# enter.send_keys(Keys.ENTER)

enter = driver.find_element(By.CLASS_NAME, "btn")
enter.click()
# send_keys(Keys.ENTER)