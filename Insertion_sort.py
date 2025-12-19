def Insertion_sort(n):
    x=len(n)
    for i in range(1,x):
        key=n[i]
        j=i-1
        while j>=0 and n[j]>key :
            n[j+1]=n[j]
            j-=1
            
        n[j+1]=key
    return n
        
    
n=[4,8,1,7,10]
print(Insertion_sort(n))
