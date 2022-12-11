from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # t = driver.find_element(By.ID, 'articlecount')
# t = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(t.text)
# t.click()

# link = driver.find_element(By.LINK_TEXT, "Talk")
#
# link.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# go = driver.find_element(By.NAME, "go")
# go.click()
