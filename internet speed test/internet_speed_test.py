import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.speedtest.net/")

# time.sleep(10)

go = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

time.sleep(60)

download = driver.find_element(By.XPATH,
                               '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

upload = driver.find_element(By.XPATH,
                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

print(f"Your download speed is {download.text} MBit/s and your upload speed is {upload.text} MBit/s")

driver.quit()
