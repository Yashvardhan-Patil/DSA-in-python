def fun(nums):
    n=len(nums)
    i=0
    j=i+1
    max=0

    
    for i in range(n):
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                maxdiff=nums[j]-nums[i]
            if maxdiff>max:
                max=maxdiff
    return max if max> 0 else None

            
        
nums=[1,5,6,7,8,9]
print(fun(nums))


        
        