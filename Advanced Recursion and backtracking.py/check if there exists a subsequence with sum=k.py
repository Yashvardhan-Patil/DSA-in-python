#1st solution
def sub(index,total,subset):
    nums=[4,5,9]
    target=9
    if total==target:
        result.append(subset.copy())
        return True
    elif total>target:
        return False
    if index>=len(nums):
        return False
    subset.append(nums[index])
    total+=nums[index]
    pick=sub(index+1,total,subset)
    if pick==True:
        return True

    e=subset.pop()
    total=total
    notpick=sub(index+1,total,subset)
    return notpick

result=[]
print(sub(0,0,[]))

#2nd Solution
def sub(index,total):
    nums=[4,5,9]
    target=9
    if total==target:
        
        return True
    elif total>target:
        return False
    if index>=len(nums):
        return False
    
    total+=nums[index]
    pick=sub(index+1,total)
    if pick==True:
        return True

    
    total=total
    notpick=sub(index+1,total)
    return notpick

result=[]
print(sub(0,0))
