#sum of 1 to n using recursion
sum=0
def fuct(sum,i,n):
    if i>n:
        print(sum)
        return
    fuct(sum+i,i+1,n)
fuct(sum,1,5)

#Using functional
print("Second question=")
def funct(n):
    if n==1:
        return 1
    
    return n+funct(n-1)
print(funct(5))

print("Third question=")

def Fact(n):
    if n==0:
        return 1
    return n*Fact(n-1)
n=int(input("Enter The number:"))
print(f"The Factorial of given number is:{Fact(n)}")