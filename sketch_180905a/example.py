import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.newmanschool.org/page/calendar?showAll=1&sDate=20180901&eDate=20180930&selStartDate=20180901&selEndDate=20180930&siteId=&tab=1&ec=0_5373%2C0_1797%2C0_2072%2C0_2075%2C0_13161%2C0_8205%2C0_8206%2C0_5628%2C0_5673%2C0_8207&ts=")

soup = BeautifulSoup(driver.page_source, 'html.parser')
calendar = soup.find(id="content_924422")
days = calendar.find_all('div', class_="day")
# print(days[0].text)

def getEventsToday():
    T = datetime.timetuple(datetime.utcnow())
    x,x,day,x,x,x,x,x,x = T
    today = days[day+5].text
    print(days[day])
    # return(today)

getEventsToday()
