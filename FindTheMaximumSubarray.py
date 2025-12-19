#subarray: continuous elements of given array is called subarray
def fuc(nums):
    n=len(nums)
    maxi=float("-infinity")
    total=0
    for i in range(0,n):
        total=total+nums[i]
        maxi=max(maxi,total)
        if total<0:
            total=0
    return maxi
nums=[-2,-5,-8,-3,2,4,7]
print(fuc(nums))