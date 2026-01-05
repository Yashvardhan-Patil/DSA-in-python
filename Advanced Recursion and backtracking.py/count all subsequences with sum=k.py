def sub(index,total):
    nums=[4,5,9]
    target=9
    if total==target:
        
        return 1
    elif total>target:
        return 0
    if index>=len(nums):
        return 0
    
    total+=nums[index]
    pick=sub(index+1,total)
    total=total
    notpick=sub(index+1,total)
    return pick + notpick

result=[]
print(sub(0,0))
