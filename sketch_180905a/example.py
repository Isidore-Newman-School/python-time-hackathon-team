import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# soup = BeautifulSoup(page.content, 'html.parser')
driver = webdriver.Chrome()
driver.get("https://www.newmanschool.org/page/calendar?showAll=1&sDate=20180901&eDate=20180930&selStartDate=20180901&selEndDate=20180930&siteId=&tab=1&ec=0_5373%2C0_1797%2C0_2072%2C0_2075%2C0_13161%2C0_8205%2C0_8206%2C0_5628%2C0_5673%2C0_8207&ts=")
timeout = 20
soup = BeautifulSoup(driver.page_source, 'html.parser')
calendar = driver.find_element_by_id(id_='content_924422')
nineteenth = calendar.find_all('calendar-days')[0]
# print(calendar)

print(soup.find_all('div')[0])








# page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
# soup = BeautifulSoup(page.content, 'html.parser')
# seven_day = soup.find(id = "seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")
# tonight = forecast_items[0]
# print(tonight.prettify())
# # tonightForecast = tonight.get_text()
# # print(tonightForecast)
# periodName = tonight.find(class_="period-name").get_text()
# shortDesc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp temp-high").get_text()
# print(periodName)
# print(shortDesc)
# print(temp)

# page = requests.get("https://en.wikipedia.org/wiki/Warring_States_period")
# soup = BeautifulSoup(page.content, 'html.parser')
# refrence = soup.find(id="toc")
# shangYang = refrence.find(class_="toclevel-2 tocsection-11")
# print(shangYang.get_text())


# page = requests.get("https://www.newmanschool.org/page/calendar?showAll=1&sDate=20180901&eDate=20180930&selStartDate=20180901&selEndDate=20180930&siteId=&tab=1&ec=0_5373%2C0_1797%2C0_2072%2C0_2075%2C0_13161%2C0_8205%2C0_8206%2C0_5628%2C0_5673%2C0_8207&ts=")
# soup = BeautifulSoup(page.content, 'html.parser')
# header = soup.find(id = "content_414")
# newman = header.find(class_="mm-title")

# page = requests.get("https://en.wikipedia.org/wiki/Warring_States_period")
# soup = BeautifulSoup(page.content, 'html.parser')
# title = soup.find()
