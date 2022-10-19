#BMI計算機　・BMI電卓
'''height = int(input("你多高?"))
weight = int(input("你多重?"))
BMI = (weight/((height/100)**2))
BMI = round(BMI,1)
if BMI < 18.5:
    print(F"你的BMI是{BMI}，體重過輕")
elif 18.5 < BMI <24 :
    print(F"你的BMI是{BMI}，正常體重")
elif 24< BMI <27:
    print(F"你的BMI是{BMI}，體重過重")
elif 27< BMI<30:
    print(F"你的BMI是{BMI}，輕度肥胖")
elif 30<BMI<35:
    print(F"你的BMI是{BMI}，中度肥胖")
elif BMI>35:
    print(F"你的BMI是{BMI}，重度肥胖")'''

#算最大最小
stringA = input()
def FoundTheMax_Min():
    ListOfMax_Min = stringA.split()
    LListOfMax_Min = ListOfMax_Min.sort()
    print(LListOfMax_Min[-1]-LListOfMax_Min[0])

FoundTheMax_Min()

#點餐系統オーダーシステム
print("歡迎使用拉麵點餐機\n(1)鹽味拉麵 $220 \n(2)醬油拉麵 $240\n(3)豚骨拉麵 $280")
ramen = int(input("選一個拉麵"))
optionplus = input("是否加大，豚骨口味+$50，其他口味+$30(輸入Y or N)")
optionegg = input("是否加溏心蛋+$30(輸入Y or N)")
optionmeat = input("是否加叉燒+$60(輸入Y or N)")

saltramen = 220
soyramen = 240
pigramen = 280
bill = 0
sale = 120
if optionplus == "Y" and ramen ==3:
    bill += 50
elif  optionplus == "Y":
    bill += 30
if optionegg == "Y":
    bill +=30
if optionmeat =="Y":
    bill += 60
if ramen == 1 and bill >= sale :
    print (f"加好加滿折價$20，總金額${(saltramen + bill)-20},感謝您的光臨")
elif ramen == 1 and bill < sale :
    print (f"總金額${(saltramen + bill)},感謝您的光臨")
elif ramen == 2 and bill >= sale :
    print (f"加好加滿折價$20，總金額${(soyramen + bill)-20},感謝您的光臨")
elif ramen == 2 and bill < sale :
    print (f"總金額${(soyramen + bill)},感謝您的光臨")
elif ramen == 3 and bill >= sale:
    print (f"加好加滿折價$20，總金額${(pigramen + bill)-20},感謝您的光臨")
elif ramen == 3 and bill < sale :
    print (f"總金額${(pigramen + bill)},感謝您的光臨")



    






      
         


