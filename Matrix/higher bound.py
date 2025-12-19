def fun(nums):
    n=len(nums)
    higherbound=n
    low=0
    high=n-1
    target=5
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            higherbound=mid
            high=mid-1
        else:
            mid=low+1
    return higherbound

nums=[1,2,3,4,5,6]
print(fun(nums))