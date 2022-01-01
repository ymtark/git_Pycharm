from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s = Service("C:/Dev/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

# article_count = driver.find_element(by="css selector", value="#articlecount a")
# article_count.click()

# all_portals = driver.find_element(by="link text", value="All portals")
# all_portals.click()

search = driver.find_element(by="name", value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)