n=int(input("Enter The Number:"))
num=n
total=0
nod=len(str(n)) #nod=number of digits
while num>0:
    ld=num%10
    total=total+(ld**nod)
    num=num//10
if total==n:
    print("Armstrong Number")
else:
    print("Not an armstrong number")