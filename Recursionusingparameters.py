def funct(x,n):
    if n==0:
        return
    print(x)
    funct(x,n-1)
funct(12,5)

#Print 1 to n using recursion
print("second question=")
def funct(i,n):
    if i>n:
        return
    print(i)
    funct(i+1,n)
funct(1,5)


#print 1 to n using head recursion
print("Third qyestion=")
def funct(i,n):
    if i<n:
        return
    funct(i-1,n)
    print(i)
    
funct(5,1)