from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime

#############################################

#############################################
# Step 1
website_link = "https://www.thesun.co.uk/sport/football/"

chrome_driver_path = "C:\Development\chromedriver.exe"
#############################################

#############################################
# Step 2

# this options class will scrape the website  by opening it in background
# -----------------------
options = Options()
options.headless = True
# -----------------------

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)  # options=options (extra)

driver.get(website_link)

#############################################

#############################################
# Step 3

containers = driver.find_elements(By.CLASS_NAME, 'teaser__copy-container')

titles = [i.find_element(By.CLASS_NAME, 'teaser__headline').text for i in containers]
subtitles = [i.find_element(By.CLASS_NAME, 'teaser__subdeck').text for i in containers]
links = [i.find_element(By.CLASS_NAME, 'text-anchor-wrap').get_attribute("href") for i in containers]

#############################################

#############################################
# Step 4

my_dict = {"title": titles, "subtitle": subtitles, "link": links}

df = pd.DataFrame(my_dict)

date = datetime.now().strftime('%d_%m_%Y')

df.to_csv(f"file_{date}.csv")

#############################################
# Step 5

driver.quit()

#############################################
