def fun(nums,target):
    n=len(nums)
    nums.sort()
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        if nums[mid]==nums[low]==nums[high]:
            low+=1
            mid-=1
            continue
        if nums[mid]<=nums[high]:
            if nums[mid]<=target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
        if nums[mid]>=nums[low]:
            if nums[low]<=target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
    return False
nums=[1,2,2,3,5,5,5,7,8,9,10]
print(fun(nums,5))