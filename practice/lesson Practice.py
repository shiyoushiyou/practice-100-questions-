# 1.Write a function called "printMany" that prints out integers 1, 2, 3, ..., 100.
#  寫一個函式印出1到100
def One_to_Onehundred ():
   for i in range(1,101):
       print(i)

One_to_Onehundred()

# 2.Write a function called "printEvery3" that prints out integers 1, 4, 7, 10, ..., 88.
#  寫一個函式去列出1~88(每個數間隔3)
def printEvry3 ():
   for i  in range(1,89,3):
       print(i)
printEvry3()

# 3.Write a function called "position" that returns a tuple of the first uppercase letter and its index location. If not found, returns -1.
#  寫一個函式他會return一個tuple(字串裡的第一個大寫跟index)，如果沒有符合的就return-1
WriteSomething = input()
def position ():
   for i,item in enumerate(WriteSomething):
       if item == item.upper():
           print(i,item)
           break
       else:
           print("-1")
           break

position ()
# 4. Write a function called "findSmallCount" that takes one list of integers and one integer as input,
#   and returns an integer indicating how many elements in the list is smaller than the input integer.


def findSmallCount(listA,intB):
   counter1 = 0
   for i in listA:
       if i < intB:
           counter1 += 1
    
   return counter1

print (findSmallCount ([1, 2, 3], 2))

    
Sumall = 0
for i in range(101):
   Sumall += i

print(Sumall)

# Write a function called "findSmallerTotal" that takes one list of integers and one integer as input,
# and returns the sum of all elements in the list that are smaller than the input integer. 


def findSmallCount(listA,intB):
   Sumall = 0
   for i in listA:
      if i < intB:
       Sumall += i
   return Sumall
print (findSmallCount ([1, 2, 3,3,6,7,8,10], 99))
# Write a function called "findAllSmall" that takes one list of integers and another integer as input, 
# and returns an list of integers that contains all elements that are smaller than the input integer.


def findAllSmall(listA,intB):
   result = []
   for i in listA:
      if i < intB:  
       result.append(i) #每符合條件一次增加i元素到result
   return result
print (findAllSmall([1, 2, 3], 10)) # returns [1, 2, 3]              

# Write a function called "summ" that takes one list of numbers, 
# and return the sum of all elements in the input list.


def summ (list):
   Sumall = 0
   for i in list:
       Sumall += i
   return Sumall

print (summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) )
# Write a function called "stars" which prints out layers of stars in the following pattern:

def stars (int1):
   for i in range(1,int1+1) :
       print(i*"*")
stars(4)
# Write a function called "stars2" which 
# prints out layers of stars in the following pattern:

def stars2 (int1):
   for i in range(1,int1+1):
       print(i*"*")
   for x in range(int1-1,0,-1):
       print(x*"*")
stars2(3)
def table (n):
   count1 = 1
   for i in range (9):
       all = (n)*(count1)
       print (f'{n} X {count1} = {all}')    
       count1 += 1        
table(3)  

def table9to9 ():
    for i in range(1,10):
        for x in range (1,10):
            print(f'{i} X {x} = {i*x}')

table9to9 ()

