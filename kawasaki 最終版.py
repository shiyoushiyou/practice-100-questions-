from dataclasses import replace
from bs4 import BeautifulSoup as bs4BS
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#selenium的 設定
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
#抓店家資訊

url ="https://www.kawasaki-plaza.net/shop/"
request =requests.get (url)
data = bs4BS(request.text,"html.parser",)
ShopList = data.find_all("div",class_="m-grid-shop__content")
ShopNames = data.find_all("p",class_="m-grid-shop__ttl")



for i in range(len(ShopList)): #loop跑shoplist有多長就跑多少次
    StoreLink = ShopList[i].a["href"]#找他的href
    StoreLink = StoreLink.replace('../','')
    
    if ShopList[i] != None:
        TotalTestdriveList = f'https://www.kawasaki-plaza.net/{StoreLink}testdrive/'
        TestdriveList = TotalTestdriveList#把TotalTestdriveList 放進testdrivelist ，一個迴圈跑一個
        driver.get(TestdriveList)
        time.sleep(5)
        BikeName = driver.find_elements(By.CSS_SELECTOR,".m-list-item__ttl")#因為迴圈會更新testdrivelist，所以要把BikeName放進迴圈一起更新
        BikeTestdrive = driver.find_elements(By.CSS_SELECTOR,".m-list-testdrive")
        
        print(ShopNames[i].text)
    for NumBike in range(len(BikeName)):
        print(BikeName[NumBike].text,BikeTestdrive[NumBike].text)
        


        


   


