def fun(nums):
    n=len(nums)
    dict={}
    for i in range(0,n+1):
        dict[i]=0
    for i in nums:
        dict[i]=1
    for k,v in dict.items():
        if v==0:
            return k
nums=[0,1,2,4,5,6,7]
print(fun(nums))