# 算point　ポイント計算
# 通常是買的金額x1%，但日期有3的數字就是3%，有5的是5%
# 一個月裡面有三的有3,13 23,30,31`
# 五的有5,15,25 
Point = 0
Count = int(input())
AllDayof3 =["3","13","23","30","31"]
AllDayof5 =["5","15","25"]

for i in range (Count):
    Bill = input()
    payDay,Payment = Bill.split()
    if payDay in AllDayof3 :
        PayDay3Point = int(Payment)*0.03
        Point += int(PayDay3Point)
    elif payDay in AllDayof5:
        PayDay5Point = int(Payment)*0.05
        Point += int(PayDay5Point)        
    else :
        usually = int(Payment)*0.01
        Point += int(usually)
        
print (Point)



