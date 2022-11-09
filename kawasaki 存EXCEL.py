#抓取每一個kawasaki店家的持有車輛，並且計算出各店家車輛的狀態。


from dataclasses import replace
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs4BS
import requests
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
#抓取車輛資訊
TestdriveList = "https://www.kawasaki-plaza.net/sapporoshiroishi/testdrive/"
driver.get(TestdriveList)
time.sleep(5)
#pandas的設定
path = 'kawasaki.xlsx'
df = pd.DataFrame()

Status_show = []
Status_test = []
Status_rent = []
BikeNameList = []
BikeStatusList = []

for i in range(len(ShopList)): #loop跑shoplist有多長就跑多少次
    StoreLink = ShopList[i].a["href"]#找他的href
    StoreLink = StoreLink.replace('../','')
    if ShopList[i] != None:
        TotalTestdriveList = f'https://www.kawasaki-plaza.net/{StoreLink}testdrive/'
        TestdriveList = TotalTestdriveList#把TotalTestdriveList 放進testdrivelist ，一個迴圈跑一個
        driver.get(TestdriveList)
        time.sleep(5)
        BikeNames = driver.find_elements(By.CSS_SELECTOR,".m-list-item__ttl")       
        for x in range(len(BikeNames)):#判斷車子跟狀態
            bikes = bs4BS(BikeNames[x].text,"html.parser")
            BikeTestdrive = driver.find_elements(By.CSS_SELECTOR,".m-list-testdrive")
            bikeStatus = bs4BS(BikeTestdrive[x].text,"html.parser")

            BikeName= str(bikes).replace(" ","")#把車輛名稱轉list
            BikeStatus = str(bikeStatus).replace("(要予約*)","").replace("\n","")#把車輛狀態轉list

            BikeNameList.append(BikeName)
            BikeStatusList.append(BikeStatus)#新增元素到list

        for s in BikeStatusList:#判斷有沒有符合
            if(s.find("展示")!= -1 ):
                Status_show.append(1)    
            else:
                Status_show.append("")
            if(s.find("試乗")!= -1 ):
                Status_test.append(1)
            else:
                Status_test.append("")
            if(s.find("レンタル")!= -1):
                Status_rent.append(1)
            else:
                Status_rent.append("")

    data ={'車輛名稱':BikeNameList,
        '展示車両':Status_show,
        '試乗車':Status_test,
        'レンタル車両':Status_rent
            }       
    data = pd.DataFrame(data)
    #製作工作頁
    ShopName =str(ShopNames[i].text)
    shopNames =ShopName.replace("カワサキ プラザ","")  
    with pd.ExcelWriter(path,engine = 'openpyxl',mode ='a')as writer:
        data.to_excel(writer,index = False,sheet_name = shopNames)

    Status_show.clear()
    Status_test.clear()
    Status_rent.clear()
    BikeNameList.clear()
    BikeStatusList.clear()
