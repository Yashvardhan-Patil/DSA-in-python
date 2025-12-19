# 1st method
num=int(input("Enter The Number:"))
result=[]
for i in range (1,num+1):
    if num%i==0:
        result.append(i)
print(result)

# 2nd method
from math import sqrt
num=int(input("enter the number:"))
result=[]
for i in range (1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
    if num//i!=i:
        result.append(num//i)
result.sort()
print(result)