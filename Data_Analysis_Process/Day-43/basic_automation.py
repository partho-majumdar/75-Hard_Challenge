# open google
# search campusX
# learnwith.campusx.in
# dsmp course page

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
driver.get("https://google.com")

time.sleep(1)

# fetch the search input box using xpath
user_input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys("CampusX")

time.sleep(1)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(
    by=By.XPATH, value='//*[@id="ixcYae"]/div/div/div/div/div/div/div[1]/div/span/a'
)
link.click()
time.sleep(1)

link2 = driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/header/section[2]/a[1]"
)
link2.click()
