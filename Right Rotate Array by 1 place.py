def fun(n):
    x=len(n)
   
    for i in range(x):
        n[i],n[x-1]=n[x-1],n[i]
    

     
    return n
n=[1,5,4,8,3]
print(fun(n))
   