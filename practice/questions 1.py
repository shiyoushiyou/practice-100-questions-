
#判斷每個input進來的值與前一個值相比ture or false

string = input()
list = string.split()
result1 = True #這是變數
for i,item in enumerate (list):
    if (i+1) < len(list): #判斷list的長度，如果超過就停
        str1 = list[i]
        str2 = list[i+1]
        strhead = str2[0] #string 的 slicing 
        strtell = str1[-1]
        if strhead != strtell:
            print(strtell,strhead)
            result1 = False 
            break
if result1 == True:
    print("棒棒棒!")

    
    
      
       
    





