def fun(nums,target):
    n=len(nums)
    low=0
    high=n-1
    
    for i in range(n):
        mid=(low+high)//2
        if low>high:
            return -1
        elif nums[mid]==target:
           return nums[mid]
        elif mid>=target:
            high=mid-1
        elif mid<=target:
            low=mid+1
    return nums[mid]
nums=[1,2,3,4,5,6]
print(fun(nums,5))
