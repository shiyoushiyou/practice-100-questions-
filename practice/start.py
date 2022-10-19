# 是註解，用於紀錄或說明
#cls是清空終端機內容，撰寫程式檔案副檔名用py
#執行程式：python 檔案名稱
print("Hello Python")
#資料的分類：整數.長整數.浮點數(小數)
#數字ex 12354
#字串把想表達的文字用雙引號框起來
#布林值 True False
# 有順序，可動的列表list
print(round(2.5))
#round 是四捨五入。當進位的數字是基數，那就會round down，是偶數就會正常進位
#typecasting把一種資料型態轉換成另一個資料型態
#ex.把字串轉整數字
print(int(3.0))
print(float(3))
#Math Module
#e,pi(常數的一種)
#floor(無條件捨去),ceil(無條件進位),sqrt(sqare root的縮寫開根號)
import math
from opcode import haslocal
from winreg import HKEY_LOCAL_MACHINE
from xmlrpc.server import SimpleXMLRPCRequestHandler
print(math.e)
print(math.pi)
print(math.floor(4.9999))
print(math.ceil(4.67657))
print(math.sqrt(36))

x=5
x=x+1#x=x+1跟x+=1是一樣的，
print(x)

#strings是有順序性.連續性的句子，ex Aloha 
# 字串六大規則
#pyhton的字串有順序，順序從零開始算，字串有可切割性
# ex.hello可以取ell來print
x='hello'
#  01234
#  h    o  l  l  e
#-5or0 -4 -3 -2 -1
print(x[3])
print(x[1:4])
#切割時包含起點不含終點
#len計算長度，upper變成大寫，lower變成小寫
print(len("shiyou"))
name = "shiyou"
print(name.upper())
print(name.lower()) 
print(name.isupper())
print(name.islower())
print(name.upper().isupper())
#index 索引
name="Shiyou"
print(name.index("i"))
#replace替代
name="Shiyou"
print(name.replace("Shi","syu"))
#split 從字串中排序
x="今天 天氣 很好"
print(x.split(" "))
#list 一樣是排序但是是每個字被排序
print(list(x))
friends=["a","b","v","as"]
friends.insert(2,"shiyou")
print(friends)
friends.remove("v")
print(friends)
friends.sort()
print(friends)

#a = int(input("給我一個數字:"))
#b = int(input("在給我一個數字:"))
#print(a-b)

person = {"name":"shiyou","age":"26"}
print(person["name"])

a = [3,567,786,4,87,32]
a.sort()
print(a)

print(8+5)
print(8-5)
print(8*5)
print(8/5)
a = str(8//5)
b = str(8%5)

print(a+'余り'+b)

#a = int(input("好きな整数を入力してください:"))
#b = int(input("もう一つ整数を入力してください:"))
#print(f"{a}x{b}={a*b}")

#b = int(input("給我一個數字:"))

#if (b%2)==0:
    #print("偶數")
#else:
    #print("奇術")

a = [1,43,465,54,23,6,7]
a.sort() 
print(a)
#x = set()
#x.add(100)
#print(x)










