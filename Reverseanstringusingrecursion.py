
def func(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    func(nums,left+1,right-1)
    return nums
nums=[1,5,6,4,7]
print(func(nums,0,4))