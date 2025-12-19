def fun(n):
    x=len(n)
    k=k%x
    n[:]=n[x-k:]+n[:x-k]
    return n
n=[1,5,4,7,8,9]
k=3
print(fun(n))