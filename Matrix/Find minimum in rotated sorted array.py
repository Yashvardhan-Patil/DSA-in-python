def fun(nums):
    n=len(nums)
    low=0
    high=n-1
    mini=float('inf')
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=nums[high]:
            mini=min(mini,nums[mid])
            high=mid-1
        else:
            mini=min(mini,nums[low])
            low=mid+1

            
    return mini
nums=[2,3,8,9,0,5,8]
print(fun(nums))