def func(n):
    x=len(n)
    largest=0
    second_largest=0
    for i in range(0,x):
        if n[i]>largest:
            largest=n[i]
    for i in range(0,x):
        if  n[i]<largest:
            second_largest=n[i]
            
    return second_largest
n=[12,65,96,78]
print(func(n))