#じゃんけん大会
#剪刀石頭布
import random
print("請輸入1.石頭2.剪刀3.布")

wincount = 0
losecount = 0

def Onemoretime (x,y): #x,y是一個代數，沒什麼意義。
  computer = random.randint(1,3)#random.randint是從範圍之中隨機出數字
  user = int(input())
  if user >3:
    print("再輸入一次:")#當這個條件被滿足，就會去執行whlie所以可以再輸入一次
  elif user ==3 and int(computer) ==1:
    print(user,computer)
    print("你贏了")
    x += 1
  elif  user  == int(computer):
    print(user,computer)
    print("平手")
  elif user >int(computer):
    print(user,computer)
    print("你輸了")
    y+= 1
  elif user <int(computer):
    print(user,computer)
    print("你贏了")
    x += 1
  return(x,y) #把計算到的值放回x,y

while (wincount<2) and (losecount<2): #當...的時候就跑...
#當   wincount<2跟losecount<2的時候就執行onemoretime
  (wincount,losecount) = Onemoretime(wincount,losecount)#onemoretime()理面放參數是為了要讓值放回x,y

#猜數字
