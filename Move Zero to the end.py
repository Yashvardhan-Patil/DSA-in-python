def fun(nums):
    n=len(nums)
    temp=[]
    for i in range(n):
        if nums[i]!=0:
            temp.append(nums[i])
    x=len(temp)
    for i in range(0,x):
        nums[i]=temp[i]
    for i in range(x,n):
        nums[i]=0
    return nums
nums=[1,3,0,4,0,5,6,0]
print(fun(nums))