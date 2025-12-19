
n=int(input("enter The Number:"))
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num=num//10
if n==result:
    print("Palindrome")
else:
    print("Not Palindrome")
