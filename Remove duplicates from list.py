def fun(n):
    x=len(n)
    freq_map={}
    for i in range(0,x):
        freq_map[n[i]]=0

    j=0
    for k in freq_map:
        n[j]=k
        j+=1

    return j

n=[1,1,1,2,3,4,7,9,10]
new=fun(n)
print(n[:new])
