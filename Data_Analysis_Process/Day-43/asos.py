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
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(service=driver_path, options=chrome_options)

driver.get("https://www.asos.com/men")

driver.find_element(
    by=By.XPATH,
    value='//*[@id="chrome-sticky-header"]/div[2]/div[2]/nav/div/div/button[2]',
).click()

driver.find_element(
    by=By.XPATH,
    value='//*[@id="029c47b3-2111-43e9-9138-0d00ecf0b3db"]/div/div[2]/div/div[1]/ul/li[1]/a',
).click()

# driver.find_element(by=By.XPATH, value='//*[@id="plp"]/div/div[1]/div[2]/div/a').click()

old_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.find_element(
        by=By.XPATH, value='//*[@id="plp"]/div/div[1]/div[2]/div/a'
    ).click()

    new_height = driver.execute_script("return document.body.scrollHeight")

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break
    old_height = new_height

html = driver.page_source
with open("./Advance_Web_Scrapping_Selenium/asos.html", "w", encoding="utf-8") as f:
    f.write(html)
