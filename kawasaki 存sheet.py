import openpyxl 
from bs4 import BeautifulSoup as bs4BS
import requests
import pandas as pd
url ="https://www.kawasaki-plaza.net/shop/"
request =requests.get (url)
data = bs4BS(request.text,"html.parser",)
ShopList = data.find_all("div",class_="m-grid-shop__content")
ShopNames = data.find_all("p",class_="m-grid-shop__ttl")
count = len(ShopList)
path = 'kawasaki.xlsx'
df = pd.DataFrame()
for i in range(count): #loop跑shoplist有多長就跑多少次
    if ShopNames[i] != None:
        ShopName =str(ShopNames[i].text)
        shopNames =ShopName.replace("カワサキ プラザ","")  
    with pd.ExcelWriter(path,engine = 'openpyxl',mode ='a')as writer:
        df.to_excel(writer,index =False,sheet_name = shopNames)
