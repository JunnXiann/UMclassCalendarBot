import re
import os
import getpass
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from Writer import *

url = "https://maya.um.edu.my/sitsvision/wrd/siw_lgn"
print("Please enter your MAYA credentials: ")
username = input("Username: ")
password = getpass.getpass("Password: ")
class_data = []

driverPath = "./chromedriver"
driver = webdriver.Chrome(driverPath)

driver.get(url)
driver.find_element(By.ID ,"MUA_CODE.DUMMY.MENSYS").send_keys(username)
driver.find_element(By.ID ,"PASSWORD.DUMMY.MENSYS").send_keys(password)
driver.find_element(By.NAME ,"BP101.DUMMY_B.MENSYS").click()
driver.find_element(By.XPATH,'//a[@href="javascript:timetable_popup();"]').click()
driver.find_element(By.ID, "sits_dialog").find_elements(By.TAG_NAME, "a")[0].click()
driver.find_element(By.NAME, "BP102.DUMMY_B.MENSYS").click()
classes = driver.find_element(By.CLASS_NAME, "sitsjqttitems").find_elements(By.TAG_NAME,"li")
for Class in classes:
    data = Class.text.splitlines()
    string = Class.get_attribute("tt-tooltip")
    m = re.search(r'[A-Za-z]{3}\.', string)
    data_json = {
        "date": m.group(0).strip("."),
        "time": data[1],
        "occurrence": data[2].strip("Occurence: "),
        "code": data[3].strip("Code: "),
        "semester": data[4],
        "type": data[5],
        "campus": data[6],
        "room": data[7],
        "lecturer": data[8].replace('Lecturer: ',''),
    }
    class_data.append(data_json)
driver.quit()

cal = Calendar()

for data in class_data:
    cal.add_component(write(username, password, data["date"], data["time"], data["occurrence"], data["code"], data["room"], data["lecturer"]))

directory = '/Users/junxian/Desktop'
f = open(os.path.join(directory, 'class.ics'), 'wb')
f.write(cal.to_ical())
f.close()