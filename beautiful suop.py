from bs4 import BeautifulSoup as bs4BS
import requests


result = requests.get("https://news.yahoo.co.jp/ranking/access/news/business")
news = bs4BS(result.text,"html.parser")
newstitle = news.find_all("div",class_="newsFeed_item_title")
newslink = news.find_all ("a",class_ ="newsFeed_item_link")

# for i in range (10):
#     if newstitle[i] !=None:
#         print(newstitle[i].text)
        




