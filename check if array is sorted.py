def fun(n):
    x=len(n)
    for i in range(0,x-1):
        if n[i]>n[i+1]:
            return False
    return True
n=[1,2,3,4,6]
print(fun(n))