from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# convert python Latest News and Upcoming Events to csv
import pandas as pd

chrome_driver_path = "C:\Development\chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

# Python Upcoming Events

times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
texts = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

dict1 = {
    "Date": [i.text for i in times],
    "Event Name": [i.text for i in texts][:len(times)],
    "Event Link": [i.get_attribute("href") for i in texts][:len(times)]
}
df1 = pd.DataFrame(dict1)
df1.to_csv("events_python.csv")

# Python Latest News

times_n = driver.find_elements(By.CSS_SELECTOR, ".medium-widget time")
texts_n = driver.find_elements(By.CSS_SELECTOR, ".medium-widget li a")


dict2 = {
    "Date": [i.text for i in times_n],
    "News": [i.text for i in texts_n][:len(times_n)],
    "Link": [i.get_attribute("href") for i in texts_n][:len(times_n)]
}


df2 = pd.DataFrame(dict2)
df2.to_csv("news_python.csv")

driver.quit()
