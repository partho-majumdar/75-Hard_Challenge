from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = Service(
    "E:/DATA-SCIENCE AND MECHINE LEARNING/chromedriver-win64/chromedriver.exe"
)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(service=driver_path, options=chrome_options)

driver.get("https://www.ajio.com/men-backpacks/c/830201001")

height = driver.execute_script(
    "return document.body.scrollHeight"
)  # --> scroll page automatically one time

old_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    new_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    if new_height == old_height:
        break
    ols_height = new_height

html = driver.page_source
with open("./Advance_Web_Scrapping_Selenium/ajio.html", "w", encoding="utf-8") as f:
    f.write(html)
