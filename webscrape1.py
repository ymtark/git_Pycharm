from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
# options.add_argument("headless")

s = Service("C:/Dev/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://www.python.org/"
driver.get(url)

event_times = driver.find_elements(by="css selector", value=".event-widget li time")
event_titles = driver.find_elements(by="css selector", value=".event-widget li a")

events = {}
for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_titles[i].text
    }

print(events)

driver.quit()
