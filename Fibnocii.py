def func(n):
    if n==0 or n==1:
        return n
    
    return func(n-1)+func(n-2)
n=int(input("Enter the number:"))
print(func(n))

    