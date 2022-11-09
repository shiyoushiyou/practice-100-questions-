from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dataclasses import replace
from bs4 import BeautifulSoup as bs4BS
import requests


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\kmrry\OneDrive\桌面\程式語言\chromedriver")

headers = {
"Accept-Ranges": "bytes",
"Content-Type": "application/json",
"X-Content-Type-Options": "nosniff",
"X-FRAME-OPTIONS": "SAMEORIGIN",
"Referer": "https://www.kawasaki-plaza.net/sapporoshiroishi/testdrive/",
}
TestdriveList = "https://www.kawasaki-plaza.net/sapporoshiroishi/testdrive/"
driver.get(TestdriveList)

time.sleep(5)

BikeName = driver.find_elements(By.CSS_SELECTOR,".m-list-item__ttl")
BikeTestdrive = driver.find_elements(By.CSS_SELECTOR,".m-list-testdrive")

for i in range(len(BikeName)):
    if i != None:
        #print(BikeName[i].text)
        # print (BikeTestdrive[i].text)
        with open('explore.txt', 'a', encoding='utf-8') as file:
            file.write (BikeName[i].text)
            file.write ('\n')
            file.write (BikeTestdrive[i].text)
            file.write ('\n')

