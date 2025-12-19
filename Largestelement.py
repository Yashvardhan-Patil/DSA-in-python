def fun(n):
    x=len(n)
    largest=0
    for i in range (0,x):
        if n[i]>largest:
            largest=n[i]
            
    
    return largest            
 
n=[12,45,98,13]
print(fun(n))
        