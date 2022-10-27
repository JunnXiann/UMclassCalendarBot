import os
from selenium import webdriver

def loginBot(username, password, url):
    driverPath = "/Users/junxian/Downloads/chromedriver"

    driver = webdriver.Chrome(driverPath)
    driver.get(url)

    driver.findElementByName



url = "https://maya.um.edu.my/sitsvision/wrd/SIW_XTTB"