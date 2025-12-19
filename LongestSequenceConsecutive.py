def fun(nums):
    n=len(nums)
    
    my_set=set()
    for i in range(n):
        my_set.add(nums[i])
    largest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                
                x+=1
            largest=max(count,largest)
    return largest
nums=[1,5,7,6,8,10,9,12,13,15,14]
print(fun(nums))
