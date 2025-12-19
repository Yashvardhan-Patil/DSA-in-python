def fun(nums,target):
    n=len(nums)
    low=0
    high=n-1
    floor=-1
    ceil=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]>target:
            floor=nums[mid]
            low=mid+1
        else:
            ceil=nums[mid]
            high=mid-1

    return [floor,ceil]
nums=[1,2,3,4,5,6]
print(fun(nums,3))