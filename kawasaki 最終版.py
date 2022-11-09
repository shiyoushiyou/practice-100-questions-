from dataclasses import replace
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs4BS
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

#抓取店家資訊
TestdriveList = "https://www.kawasaki-plaza.net/sapporoshiroishi/testdrive/"
driver.get(TestdriveList)
time.sleep(5)
#車名
BikeName = driver.find_elements(By.CSS_SELECTOR,".m-list-item__ttl")
BikeTestdrive = driver.find_elements(By.CSS_SELECTOR,".m-list-testdrive")

Status_show = []
Status_test = []
Status_rent = []
BikeNameList = []
BikeStatusList = []
        
for i in range(len(BikeName)):
    bikes = bs4BS(BikeName[i].text,"html.parser")
    bike = str(bikes).replace(" ","")#把車輛名稱轉list
    bikeStatus = bs4BS(BikeTestdrive[i].text,"html.parser")
    BikeStatus = str(bikeStatus).replace("(要予約*)","").replace("\n","")#把車輛狀態轉list

    BikeNameList.append(bike)
    BikeStatusList.append(BikeStatus)#新增元素到list

for s in BikeStatusList:
    if(s.find("展示") ):
        Status_show.append("展示")    
    else:
        Status_show.append("")

    if(s.find("試乗") ):
        Status_test.append("試乗")
    else:
        Status_test.append("")
        
    if(s.find("レンタル")):
        Status_rent.append("レンタル")
    else:
        Status_rent.append("")

data ={'車輛名稱':BikeNameList,
       '車輛status1':Status_show,
       '車輛status2':Status_test,
       '車輛status3':Status_rent
        }
data = pd.DataFrame(data)
data.to_excel('kawasaki.xlsx',index = False)


        


   


