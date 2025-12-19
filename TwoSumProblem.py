def fun(nums):
    n=len(nums)
   
    for i in range(n):
        for j in range(n):
            if nums[i]+nums[j]==13:
                return i,j
    return nums
        
nums=[12,1,4,8,9,10]
print(fun(nums))