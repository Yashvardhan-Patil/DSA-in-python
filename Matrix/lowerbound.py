def fun(nums):
    n=len(nums)
    lowerbound=n
    low=0
    high=n-1
    target=2
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lowerbound=mid
            high=mid-1
        else:
            mid=low+1
    return lowerbound

nums=[1,2,3,4,5,6]
print(fun(nums))