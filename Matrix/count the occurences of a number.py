def fun(nums,target):
    n=len(nums)
    nums.sort()
    first=-1
    last=-1
    count=0
    for i in range(n):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i
            count=(last-first)+1
    return count
nums=[1,1,1,2,3,5,7,8]
print(fun(nums,1))
    
    
        

    
    
