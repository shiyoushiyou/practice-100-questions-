# バス代の計算,pointある場合はポイントが先に使われる
#計算車錢，print剩下的車錢跟點數。
#條件：點數大於車錢，車錢會被抵掉。用點數抵車錢就不會拿到新的點數
#通常函式才會用return

def is_number(s):#判斷input進來的值是否符合所需格式。
    #如果不是就pass是的話就return True
    try:
        int(s)
        return True
    except ValueError:
        pass

money = input()#餘額
while not(is_number(money)) :#當函式不等於True時進入whlie
     print("你在輸入什麼?")
     money = input()
money = int(money)

buscount = input()#搭幾次車
while not(is_number(buscount )) :
     print("你在輸入什麼?")
     buscount  = input()
buscount = int(buscount)
point = 0


for i in range(int(buscount)):
    busmoney = input()#車錢

    while not(is_number(busmoney)) :
        print("你在輸入什麼?")
        busmoney  = input()
    if point > (int(busmoney)):
        point -=  int(busmoney)
        #point減車錢之後回傳值到point

    elif money > int(busmoney) :
        money -=int(busmoney) #剩多少錢
        point += float(busmoney)*0.1#搭車拿到的點數
    else:    
        print("給錢")
    
    print(int(point))
    print(money)
    



    

    

    

    





