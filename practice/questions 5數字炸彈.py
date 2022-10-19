#數字炸彈
#會有一個隨機數字，玩家要輸入數字，猜到隨機數字的人輸。
#重點:每輸入一次數字，範圍就會改變。猜對了數字，遊戲就結束。

#先寫一個function去判斷每一次的input後的範圍
#然後讓每一次的computer固定之後讓TheInput變動
import random


MinValue = 1
MaxValue = 100
computer = random.randint(1,100)
print(computer)

while True:
    TheInput = int(input(f"Please give me a numer between:{MinValue}and{MaxValue}"))
    if  TheInput < MinValue or TheInput > MaxValue:
        print(f"No!Please give me a numer between:{MinValue}and{MaxValue}")
        continue
    if TheInput <  computer:
            MinValue = TheInput
            print (f'猜{TheInput}~{MaxValue}之間')    
            TheInput = int(input(f"Please give me a numer between:{TheInput}and{MaxValue}"))
    elif computer < TheInput:
            MaxValue = TheInput
            print (f'猜{MinValue}~{TheInput}之間')
            TheInput = int(input(f"Please give me a numer between:{MinValue}and{TheInput}"))
    if TheInput == computer:
            print ("you lose!!")
            break



