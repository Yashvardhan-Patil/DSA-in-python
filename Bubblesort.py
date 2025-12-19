def bubble_sort(n):
    x=len(n)
    for i in range(x):
        m=i
        for j in range(i+1,x):
            if n[j]<n[m]:
                n[j],n[m]=n[m],n[j]
        
    return n
n=[4,8,1,2,3]
print(bubble_sort(n))